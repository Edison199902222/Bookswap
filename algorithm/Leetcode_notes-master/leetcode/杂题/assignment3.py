import matplotlib.pyplot as plt
import numpy as np


def question_1():
    def function(x):
        return np.sin(10 * x) - x

    def derivative_function(x):
        return 10 * np.cos(10 * x) - 1

    def newton(f, f_, x, min_delta=0):
        while True:
            x_ = x - f(x) / f_(x)
            if abs(x_ - x) <= min_delta:
                return x_
            x = x_

    def interval_bisection(f, a, b, min_delta=1e-10):
        m = None
        while b - a > min_delta:
            m = a + (b - a) / 2
            if np.sign(f(a)) == np.sign(f(m)):
                a = m
            else:
                b = m

        return m

    truth_x = np.linspace(-2, 2, 10000)
    truth_y = function(truth_x)

    print("\n     ========     Interval Bisection algorithm     ========     ")
    plt.plot(truth_x, truth_y, zorder=1)
    plt.axhline(0, color='blue', zorder=1)

    ab_init = (-1, -0.8, -0.5, -0.2, 0.2, 0.5, 0.8, 1)
    for i in range(len(ab_init) - 1):
        init_a, init_b = ab_init[i:i + 2]
        #plt.fill_betweenx(truth_x, init_a, init_b,
                          #color=('orange', 'red')[i % 2], alpha=0.5, zorder=0)

        x_root = interval_bisection(function, init_a, init_b)
        print(f"The root of function when using interval [{init_a:4.1f}, {init_b:4.1f}] is {x_root:10.7f}")
        plt.scatter(x_root, function(x_root), marker='D', color='purple', s=50, zorder=1)

    plt.title(f"Interval Bisection algorithm using\n{ab_init}as the initial interval")
    plt.show()

def question_2():
    def compute_convergence_rate(in_errors):
        r_score = list()
        for r in range(1, 10):
            errors = in_errors[:]
            for i, value in enumerate(errors):
                if i == len(error) - 1:
                    continue
                errors[i] = errors[i + 1] / np.power(errors[i], r)

            errors = np.array(errors[:-1])
            r_score.append(np.linalg.norm(errors - np.mean(errors)))

        return np.argmin(r_score) + 1


    z = 81
    x = 70
    min_delta = 1e-10
    error = list()

    while True:
        x_ = (z + x) / (1 + x)
        error.append(x_ - np.sqrt(z))
        if abs(x_ - x) <= min_delta:
            break
        x = x_

    iteration = np.arange(len(error))
    plt.plot(iteration, error, label="Iteration errors")
    plt.plot(iteration[::2], error[::2], label="Even iteration errors")
    plt.plot(iteration[1::2], error[1::2], label="Odd iteration errors")
    plt.legend()
    plt.title("Errors $x_k-\\sqrt{z}$ for $x_{k+1}=(z+x_k)/(1+x_k)$ with z = 81, $x_0$ = 70")
    plt.show()

    print(f"Convergence rate for part a is {compute_convergence_rate(error)}")

    x = 70
    error = list()
    while True:
        x_ = 0.5 * (x + z / x)
        error.append(x_ - np.sqrt(z))
        if abs(x_ - x) <= min_delta:
            break
        x = x_

    iteration = np.arange(len(error))
    plt.plot(iteration, error, label="Iteration errors")
    plt.legend()
    plt.title("Errors $x_k-\\sqrt{z}$ for $x_{k+1}=0.5(x_k + z / x_k)$ with z = 81, $x_0$ = 70")
    plt.show()

    print(f"Convergence rate for part b is {compute_convergence_rate(error)}")

    print("Question is the same as: what is the root of f(x) = z - x ** n")
    print("f(x) = z - x ** n | f'(x) = -n * x ** (n - 1)")

question_1()
