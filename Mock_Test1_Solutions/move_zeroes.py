index=0
for i in range(0,len(nums)):
  if(nums[i]!=0):
    nums[index]=nums[i]
    index+=1
while(index<len(nums)):
  nums[index]=0
  index+=1
