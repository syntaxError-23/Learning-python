

books = ["Matthew", "Mark", "Luke", "John", "Acts", "Romans", "Ephesians", "Galatians", "1 Corinthians", "2 Corinthians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation" ]

def write_books_to_file(filename):
    #open file
    file = open(filename, "w")
    #write to file

    for book in books:
        file.write(book + "\n")

    #close file
    file.close()

def main():
    write_books_to_file("Books.txt")
    return

if __name__ == "__main__":
    main()