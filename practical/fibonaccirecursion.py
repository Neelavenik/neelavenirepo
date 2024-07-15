# Fibonacci series using recursion
def fibonacci(n):
	if n <= 1:
		print(n)
		return n
	return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))
