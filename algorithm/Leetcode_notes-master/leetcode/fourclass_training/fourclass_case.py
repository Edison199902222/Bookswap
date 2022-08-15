import math
import numpy as np
from sklearn.model_selection import train_test_split

from leetcode.fourclass_training import LAM_decimal


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def sigmoid_backward(d, y):
    sig = sigmoid(y)
    return d * sig * (1.0 - sig)


def relu_backward(d, y):
    dy = np.array(d, copy=True)
    dy[y <= 0] = 0
    return dy


def init_layers(nn_architecture, seed=1):
    np.random.seed(seed)
    number_of_layers = len(nn_architecture)
    params_values = {} #intial weight and bias

    for idx, layer in enumerate(nn_architecture):
        layer_idx = idx + 1
        layer_input_size = layer["input_dim"]
        layer_output_size = layer["output_dim"]

        params_values['W' + str(layer_idx)] = np.random.randn(
            layer_output_size, layer_input_size) * 0.1
        params_values['b' + str(layer_idx)] = np.random.randn(
            layer_output_size, 1) * 0.1
    #print(params_values)
    return params_values


def dot(A, B):
    C = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(B.shape[0]):
                #C[i][j] += A[i][k] * B[k][j]
                C[i][j] += LAM_decimal.approx_multiplication(A[i][k], B[k][j])
    return C

def single_layer_forward_propagation(A_prev, W_curr, b_curr, activation="relu"):
    #Z_curr = np.dot(W_curr, A_prev) + b_curr
    Z_curr = dot(W_curr, A_prev) + b_curr
    if activation == "relu":
        activation_func = relu
    elif activation == "sigmoid":
        activation_func = sigmoid
    else:
        raise Exception('Non-supported activation function')

    return activation_func(Z_curr), Z_curr


def full_forward_propagation(X, params_values, nn_architecture):
    memory = {}
    A_curr = X
    for idx, layer in enumerate(nn_architecture):
        layer_idx = idx + 1
        A_prev = A_curr

        activ_function_curr = layer["activation"]
        W_curr = params_values["W" + str(layer_idx)]
        b_curr = params_values["b" + str(layer_idx)]

        A_curr, Z_curr = single_layer_forward_propagation(A_prev, W_curr, b_curr, activ_function_curr)
        memory["A" + str(idx)] = A_prev
        memory["Z" + str(layer_idx)] = Z_curr

    return A_curr, memory


def get_cost_value(Y_hat, Y): #cross entropy
    m = Y_hat.shape[1]
    cost = -1 / m * (np.dot(Y, np.log(Y_hat).T) + np.dot(1 - Y, np.log(1 - Y_hat).T))

    return np.squeeze(cost) #return cost value


def convert_prob_into_class(probs):
    probs_ = np.copy(probs)
    probs_[probs_ > 0.5] = 1
    probs_[probs_ <= 0.5] = 0

    return probs_


def get_accuracy_value(Y_hat, Y):
    Y_hat_ = convert_prob_into_class(Y_hat)
    return (Y_hat_ == Y).all(axis=0).mean()


def single_layer_backward_propagation(dA_curr, W_curr, b_curr, Z_curr, A_prev, activation="relu"):
    m = A_prev.shape[1]

    if activation == "relu":
        backward_activation_func = relu_backward
    elif activation == "sigmoid":
        backward_activation_func = sigmoid_backward
    else:
        raise Exception('Non-supported activation function')

    dZ_curr = backward_activation_func(dA_curr, Z_curr)
    '''dW_curr = np.dot(dZ_curr, A_prev.T) / m
    db_curr = np.sum(dZ_curr, axis=1, keepdims=True) / m
    dA_prev = np.dot(W_curr.T, dZ_curr)'''

    dW_curr = dot(dZ_curr, A_prev.T) / m
    db_curr = np.sum(dZ_curr, axis=1, keepdims=True) / m
    dA_prev = dot(W_curr.T, dZ_curr)

    return dA_prev, dW_curr, db_curr


