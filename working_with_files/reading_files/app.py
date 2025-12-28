

def read_file():
    #open file
    file = open("authors.txt", "r")

    #read file
    #content = file.read()
    #print(content)

    #return a list (iterable) of lines from the file
    lines = file.readlines()

    for line in lines:
        print(line)

    #close file
    file.close()

    return

def main():
    read_file()
    return

if __name__ == "__main__":
    main()