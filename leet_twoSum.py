#Runtime: 5948 ms, faster than 12.11% of Python3 online submissions for Two Sum.
#Memory Usage: 13.8 MB, less than 69.53% of Python3 online submissions for Two Sum.
def twoSum2(nums, target):
  l=len(nums)
  result=None
  for i in range(l):
    for j in range(i+1,l):
      if nums[i]+nums[j] == target:
        result=[i,j]
        break

    if result:
      break
        
  return result

#Runtime: Runtime: 7328 ms faster than 5%
# Memory Usage: 14.1 MB, less than 61% of Python3 online submissions for Two Sum.
# using lambda x: x+nums[i] makes this function even more slower
def twoSum_slower(nums, target):
    def fn(i):
        return i+x
    l=len(nums)
    result=None
    for i in range(l):
        x=nums[i]
        new_nums=list(map(fn, nums[i+1:]))
        try:
            j=new_nums.index(target)
            result=[i,j+i+1]
            break
        except:
            continue
    return result

#Runtime: 860 ms faster than 22%
#Memory Usage: 13.6 MB lesser than 93%
def twoSum(nums, target):
    l=len(nums)
    result=None
    for i in range(l):
        try:
            j=nums[i+1:].index(target-nums[i])
            if i!=j:
                result=[i,j+i+1]
                break
        except:
            continue
    return result


#Brute force to linearly search the list with 2 loops and then call the index function of list
#Time limit exceeded
def threeSum_slower(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        result=[]
        ref=[]
        for i in range(l):
            for j in range(i+1, l):
                try:
                    k = nums[j+1:].index(0-(nums[i]+nums[j]))
                    if (not (set([nums[i], nums[j], nums[k+j+1]]) in ref)): #check for duplicates
                        result.append([nums[i], nums[j], nums[k+j+1]])
                        ref.append(set([nums[i], nums[j], nums[k+j+1]]))
                except:
                    continue
        return result


#Similar to above but the second loop is replaced with a function call to twoSum
#The first loop is a linear search, so is the second one within the function twoSum
#For a given number in i, call a function to pick all 2 pairs of numbers from the rest of the list that sum to 0
#While appending to the main result set check for no duplicates in the results
#Time limit exceeded
def threeSum3(nums):
    def twoSum3(nums, target):
        l=len(nums)
        result=[]
        for i in range(l):
            num_i = nums[i]
            new_nums=nums[i+1:]
            try:
                while len(new_nums)>0:
                    j=new_nums.index(target-num_i)
                    result.append([num_i, new_nums[j]])
                    new_nums=new_nums[j+1:]   
            except:
                continue
        return result

    result3=[]
    ref=[]
    l3=len(nums)
    for ix in range(l3):
        r1 = twoSum3(nums[ix+1:], 0-nums[ix])
        for x in r1:
            if not (set([nums[ix], x[0], x[1]]) in ref): #check for duplicates
                result3.append([nums[ix], x[0], x[1]])
                ref.append(set([nums[ix], x[0], x[1]]))
    return result3
        
#The list is first sorted and then there is a linear search with 2 loops and third is index call on list
#Check if the next number in loop 1 or loop2 is same as earlier one, in which case avoid the loop
#Thus no duplicates are created. There is then no need for the code to check duplicates
#The second loop is done with a function call to twoSum. Thus we have to loop through twoSum's results.
def threeSum2(nums):
    def twoSum3(nums, target):
        l=len(nums)
        result=[]
        for i in range(l):
            if i>0 and nums[i]==nums[i-1]:
                continue
            try:
                j=nums[i+1:].index(target-nums[i])
                result.append([nums[i], nums[j+i+1]])
            except:
                continue
        return result

    result3=[]
    l3=len(nums)
    nums.sort()
    for ix in range(l3):
        if ix>0 and nums[ix]==nums[ix-1]:
                continue
        r1 = twoSum3(nums[ix+1:], -nums[ix])
        for x in r1:
            result3.append([nums[ix], x[0], x[1]])

    return result3

#Sort the list.
#Linear search in 2 loops and then call index function to get the number list
#If the number is same as the prior one in the loop then skip it
#Thus duplicates are not created
#Also there is no function call to twoSum so the results from it do not need to looped through either
#Entries are made directly to the main results list

def threeSum1(self, nums: List[int]) -> List[List[int]]:
        result3=[]
        l3=len(nums)
        nums.sort()
        for ix in range(l3):
            if ix>0 and nums[ix]==nums[ix-1]:
                    continue
    
            for i in range(len(nums[ix+1:])):
                if i>0 and nums[i+ix+1]==nums[i+ix]:
                    continue
                try:
                    j=nums[i+1+ix+1:].index(-nums[ix]-nums[i+ix+1])
                    result3.append([nums[ix], nums[i+ix+1], nums[j+i+1+ix+1]])
                except:
                    continue

        return result3


#Sort the list
#Linear search with 2 loops and in the third one do a binary search for the value rather than calling index function of the list
#No functions are called so no need to loop through results to create the result set
#Entries are made directly to results
def threeSum(self, nums: List[int]) -> List[List[int]]:
    result3=[]
    l3=len(nums)
    nums.sort()
    for ix in range(l3):
        if ix>0 and nums[ix]==nums[ix-1]:
            continue
    
        for i in range(len(nums[ix+1:])):
            if i>0 and nums[i+ix+1]==nums[i+ix]:
                continue
            #j=nums[i+1+ix+1:].index(-nums[ix]-nums[i+ix+1])
            st=i+1+ix+1
            end=l3-1
            value=-nums[ix]-nums[i+ix+1]
            while end-st >=0:
                mid=int((end+st)/2)
                if nums[mid]==value:
                    result3.append([nums[ix], nums[i+ix+1], nums[mid]])
                    break
                elif value<nums[mid]:
                    end=mid-1
                else:
                    st=mid+1

    return result3
