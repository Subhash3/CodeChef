#!/usr/bin/python3

def max_height(c, f, N) :
    c.sort(reverse=True)
    f.sort(reverse=True)
    height = 0
    i = 0
    while i < N :
        # print(c, f)
        max_avg = 0
        min_index = None
        i = j = 0
        while j < N :
            # print("max_avg:", max_avg)
            # print(c[i], f[j])
            avg = int((c[i] + f[j])/2)
            # print("avg:", avg)
            if avg > max_avg :
                # print("max >  avg... updating max")
                max_avg = avg
                min_index = j
            elif avg == max_avg and f[j] < f[min_index] :
                # print(f[j])
                min_index = j
            else :
                break
            j += 1
        height += max_avg
        # print("height:", height)
        # print(c[i], f[min_index])
        c.pop(i)
        f.pop(min_index)
        N -= 1
        # print(N)
        i += 1
    
    height += int((c[0]+f[0])/2)
    return height    

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N = int(input())
    chefs_heights = list(map(int, input().split()))
    chefettes_heights = list(map(int, input().split()))
    height = max_height(chefs_heights, chefettes_heights, N)
    print(height)
