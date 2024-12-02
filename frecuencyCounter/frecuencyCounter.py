def FrecuncyCounter(fileName):
    try:
        file = open(fileName)
        text = file.read()
        return {char: text.count(char) for char in text}
    except Exception as error:
        print(f"error: file couldn't be processed: {fileName} ,{error}")
        return None