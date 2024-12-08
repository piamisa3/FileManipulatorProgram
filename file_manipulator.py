import sys

# Varidate
def varidate():
    match sys.argv[1]:
        case "reverse":
            if len(sys.argv) != 4:
                errorMessage("Incorrect number of arguments. reverse is 4")
            reverseString()

        case "copy":
            if len(sys.argv) != 4:
                errorMessage("Incorrect number of arguments. copy is 4")
                copyFile()

        case "duplicate-contents":
            if len(sys.argv) != 4:
                errorMessage("Incorrect number of arguments. duplicate-contents is 4")

        case "replace-string":
            if len(sys.argv) != 5:
                errorMessage("Incorrect number of arguments. replace-string is 5")

        case _:
            errorMessage("Incorrect of arguments")
        
def errorMessage(error_message):
    raise ValueError(f"error: {error_message}")

def reverseString():
    inputpath = sys.argv[2]
    outputpath = sys.argv[3]


    with open(inputpath) as f:
        contents = f.read()
    reverse_contents = contents[::-1]
    with open(outputpath, 'w') as f:
        f.write(reverse_contents)


if __name__=="__main__":
    varidate()