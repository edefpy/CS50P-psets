answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").lower().replace(" ", "").replace("-", "")

match answer:
	case "42" | "fortytwo":
		print("Yes")
	case _:
		print("No")
