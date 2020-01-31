#Runtime: 56 ms faster than 28%
#Memory Usage: 12.8 MB less than 100%
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #nums1=merge_sort(list(set(nums1)))
        nums1=sorted(list(set(nums1)))
        nums2=sorted(list(set(nums2)))
        l1=len(nums1)
        l2=len(nums2)
        result=[]
        if l1==0 or l2==0:
            return result
        if l1<l2:
            for i in nums2:
                if i > nums1[-1]:
                    break
                elif i < nums1[0]:
                    continue
                else:   
                    a=binary_search(nums1, i) 
                    #index errors if item does not exist try: nums1.index(i) and append to result except: continue
                    if a>-1:
                        result.append(i)               
        else:
            for i in nums1:
                if i > nums2[-1]:
                    break
                elif i < nums2[0]:
                    continue
                else:
                    a=binary_search(nums2, i)
                    if a>-1:
                        result.append(i)
        return result

def binary_search(input_list, x):
        end=len(input_list)
        st=0
        while end-st >=0:
            mid=int((end+st)/2)
            if input_list[mid]==x:
                return mid
            elif input_list[mid]<x:
                st=mid+1
            else:
                end=mid-1
        return -1
        
def merge_sort(input_list):
        l=len(input_list)
        output_list=[]
        if l<=1:
            return input_list
        else:
            mid=int(l/2)
            left_l=merge_sort(input_list[:mid])
            right_l=merge_sort(input_list[mid:])
            ll=len(left_l)
            rl=len(right_l)
            i,j=0,0
            l_elem=left_l[i]
            r_elem=right_l[j]
            while len(output_list) < (ll+rl):
                if l_elem < r_elem:
                    output_list.append(l_elem)
                    i=i+1
                    try:
                        l_elem=left_l[i]
                        continue
                    except:
                        output_list=output_list+right_l[j:]
                        break
                else:
                    output_list.append(r_elem)
                    j=j+1
                    try:
                        r_elem=right_l[j]
                        continue
                    except:
                        output_list=output_list+left_l[i:]
                        break
            return output_list