import random
from leetcode.fourclass_training import LAM

def random_list():
    A = []
    for i in range(5000000):
        x = random.randint(-500,500)
        while x == 0:
            x = random.randint(-500, 500)
        A.append(x)
    return A
def main():
    random.seed(2)
    lists1 = random_list()
    lists2 = random_list()
    i = 0
    j = 0
    ans = []
    MRED = 0
    MED = 0
    MSE = 0
    max_value = float("-inf")
    while i < len(lists1) and j < len(lists2):
        result1 = lists1[i] * lists2[j]
        result2 = LAM.approx_multiplication(lists1[i], lists2[j])

        MRED += (abs(result2 - result1))/abs(result1)

    MRED /= 5000000
    print(MRED)

main()

'''
LAM_ref:
ER: 99.968%
MRED: 0.12159491252926169
MED: 6676.28664446678
NMED: 0.026705146577867118

proposed_LAM
ER: 99.968%
MRED: 0.13077169459344135
MED: 5788.986495580547
NMED: 0.023155945982322186
'''