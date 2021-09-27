def solucion(N):
    aux = N
    result = []
    while aux >= 1:
        result = [aux % 2] + result
        aux = aux // 2
    count = 0
    max_binary_gap = 0 
    for binary_num in result:
	if binary_num == 1:
	    if count >= max_binary_gap:
		    max_binary_gap = count
		count = 0
	    if binary_num == 0:
		count += 1
    return max_binary_gap			
	
	
num = input("get binary gap from: ")
print(solucion(num))
		
