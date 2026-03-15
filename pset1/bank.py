def main():
	greet = input("Greeting: ").lower().strip()
	print(correct(greet))

def correct(g):
	if g.startswith("hello"):
		return "$0"
	elif g.startswith("h"):
		return "$20"
	else:
		return "$100"
		
main()
