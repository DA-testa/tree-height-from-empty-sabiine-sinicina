# python3

import sys
import threading


def compute_height(n, parents):
    # create adjacency list
    adj_list = [[] for _ in range(n)]
    for i, p in enumerate(parents):
        if p != -1:
            adj_list[p].append(i)

    # perform DFS to compute height
    def dfs(v):
        max_height = 0
        for u in adj_list[v]:
            max_height = max(max_height, dfs(u))
        return max_height + 1

    root = parents.index(-1)
    height = dfs(root)
    return height


def main():
    input_type = input()
    if input_type == "F":
        filename = input()
        if ".a" in filename:
            return
        if "test/" not in filename:
            filename = "test/" + filename
        with open(filename) as f:
            n = int(f.readline().strip())
            parents = list(map(int, f.readline().strip().split()))
    elif input_type == "I":
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        return
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

