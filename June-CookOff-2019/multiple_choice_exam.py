#!/usr/bin/python3

def get_score(N, correct_ans, chef_ans) :
    score = 0
    evaluate = True
    for i in range(N) :
        if evaluate :
            if chef_ans[i] == correct_ans[i] :
                # print("correct")
                score += 1
            elif chef_ans[i] == 'N' :
                # print("Unanswered")
                pass
            else :
                # print("Wrong")
                evaluate = False
        else :
            # print("Skipping this one, cuz previous one is wrong")
            evaluate = True
    return score

try : 
    T = int(input())
except :
    quit()
for test_case in range(T) :
    N = int(input())
    correct_ans = input()
    chef_ans = input()
    score = get_score(N, correct_ans, chef_ans)
    print(score)