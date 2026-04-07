def main():
    groceries = get_list()
    show_groceries(groceries)

def get_list():
    grocery_list = {}
    while True:
        try:
            item = input().strip().upper()
        except EOFError:
            return grocery_list
        else:
            if item not in grocery_list:
                grocery_list[item] = 1
            else:
                grocery_list[item] += 1

def show_groceries(groceries):
    for i in sorted(groceries):
        print(groceries[i], i)

main()
