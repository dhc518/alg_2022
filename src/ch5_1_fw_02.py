n_vertices = 19
edges = [
  (0, 1, 565), (0, 4, 473), (0, 6, 124), (0, 18, 448), (1, 4, 166), 
  (1, 6, 257), (1, 7, 532), (1, 16, 323), (2, 5, 169), (2, 8, 172), 
  (2, 11, 255), (2, 15, 526), (3, 8, 154), (3, 11, 381), (3, 12, 240), 
  (3, 13, 464), (3, 15, 375), (3, 16, 220), (3, 17, 318), (4, 10, 280), 
  (5, 9, 374), (5, 13, 484), (6, 10, 179), (6, 13, 445), (6, 17, 93), 
  (7, 13, 211), (7, 17, 313), (9, 12, 47), (9, 13, 239), (9, 14, 217), 
  (11, 14, 430), (12, 13, 305), (12, 14, 228), (15, 18, 249), (17, 18, 386)
]

# 함수는 사용하지 않고 작성한다 (키워드 def 를 사용하지 않는다)
# 결과는 12x12 의 표 형태로 비용을 출력한다.

# 1. Edge List -> Adj Matrix 형태로 변환 
# 2. 2차원 배열 D 에 0, 비용, inf 중 하나를 넣어 초기화
INF = float('inf')
D = [[ INF for _ in range(n_vertices) ] for _ in range(n_vertices) ] # n x n 의 INF
P = [[ -1 for _ in range(n_vertices) ] for _ in range(n_vertices) ] # n x n 의 INF
for i in range(n_vertices):
    # ... # 0 이 들어가는 경우 (출발지/도착지 같은 경우)
    D[i][i] = 0
for u,v,w in edges:
    # ... # 알려진 비용
    D[u][v] = w
    D[v][u] = w
    # ... 
print(D)
# 3. k 를 0 부터 11 까지 변환하며 비용 갱신
for k in range(n_vertices):
  for i in range(n_vertices):
    if i == k: continue
    for j in range(n_vertices):
      if j == i or j == k: continue
      # ... # D[i][j] 와 D[i][k] + D[k][j] 를 비교한다
      t = D[i][k] + D[k][j]
      if ...:
        ...
# 4. (opt) 갱신할 때 i 부터 j 까지 가려면 k 로 가야한다 라는 내용도 추가 저장
# 5. D 의 내용을 출력한다
for i in range(n_vertices):
  for j in range(n_vertices):
    print(f'{D[i][j]:4d} ', end='')
  print()

def path(i, j):
  k = P[i][j]
  if k < 0: return f'->{j}'
  return f'{path(i,k)}{path(k,j)}'

for i in range(n_vertices):
  print(f'from {i}:')
  for j in range(n_vertices):
    if i == j: continue
    print(f' to {j}: {i}{path(i,j)}')

#    0  381  861  535  473 1030  124  530  689  808  303  916  775  569 1003  697  704  217  448 
#  381    0  869  543  166 1038  257  532  697  830  436  924  783  702 1011  918  323  350  736 
#  861  869    0  326 1035  169  737  864  172  543  916  255  566  653  685  526  546  644  775 
#  535  543  326    0  709  495  411  631  154  287  590  381  240  464  468  375  220  318  624 
#  473  166 1035  709    0 1204  423  698  863  996  280 1090  949  868 1177 1084  489  516  902 
# 1030 1038  169  495 1204    0  906  695  341  374 1085  424  421  484  591  695  715  813  944 
#  124  257  737  411  423  906    0  406  565  684  179  792  651  445  879  728  580   93  479 
#  530  532  864  631  698  695  406    0  785  450  585 1012  497  211  667  948  851  313  699 
#  689  697  172  154  863  341  565  785    0  441  744  427  394  618  622  529  374  472  778 
#  808  830  543  287  996  374  684  450  441    0  863  647   47  239  217  662  507  605  911 
#  303  436  916  590  280 1085  179  585  744  863    0  971  830  624 1058  907  759  272  658 
#  916  924  255  381 1090  424  792 1012  427  647  971    0  621  845  430  756  601  699 1005 
#  775  783  566  240  949  421  651  497  394   47  830  621    0  286  228  615  460  558  864 
#  569  702  653  464  868  484  445  211  618  239  624  845  286    0  456  839  684  524  910 
# 1003 1011  685  468 1177  591  879  667  622  217 1058  430  228  456    0  843  688  786 1092 
#  697  918  526  375 1084  695  728  948  529  662  907  756  615  839  843    0  595  635  249 
#  704  323  546  220  489  715  580  851  374  507  759  601  460  684  688  595    0  538  844 
#  217  350  644  318  516  813   93  313  472  605  272  699  558  524  786  635  538    0  386 
#  448  736  775  624  902  944  479  699  778  911  658 1005  864  910 1092  249  844  386    0 

# 6. (opt) 12x11 의 경로들을 모두 출력해도 좋다. 이 경우 함수를 이용한다

# 6번은 다음과 같은 형태로 출력한다.
# from 0:
#  to 1: 0->6->1
#  to 2: 0->6->17->3->8->2
#  to 3: 0->6->17->3
#  to 4: 0->4
#  to 5: 0->6->17->3->8->2->5
#  to 6: 0->6
#  to 7: 0->6->17->7
#  to 8: 0->6->17->3->8
#  to 9: 0->6->13->9
#  to 10: 0->6->10
#  to 11: 0->6->17->3->11
#  to 12: 0->6->17->3->12
#  to 13: 0->6->13
#  to 14: 0->6->17->3->12->14
#  to 15: 0->18->15
#  to 16: 0->6->1->16
#  to 17: 0->6->17
#  to 18: 0->18
# from 1:
#  to 0: 1->6->0
#  to 2: 1->16->3->8->2
#  to 3: 1->16->3
#  to 4: 1->4
#  to 5: 1->16->3->8->2->5
#  to 6: 1->6
#  to 7: 1->7
#  to 8: 1->16->3->8
#  to 9: 1->16->3->12->9
#  ... (하략)
