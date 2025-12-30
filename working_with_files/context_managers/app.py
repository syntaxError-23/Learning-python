from pathlib import Path

def open_file():
    path  = Path(__file__).parent / "characters.txt"

    data = ["Melchizedek", "Isiaih", "Job", "Arius", "Thomas Aquinas"]

    with path.open("w") as file:
        for character in data:
            file.write(character + "\n")

def main():
    open_file()
    return

if __name__ == "__main__":
    main()