u = [123, 546, 754, 10, 92, 398, 847, 5] #example

def swap(a, b):
	z = a
	a = b
	b = z
	return (a, b)

def bubblesort(u):
	for i in range(0,len(u)-1):
		for j in range(0,len(u)-i-1):
			if u[j] > u[j+1]:
				u[j], u[j+1] = swap(u[j], u[j+1])
 
bubblesort(u)
