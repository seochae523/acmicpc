import sys
from collections import deque
import heapq
input=sys.stdin.readline
INF=float("inf")

def dijkstra():
    distance=[INF for i in range(V)]
    heap=[[0,K]]
    distance[K]=0
    while(heap):
        dis,node=heapq.heappop(heap)
        if(node in graph):
            for nextDis,nextNode in graph[node]:
                if(distance[nextNode]>nextDis+distance[node]):
                    distance[nextNode]=nextDis+distance[node]
                    heapq.heappush(heap,[distance[nextNode],nextNode])
    for d in distance:
        if(d==INF):
            print("INF")
        else:
            print(d)



V,E=map(int,input().split())
K=int(input())
K-=1
graph={}
for i in range(E):
    u,v,w=map(int,input().split())
    u-=1
    v-=1
    try:
        graph[u].append([w,v])
    except:
        graph[u]=[[w,v]]


dijkstra()