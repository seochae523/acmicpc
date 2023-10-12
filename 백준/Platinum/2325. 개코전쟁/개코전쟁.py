import sys
from collections import deque
import heapq
input = sys.stdin.readline
INF = float("inf")

def dijkstra(start, s, e):

    distance = [INF for i in range(N+1)]
    heap = [[0, start]]
    distance[start] = 0
    while(heap):
        dis, node = heapq.heappop(heap)
        if node in graph:
            for nextDis, nextNode in graph[node]:
                if nextNode == s and node == e or node == s and nextNode == e:
                    continue
                if(distance[nextNode] > nextDis + distance[node]):
                    distance[nextNode] = nextDis + distance[node]
                    heapq.heappush(heap, [distance[nextNode], nextNode])




    return distance

def findPath():
    path = []
    visited = [False for i in range(N+1)]
    visited[N] = True
    queue = deque()
    queue.append(N)

    while queue:
        node = queue.popleft()
        path.append(node)
        if node == 1:
            break
        if node in graph:
            for nextDist, nextNode in graph[node]:
                if distance[nextNode] + nextDist == distance[node] and not visited[nextNode]:
                    visited[nextNode] = True
                    queue.append(nextNode)
    return path


N, M = map(int, input().split())
graph = {}
path = []
for i in range(M):
    s, e, l = map(int, input().split())
    try:
        graph[s].append([l, e])
    except:
        graph[s] = [[l, e]]

    try:
        graph[e].append([l, s])
    except:
        graph[e] = [[l, s]]

distance = dijkstra(1, 0, 0)
path = findPath()


maxDist = -1
for i in range (len(path)-1):
    
    newDist = dijkstra(1, path[i], path[i+1])
    if maxDist < newDist[N]:
        maxDist = newDist[N]

print(maxDist)