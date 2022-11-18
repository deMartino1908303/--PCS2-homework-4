from data_reader import read_data

tmp_dna_str = read_data("rosalind_hamm .txt").split("\n")
dna_str1 = tmp_dna_str[0]
dna_str2 = tmp_dna_str[1]

counter = 0
diff_counter = 0
while counter < len(dna_str1):
    if dna_str1[counter] != dna_str2[counter] : diff_counter += 1
    counter += 1
print (diff_counter)
