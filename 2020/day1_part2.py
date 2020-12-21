# Merging Sort Solution 
def merge_sort(L:list):
    if len(L) == 1:
        return L
    A = merge_sort(L[0:len(L)//2])
    B = merge_sort(L[len(L)//2:])
    R = []
    ai, bi = 0, 0
    while ai < len(A) and bi < len(B):
        if A[ai] < B[bi]:
            R.append(A[ai])
            ai += 1
        else:
            R.append(B[bi])
            bi += 1
    if ai < len(A):
        R.extend(A[ai:])
    else:
        R.extend(B[bi:])
    return R

# read in list
file_in = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day1_data.txt'
with open(file_in,'r') as f:
    string_list = f.readlines()
num_list=[]
for item in string_list:
    item = int(item[:-1])
    num_list.append(item)   

# sort the list
sorted_list = merge_sort(num_list)

# Search for two number that sum to special number
def search_sum(sum_number, index_range:tuple, sorted_list:list):
    left_index, right_index = index_range
    while left_index < right_index:
        left_num = sorted_list[left_index]
        right_num = sorted_list[right_index]
        sum = left_num + right_num
        if sum == sum_number:
            break
        if sum > sum_number:
            right_index -= 1
        if sum < sum_number:
            left_index += 1
    if sum == sum_number:
        return left_index, right_index, left_num, right_num, sum
    else:
        return False

# loop through the list to find three numbers added to 2020
for i in range(len(sorted_list)-2):
    result = search_sum((2020-sorted_list[i]), (i+1,len(sorted_list)-1), sorted_list)
    if not result:
        pass
    else:
        num1 = sorted_list[i]
        num2 = result[2]
        num3 = result[3]
        index2 = result[0]
        index3 = result[1]
        mul = num1 * num2 * num3
        print('Index of three numbers are:{}'.format((i, index2, index3)))
        print('Three numbers are {}, and the multiplication of them is {}'.format((num1, num2, num3), mul))

try:
    num1
except:
    print('No three numbers added to 2020')
