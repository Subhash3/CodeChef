#!/usr/bin/python3

dp = dict()

def add(A, B) :
    iterations = 0
    while B > 0 :
        print("DP: ", dp)
        if (A, B) in dp :
            return A, iterations+dp[(A, B)]
        dp[(A, B)] = iterations + 1
        U = A ^ B
        V = A & B
        A = U
        B = V * 2
        iterations += 1
        print("\tA: ", A, ", B: ", B, ", U: ", U, ", V: ", V, ", Iterations:", iterations, sep="")
    # dp[(A, B)] = iterations
    return A, iterations

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    A = int(input(), 2)
    B = int(input(), 2)

    print("Testcase:", testCase+1, "A: ", A, "B: ", B)
    ans = add(A, B)
    print("\t" + str(ans))
    print(ans[1])