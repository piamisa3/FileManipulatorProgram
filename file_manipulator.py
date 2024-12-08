import sys
import shutil

# Varidate
def varidate():
    print(sys.argv)
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

            duplicateContents()

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

def copyFile():
    inputpath = sys.argv[2]
    outputpath = sys.argv[3]

    with open(inputpath, 'rb') as f_input:
        with open(outputpath, 'wb') as f_outputpath:
            f_outputpath.write(f_input.read())

def duplicateContents():
    inputpath = sys.argv[2]
    count = sys.argv[3]
    count = int(count)

    with open(inputpath, 'r') as f:
        content = f.read()
    
    with open(inputpath, 'a') as f:
        for i in range(count):
            f.write(content)
            
if __name__=="__main__":
    varidate()