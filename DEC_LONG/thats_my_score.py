#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    problem_and_maxScore = dict()
    N = int(input())
    for submission in range(N) :
        p, s = map(int, input().split())
        if p > 8 :
            pass
        else :
            if p in problem_and_maxScore :
                maxScore = problem_and_maxScore[p]
                if s > maxScore :
                    problem_and_maxScore[p] = s
            else :
                problem_and_maxScore[p] = s
    print(sum(problem_and_maxScore.values()))