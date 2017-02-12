def nextBiggerNum(input):
	if input == 1:
		return False
	nums= list(str(input))
	print(input, nums)
	i=len(nums)-1
	while(i>0):
		rflag=nums[i]
		lflag=nums[i-1]
		
		if rflag> lflag:
			t=lflag
			r=nums[i:]
			l=nums[0:i]
			print("T, R, L ")
			print(t,r,l)
			rlen=len(r)-1
			while (rlen>=0):
				if r[rlen]>t:
					l[i-1]=r[rlen]
					r[rlen]=t
					break
				rlen-=1

			print('before L:',l," ,r: ",r, ",min(r): ",min(r))	
			l=l+[str(min(r))]
			print('after: l= ',l)	
			return int(''.join(l))
		i-=1
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
def Test4():
	input=576
	expceted=657
	result= nextBiggerNum(input)
	return ('result : {0} and {1}'.format(expceted, result),result==expceted)
print("test1 result:",Test1())	

print("test2 result:",Test2())	

print("test3 result:",Test3())	

print("test4 result:",Test4())