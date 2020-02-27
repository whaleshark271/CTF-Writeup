from z3 import *

length = 24
my_flag = [BitVec('f_' + str(i), 8) for i in range(length)]

key = [21, 23, 9, 22, 3, 16, 17, 7, 8, 10, 11, 4, 0, 2, 13, 6, 1, 14, 18, 19, 5, 20, 12, 15]
check_values = [247, 220, 217, 225, 154, 146, 217, 173, 173, 244, 245, 225, 199, 148, 106, 163, 159, 106, 106, 173, 244, 244, 173]

s = Solver()
for k1, k2 in zip(key[:-1], key[1:]):
	s.add(my_flag[k1] + my_flag[k2] == check_values[0])
	check_values = check_values[1:]

s.add(my_flag[0] == ord('f'))
s.add(my_flag[1] == ord('l'))
s.add(my_flag[2] == ord('a'))
s.add(my_flag[3] == ord('g'))

assert s.check() == sat
m = s.model()
flag = ''.join([chr(m[i].as_long()) for i in my_flag])
print(flag)
