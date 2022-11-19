from data_reader import read_data
from itertools import product

arr = read_data("rosalind_lexf.txt").split("\n")
dna = "".join(arr[0].replace(" ", ""))
rep = int(arr[1])
result = list(product(dna, repeat = rep))
with open("zzzzresult.txt", "a") as fin:
    for group in result :
        fin.write("".join(group))
        fin.write("\n")
