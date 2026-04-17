import sys
import inflect

def main():
    p = inflect.engine()
    names = get_names("Name: ")
    bid_adieu(names, p)

def get_names(prompt):
    names = []
    while True:
        try:
            names.append(input(prompt))
        except EOFError:
            if len(names) < 1:
                print()
                sys.exit("At least one name is required")
            else:
                return names

def bid_adieu(names, p):
    print()
    print("Adieu, adieu, to", p.join(names))


main()
