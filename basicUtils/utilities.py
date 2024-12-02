def readInt(prompt="insert a number: ", qtyAttempts=None, onlyPositive=False):
    attempts = 0
    while qtyAttempts is None or attempts < qtyAttempts:
        try: 
            user = input(prompt)
            number = int(user)

            if onlyPositive and number < 0:
                print("error: number must be positive")
                attempts += 1
                continue

            return number
        except ValueError:
            print("error: number must be an integer")
            attempts += 1
    
    print("error: too many attempts")
    exit(1)


def readFloat(prompt="insert a number: ", qtyAttempts=None, onlyPositive=False):
    attempts = 0
    while qtyAttempts is None or attempts < qtyAttempts:
        try: 
            user = input(prompt)
            number = float(user)

            if onlyPositive and number < 0:
                print("error: number must be positive")
                attempts += 1
                continue

            return number
        except ValueError:
            print("error: number must be a float")
            attempts += 1
    
    print("error: too many attempts")
    exit(1)

def getFile():
    file_path = input("enter the file path: ")
    try:
        return open(file_path, "r")
    except FileNotFoundError:
        print("error: file not found")
        exit(1)

def displayMenu(title="menu", options=None):
    if not options:
        print("we don't have options")
        return
    
    print(title)
    print("=" * len(title))

    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    print()

