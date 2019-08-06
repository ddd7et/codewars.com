#https://www.codewars.com/kata/5cab471da732b30018968071

def build_square(blocks):

	print("blocks=", blocks)
	arr = [blocks.count(1), blocks.count(2), blocks.count(3), blocks.count(4)]
	a = arr[3]
	arr[3] = 0
		
	c = arr[1]//2

	arr[1] = arr[1] - 2*(arr[1]//2)

	d = min(arr[0],arr[2]    )
	
	arr[0] = arr[0] - d  
	arr[2] = arr[2] - d

	e = min(arr[0], 2*arr[1]   )//2
	
	arr[0] = arr[0] - 2*e
	arr[1] = arr[1] - e
	print("arr=",arr)

	b = arr[0]//4
	arr[0] = arr[0] - 4*(arr[0]//4)

	if a+b+c+d+e>=4:
		return True
	else:
		return False

print(
build_square([4, 4, 3, 1, 1, 1, 2])
)