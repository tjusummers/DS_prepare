# Some basic sorting logic

# %%
# Bubble sorting algorithm
def bubble(src_list):
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for i in range(len(src_list) - 1):
            if src_list[i] > src_list[i+1]:
                src_list[i], src_list[i+1] = src_list[i+1], src_list[i]
                is_swapped = True

#add test cases
test1 = [1,2,4,3]
test2 = [4,3,2,1]
test3 = [1,2,3,4]
bubble(test1)
print(f'the sorted list result is {test1}')
bubble(test2)
print(f'the sorted list result is {test2}')
bubble(test3)
print(f'the sorted list result is {test3}')

# %%
# merge sort

def merge(list1, list2):
    i = 0
    j = 0
    result = []
    while (i < len(list1)) & (j < len(list2)):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    
    if i < len(list1):
        result.extend(list1[i:])
    else:
        result.extend(list2[j:])
    
    return result

def merge_sort(src_list):
    if len(src_list) <= 1:
        return src_list
    
    #divide the list
    pivot = len(src_list)//2
    left_list = merge_sort(src_list[:pivot])
    right_list = merge_sort(src_list[pivot:])
    return merge(left_list, right_list)


test1 = [1,3,4]
test2 = [2,5,6]
try1 = merge(test1,test2)
print(try1)
test3 = [4,5,3,2,1,7,89,9]
try2 = merge_sort(test3)
print(try2)

# %%
