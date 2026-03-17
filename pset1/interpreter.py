def main():
	expression = input("Expression: ")
	x, y, z = expression.split(" ")
	x, z = int(x), int(z)
	result = calculate(x, y, z)
	print(f"{result:.1f}")
	
	
def calculate(n1, op, n2):
	if op == "+":
		return n1 + n2
	elif op == "-":
		return n1 - n2
	elif op == "*":
		return n1 * n2
	else:
		return n1 / n2
		
main()
