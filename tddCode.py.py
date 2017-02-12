def nextBiggerNum(input):
	if input == 1:
		return False
	nums= list(str(input))
	print(input, nums)
	i=len(nums)-1
	while(i>0):
		if int(nums[i]) > int(nums[i-1]):
			nums[i],nums[i-1]= nums[i-1]+nums[i]
			nums="".join(nums)
			return int(nums)
		i=i-1
	return False
def Test1():
	input=1
	expceted=False
	result= nextBiggerNum(input)
	return ('result : {0} and {1}'.format(expceted, result),result==expceted)
def Test2():
	input= 12
	expceted= 21
	result=nextBiggerNum(input)	
	return ('result : {0} and {1}'.format(expceted, result),result==expceted)
def Test3():
	input=21
	expceted=False
	result= nextBiggerNum(input)
	return ('result : {0} and {1}'.format(expceted, result),result==expceted)
def Test4():
	input=345
	expceted=354
	result= nextBiggerNum(input)
	return ('result : {0} and {1}'.format(expceted, result),result==expceted)
print("test1 result:",Test1())	

print("test2 result:",Test2())	

print("test3 result:",Test3())	

print("test4 result:",Test4())