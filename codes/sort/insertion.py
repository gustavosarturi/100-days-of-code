def swap(a, b):
	z = a
	a = b
	b = z
	return (a,b)

def insertion(x):
	for i in range(1, len(x)):
		key = u[i]
		j = i - 1
		while (j >= 0 and u[j] > key):
			u[j], u[j+1] = swap(u[j], u[j+1])
			j = j - 1
	
	return u

insertion(u)

	
