import math
import sys


#     a b c d e f g h i j k l m n o
a = [[0,4,4,0,0,0,0,0,0,0,0,0,0,0,0], # a
     [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # b
     [4,0,0,3,7,0,0,0,0,0,0,0,0,0,0], # c
     [0,0,3,0,0,0,0,0,0,0,0,0,0,0,0], # d
     [0,0,0,0,0,1,2,0,0,0,0,0,0,0,0], # e
     [0,0,0,0,1,0,0,3,7,0,0,0,0,0,0], # f
     [0,0,0,0,2,0,0,0,0,0,0,0,0,0,0], # g
     [0,0,0,0,0,3,0,0,0,0,0,0,0,0,0], # h
     [0,0,0,0,0,7,0,0,0,3,8,0,0,0,0], # i
     [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0], # j
     [0,0,0,0,0,0,0,0,8,0,0,2,2,0,0], # k
     [0,0,0,0,0,0,0,0,0,0,2,0,0,0,0], # l
     [0,0,0,0,0,0,0,0,0,0,2,0,0,1,2], # m
     [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0], # n
     [0,0,0,0,0,0,0,0,0,0,0,0,2,0,0], # 0
    ]

#     a      b      c      d      e      f      g      h      i      j      k      l      m      n      o
b = [(1,5), (2,4), (2,2), (4,3), (5,2), (5,3), (6,1), (7,2), (7,4), (8,4), (9,2), (10,3), (8,1), (7,1), (10,1)]

def eucledian(g):
     D = []
     e = len(g) - 1
     for i in range(len(g)):
          x = math.sqrt(((g[e][0] - g[i][0]) ** 2) + ((g[e][1] - g[i][1]) ** 2))
          D.append(round(x, 3))
     return D

def searchAstar(g, c, s, e, robust_output):
     h = eucledian(c)
     P = []
     dist = []
     open = []
     closed = []
     current = s
     f = []
     for i in range(len(g)):
          f.append([])
     for i in range(len(g)):
          dist.append([])
     dist[0].append(0)
     x = 0 + h[current]
     f[current].append(x)
     open.append(current)
     while current != e:
          for i in range(len(g[current])):
               if g[current][i] != 0:
                    if i not in closed:
                         if i not in open:
                              open.append(i)
                              # f function calculation
                              x = (g[current][i] + h[i])
                              #store data such as f function, parent, and distance
                              if f[i] == []:
                                   f[i].append(x)
                                   P.append((i, current))
                                   dist[i].append(dist[current][0] + g[current][i])
                              elif x > f[i][0]:
                                   f[i] = []
                                   f[i].append(x)
                                   P.append((i, current))
                                   dist[i].append(dist[current][0] + g[current][i])
          closed.append(current)
          open.remove(current)
          lowest = float(sys.maxsize)
          #find lowest f function value in the open list
          for i in range(len(open)):
               j = open[i]
               if f[j][0] < lowest:
                    lowest = f[j][0]
                    index = j
          current = index
     #create shortest path list
     last = P[-1][1]
     path = [P[-1]]
     counter = 0
     while last != 0:
          for i in range(len(P)):
               if P[i][0] == last:
                    path.insert(0, P[i])
                    last = P[i][1]
                    counter +=1
     if robust_output == True:
          return f, path, dist[-1][0], len(closed)
     else:
          return path, dist[-1][0], len(closed)






print(searchAstar(a, b, 0, 14, False))
