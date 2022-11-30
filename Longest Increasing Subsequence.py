#i found the algoritmh online and wrote this program based on that
from data_reader import read_data
def Longest_sub_sec(nums, n, func):

    base_list = []      

    new_list = [] 

    for counter1 in range(n):

        base_list.append(1)

        new_list.append([nums[counter1]])

        for counter2 in range(counter1):

            if func(nums[counter2], nums[counter1]):

                base_list[counter1] = max(base_list[counter1], base_list[counter2] + 1)

                if len(new_list[counter1]) <= len(new_list[counter2]):

                    new_list[counter1] = new_list[counter2] + [nums[counter1]]

    return max(base_list, new_list[base_list.index(max(base_list))])



info = read_data("rosalind_lgis.txt").split("\n")

max_n = int(info[0])

nums = list(map(int, info[1].split()))

incr = (Longest_sub_sec(nums, max_n, lambda a, b: a<b))
decr = (Longest_sub_sec(nums, max_n, lambda a, b :a> b))

incr = list(map(str, incr))
decr = list(map(str, decr))

with open("result.txt", "a") as done:
    done.write(" ".join(incr))
    done.write("\n")
    done.write(" ".join(decr))
