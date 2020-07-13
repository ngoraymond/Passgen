
# generate test cases for fingerlab!

import sys

def build_tree(lst):
  if len(lst) == 0:
    return 'L'
  mid = len(lst) // 2
  tree = 'N (' + build_tree(lst[:mid]) + ', ' + str(lst[mid]) + ', ' + build_tree(lst[mid+1:]) + ')'
  return tree

if __name__ == "__main__":

  if len(sys.argv) != 2:
    print('ERROR! usage: $ python3 fingerlab_tests.py NUMBER_OF_NODES')
    exit(0)

  nodes = int(sys.argv[1])
  lst = [i+1 for i in range(nodes)]

  for i in range(nodes):
    print('val gen' + str(i+1) + ' : unit Tree.t =')
    print(' ' + build_tree(lst[:i]))
    print()