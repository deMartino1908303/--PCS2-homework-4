from data_reader import read_data
info = read_data("rosalind_fib.txt").split()
child = 1
parent = 0
for _ in range(1,int(info[0])) : child, parent = parent , parent + (child * int(info[1]))
print(child)
