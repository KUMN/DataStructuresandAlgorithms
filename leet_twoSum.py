#Runtime: 5948 ms, faster than 12.11% of Python3 online submissions for Two Sum.
#Memory Usage: 13.8 MB, less than 69.53% of Python3 online submissions for Two Sum.
def twoSum(nums, target):
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