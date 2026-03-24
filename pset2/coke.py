coke = 50
print(f"Amount Due: {coke}")

while coke > 0:
	pay = int(input("Insert Coin: "))
	if pay == 5 or pay == 10 or pay == 25:
		coke -= pay
		if coke > 0: 
			print(f"Amount Due: {coke}")
		else:
			print(f"Change Owed: {0 - coke}")
	else:
		print(f"Amount Due: {coke}")
