from data_reader import read_data

info = read_data("rosalind_fibd (2).txt").split()
arr = [0]*int(info[1])
arr[1] = 1; arr[0] = 1
timer = int(info[0])-2
family = len(arr)
while timer >=0:
    tmp = arr[0]
    new_bebe = 0
    for count in range(1, family):
        new_bebe += arr[count]
    for cou in range(family-1, 1, -1):
       arr[cou] = arr[cou-1]
    arr[1] = tmp
    arr[0]= new_bebe
    timer-=1
print (arr[0])
