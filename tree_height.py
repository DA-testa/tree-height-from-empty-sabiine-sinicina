# python3

import sys
import threading


def compute_height(n, parents):
    adj_list = [[] for _ in range(n)]
    for i, p in enumerate(parents):
        if p != -1:
            adj_list[p].append(i)

    def dfs(v, adj_list):
        max_height = 0
        for u in adj_list[v]:
            max_height = max(max_height, dfs(u, adj_list))
        return max_height + 1

    root = parents.index(-1)
    height = dfs(root, adj_list)
    return height

def main():
    input_type = input()

    if input_type == "F":
        filename = input()
        if ".a" in filename:
            return
        #if "test/" not in filename:
            #filename = "test/" + filename
        with open(filename) as f:
            n = int(f.readline().strip())
            parents = list(map(int, f.readline().strip().split()))
    elif input_type == "I":
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        return
    print(compute_height(n, parents))
    


    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
