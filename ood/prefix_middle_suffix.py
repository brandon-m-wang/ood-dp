def appears_once(list1, list2):
    # list1 = ["a", "b", "c", "a"]
    # list2 = ["c", "a", "b", "d"]
    # => (1, 2) or (2, 3)
    blacklist1 = set()
    seen1 = {}
    
    blacklist2 = set()
    seen2 = {}
    
    ans = []
    
    for i, elem in enumerate(list1):
        if elem in seen1:
            blacklist1.add(elem)
        else:
            seen1[elem] = i
    
    for i, elem in enumerate(list2):
        if elem in seen2:
            blacklist2.add(elem)
        else:
            seen2[elem] = i
    
    for elem, idx in seen1.items():
        if elem not in blacklist1 and elem not in blacklist2:
            ans.append(idx)
    
    return ans

# Test cases
# O(n)

print(appears_once(["a", "b", "c", "a"], ["c", "a", "b", "d"]))

def prefix_middle_suffix(list1, list2):
    if len(list1) == len(list2):
        shorter = list1
        longer = list2
    else:
        shorter = min(list1, list2, key=len)
        longer = max(list1, list2, key=len)
    prefix = []
    i = 0
    while i < len(shorter):
        if list1[i] != list2[i]:
            break
        prefix.append(list1[i])
        i += 1
    suffix = []
    j = 1
    while j < len(shorter) - i:
        if list1[-j] != list2[-j]:
            break
        suffix.append(list2[-j])
        j += 1
        
    print(prefix, suffix)
    middle1 = shorter[i:len(shorter)-j + 1]
    middle2 = longer[i:len(longer)-j + 1]
    print(middle1, middle2)
    
# O(n)
    
prefix_middle_suffix(["a", "a"], ["a", "a", "a"])

list1 = ["a", "b", "c", "d"] 
list2 = ["a", "b", "f", "d"]

prefix_middle_suffix(list1, list2)
