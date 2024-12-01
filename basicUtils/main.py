import utilities


def main():
    print("read a integer")
    number = utilities.readInt(prompt="insert a number: ", qtyAttempts=3, onlyPositive=True)
    print(f"the number is {number}")

    print("read a float")
    number = utilities.readFloat(prompt="insert a number: ", qtyAttempts=3, onlyPositive=True)
    print(f"the number is {number}")

    print("get a file")
    file = utilities.getFile()
    print(f"the file is {file}")

    print("display a menu")
    utilities.displayMenu(title="menu", options=["option 1", "option 2", "option 3"])

if __name__ == "__main__":
    main()