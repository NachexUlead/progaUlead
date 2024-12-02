from frecuencyCounter import FrecuncyCounter

fileName = input("enter the name of the file: ")
frecuency = FrecuncyCounter(fileName)

if frecuency is not None:
    print("letter frequencies")
    for key, value in sorted(frecuency.items()):
        print(f"{key}: {value}")
else:
    print("error: file couldn't be processed")

