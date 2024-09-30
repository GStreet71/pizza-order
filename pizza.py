def main():
    size = input("What size pizza would you like? [S, M, L]: ").upper()
    if size not in ["S", "M", "L"]:
        print("Invalid selection for size.")
        return

    beef = input("Would you like to add beef topping? [Y/N]: ").upper()
    if beef not in ["Y", "N"]:
        print("Invalid selection for beef.")
        return
    beef_bool = True if beef == "Y" else False

    cheese = input("Would you like to add extra cheese? [Y/N]: ").upper()
    if cheese not in ["Y", "N"]:
        print("Invalid selection for extra cheese.")
        return
    cheese_bool = True if cheese == "Y" else False

    price = calc_size(size)
    beef_price = add_beef(beef, size)
    cheese_price = extra_cheese(cheese_bool)

    get_total(price, beef_price, cheese_price)

def calc_size(size):
    if size == "L":
        return 25
    elif size == "M":
        return 20
    else:
        return 15

def add_beef(beef, size):
    if beef == "Y":
        if size == "S":
            return 2
        else:
            return 3
    return 0

def extra_cheese(cheese_bool):
    if cheese_bool:
        return 1
    return 0

def get_total(price, beef_price, cheese_price):
    total = price + beef_price + cheese_price
    print("")
    print("*********************************************")
    print(f"        Your final bill is: ${total}.       ")
    print("*********************************************")
    print("")

print("*********************************")
print("     Welcome to Python Pizza     ")
print("*********************************")
print("")

if __name__ == "__main__":
    main()