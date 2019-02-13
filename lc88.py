'''
there must be something wrong with the system!!!!!!
'''
def merge(nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
    print(nums1)
    print(nums2)
    if m == 0:
        for i in range(n):
            nums1[i] = nums2[i]
    elif n != 0:
        index1 = m-1
        index2 = n-1
        index = m+n-1
        while(index1 >= 0 and index2 >= 0):
            if(nums2[index2] > nums1[index1]):
                nums1[index] = nums2[index2]
                index2 -= 1
                index -= 1
            else:
                nums1[index] = nums1[index1]
                index1 -= 1
                index -= 1
        print(index1)
    print(nums1)

merge([2,0], 1, [1], 1)        
        