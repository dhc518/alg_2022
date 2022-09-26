from data_unsorted import numbers
# from data_unsorted_a_lot import numbers
from random import randint, seed, shuffle
from vis import SelectionSortVisualizer as Visualizer
# from vis import Dummy as Visualizer
from time import time

def main():
  print('before:', array)
  count = len(array)

  for a in range(count):
    min_value = array[a]
    min_at = a
    vis.selection(a)
    for b in range(a + 1, count):
      vis.compare(min_at, b)
      if min_value > array[b]:
        min_value = array[b]
        min_at = b
        vis.selection(b)
    vis.swap(a, min_at)
    array[a], array[min_at] = array[min_at], array[a]
    vis.mark_done(a)
    # print(f'{min_at=}. swap {a} <=> {min_at}')

  print('after :', array)

'''
Comparison: 45
Swap: 10

성능측정:
count=100 elapsed=0.000
count=1000 elapsed=0.023
count=2000 elapsed=0.086
count=3000 elapsed=0.191
count=4000 elapsed=0.331
count=5000 elapsed=0.545
count=6000 elapsed=0.878
count=7000 elapsed=1.211
count=8000 elapsed=1.523
count=9000 elapsed=1.893
count=10000 elapsed=2.321
count=15000 elapsed=5.350
count=20000 elapsed=9.383
count=30000 elapsed=21.163
count=40000 elapsed=37.976
count=50000 elapsed=59.333
'''


if __name__ == '__main__':
  seed('Hello') # 'Hello' 를 seed 로 고정하여 randint 가 항상 같은 결과가 나오게 한다

  # counts = [ 
  #   100, 1000, 2000, 3000, 4000, 5000, 
  #   6000, 7000, 8000, 9000, 10000, 15000, 
  #   20000, 30000, 40000, 50000 ]
  # for count in counts:
  #   array = numbers[:count]
  #   shuffle(array)
  #   startedOn = time()
  #   main()
  #   elapsed = time() - startedOn
  #   print(f'{count=} {elapsed=:.3f}')
  # exit() 

  vis = Visualizer('Selection Sort')

  while True:
    count = randint(10, 30)
    array = numbers[:count]
    vis.setup(vis.get_main_module())
    main()
    vis.draw()

    again = vis.end()
    if not again: break

