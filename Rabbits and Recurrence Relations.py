from data_reader import read_data
info = read_data("rosalind_fib.txt").split()
month = int(info[0])
fertility = int(info[1])
family = [1, 0]
for __ in range(month):
  tmp = family[0]
  family[0] = family[1]*ferility
  family[1] += tmp
print(family[0])
