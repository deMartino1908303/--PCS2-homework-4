from collections import Counter
from data_reader import read_data
def molt(char):
    arrx2 = ["F", "Y", "C", "H", "Q", "N", "K", "D", "E"]
    arrx4 = ['P', 'T', 'V', 'A', 'G']
    arrx6 = ["R", "S", "L"]
    arrx1 = ["W", "M"]
    if char in arrx2 : return 2
    elif char in arrx4 : return 4
    elif char in arrx6 : return 6
    elif char in arrx1 : return 1
    else : return 3

string = read_data("rosalind_mrna.txt")
dictio = Counter(string.strip())
arr = dict(dictio)
total = 3
for var in arr:
    multipier = molt(var)
    total = total * pow(multipier, arr[var])
print((total)%1000000)
