from data_reader import read_data
from itertools import permutations

number = int(read_data("rosalind_perm.txt"))+1
l = list(range(1, number))
l = list(map(str,list(permutations(l))))
with open("zzzzresult.txt", "a") as res:
    res.write(str(len(l)))
    res.write("\n")
for item in l: 
    for char in item:
        if char in ["1","2","3","4","5","6","7","8","9","0"]:
            char = char + " "
            with open("zzzzresult.txt", "a") as res:
                res.write(str(char))
    with open("zzzzresult.txt", "a") as res:
        res.write("\n")
