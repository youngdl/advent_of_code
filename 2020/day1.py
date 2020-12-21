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
print(sorted_list)

# Search for two number that sum to 2020
n = len(num_list)
left_index = 0
right_index = n - 1
while left_index < n:
    left_num = sorted_list[left_index]
    right_num = sorted_list[right_index]
    sum = left_num + right_num
    print('left: sorted_list[{}] --> {}'.format(left_index, left_num))
    print('right: sorted_list[{}] --> {}'.format(right_index, right_num))
    print('sum: {}'.format(sum))
    import pdb; pdb.set_trace()
    if sum == 2020:
        break
    if sum > 2020:
        right_index -= 1
    if sum < 2020:
        left_index += 1
        
print(sorted_list[left_index], sorted_list[right_index])
mul = sorted_list[left_index] * sorted_list[right_index]
print(mul)
