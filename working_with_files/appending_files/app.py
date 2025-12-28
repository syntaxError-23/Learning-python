
def read_file(read_file):
    file = open(read_file, "r")

    books = file.readlines()

    file.close()

    return books

def append_file(append_file, content_list):

    file = open(append_file, 'a')

    file.write("\n")

    for item in content_list:
        file.write(item)

    file.close()

def main():
    append_file("../writing_files/Books.txt", read_file("old_books.txt") )
    return

if __name__ == "__main__":
    main()