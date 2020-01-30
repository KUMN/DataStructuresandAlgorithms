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


#Time limit exceeded
def threeSum_slower(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        result=[]
        ref=[]
        for i in range(l):
            for j in range(i+1, l):
                try:
                    k = nums[j+1:].index(0-(nums[i]+nums[j]))
                    if (not (set([nums[i], nums[j], nums[k+j+1]]) in ref)):
                        result.append([nums[i], nums[j], nums[k+j+1]])
                        ref.append(set([nums[i], nums[j], nums[k+j+1]]))
                except:
                    continue
        return result



#Time limit exceeded
def threeSum2(nums):
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
            if not (set([nums[ix], x[0], x[1]]) in ref):
                result3.append([nums[ix], x[0], x[1]])
                ref.append(set([nums[ix], x[0], x[1]]))
    return result3
        
def threeSum(nums):
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

    