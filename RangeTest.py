import random

max_length = 10
x = [i for i in range(max_length)]
y = [i for i in range(max_length)]
seq = ''
for i in range(max_length):
  seq += '((' + str(x.pop(random.randint(0, len(x)-1))) + \
    ',' + str(y.pop(random.randint(0, len(y)-1))) + '),' + \
    str(random.randint(0, max_length)) + '),'
seq = 'val points0 = [' + seq[:-1] + ']'
print(seq)

tests = ''
for i in range(max_length//2):
  tests += '(points0, ' + '(' + str((i,max_length-i)) + ',' + str((max_length-i,i)) + ')),\n'
print(tests[:-2])