def full_backward_propagation(Y_hat, Y, memory, params_values, nn_architecture):
    grads_values = {}
    m = Y.shape[1]
    Y = Y.reshape(Y_hat.shape)

    dA_prev = - (np.divide(Y, Y_hat) - np.divide(1 - Y, 1 - Y_hat))

    for i in range(dA_prev.shape[1]):
        if math.isinf(dA_prev[0][i]) or math.isnan(dA_prev[0][i]):
            dA_prev[0][i] = 0.0
    #print(dA_prev)
    for layer_idx_prev, layer in reversed(list(enumerate(nn_architecture))):
        layer_idx_curr = layer_idx_prev + 1
        activ_function_curr = layer["activation"]

        dA_curr = dA_prev

        A_prev = memory["A" + str(layer_idx_prev)]
        Z_curr = memory["Z" + str(layer_idx_curr)]
        W_curr = params_values["W" + str(layer_idx_curr)]
        b_curr = params_values["b" + str(layer_idx_curr)]

        dA_prev, dW_curr, db_curr = single_layer_backward_propagation(
            dA_curr, W_curr, b_curr, Z_curr, A_prev, activ_function_curr)

        grads_values["dW" + str(layer_idx_curr)] = dW_curr
        grads_values["db" + str(layer_idx_curr)] = db_curr

    return grads_values


def update(params_values, grads_values, nn_architecture, learning_rate):
    for layer_idx, layer in enumerate(nn_architecture, 1):
        params_values["W" + str(layer_idx)] -= learning_rate * grads_values["dW" + str(layer_idx)]
        params_values["b" + str(layer_idx)] -= learning_rate * grads_values["db" + str(layer_idx)]

    return params_values


# %%


def train(X, Y, nn_architecture, epochs, learning_rate):
    params_values = init_layers(nn_architecture, 2)
    cost_history = []
    accuracy_history = []

    for i in range(epochs):
        Y_hat, cashe = full_forward_propagation(X, params_values, nn_architecture)
        '''cost = get_cost_value(Y_hat, Y)
        cost_history.append(cost)
        accuracy = get_accuracy_value(Y_hat, Y)
        accuracy_history.append(accuracy)'''

        grads_values = full_backward_propagation(Y_hat, Y, cashe, params_values, nn_architecture)
        params_values = update(params_values, grads_values, nn_architecture, learning_rate)
        #print(params_values)
    return params_values, cost_history, accuracy_history


# %%

#Fourclass
import csv
csvfile = open('fourclass_features.csv', 'r',encoding='utf-8-sig')
reader = csv.reader(csvfile)
ls = []
for item in reader:
    item = list(map(float, item))
    ls.append(item)
X = np.array(ls)

X = X.astype('float32')

csvfile2 = open('fourclass_target.csv', 'r',encoding='utf-8-sig')
reader2 = csv.reader(csvfile2)

ls2 =[]
for i in reader2:
    i = list(map(int, i))
    ls2.append(i)
y = np.array(ls2)
y = y.astype('float32')

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, test_size=0.2)
# %%
# %%

NN_ARCHITECTURE = [
    {"input_dim": 2, "output_dim": 8, "activation": "relu"},
    {"input_dim": 8, "output_dim": 1, "activation": "sigmoid"},
]

# Train
params_values = train(np.transpose(X_train),
                      np.transpose(y_train.reshape((y_train.shape[0], 1))),
                      NN_ARCHITECTURE, 9000, 0.1)[0]
# %%0.99(0.1,9000,2-8-1,random_state=1)

import json
from json import JSONEncoder
import numpy

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


# Serialization
with open("fourclass_LAM.json", "w") as write_file:
    json.dump(params_values, write_file, cls=NumpyArrayEncoder)

# Deserialization
'''''
with open("fourclass_LAM.json", "r") as read_file:
    decodedArray = json.load(read_file)

    finalNumpyArray1 = numpy.asarray(decodedArray["W1"])
    finalNumpyArray2 = numpy.asarray(decodedArray["b1"])
    finalNumpyArray3 = numpy.asarray(decodedArray["W2"])
    finalNumpyArray4 = numpy.asarray(decodedArray["b2"])

    trained_params = {} #trained_parameter
    trained_params['W1'] = finalNumpyArray1
    trained_params['b1'] = finalNumpyArray2
    trained_params['W2'] = finalNumpyArray3
    trained_params['b2'] = finalNumpyArray4
    
# Inference
Y_test_hat, _ = full_forward_propagation(np.transpose(X_test), params_values, NN_ARCHITECTURE)


# Accuracy achieved on the test set
acc_test = get_accuracy_value(Y_test_hat, np.transpose(y_test.reshape((y_test.shape[0], 1))))
print("Test set accuracy: {:.2f}".format(acc_test))
'''
# %%


