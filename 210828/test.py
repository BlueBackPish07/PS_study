import sys
import heapq
from collections import defaultdict
N, M, X  = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for i in range(M):
    s, e ,c = map(int, sys.stdin.readline().split())
    graph[N].append((e,c))