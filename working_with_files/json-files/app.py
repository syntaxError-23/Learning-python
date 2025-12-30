from pathlib import Path
import json

path = Path(__file__).parent / "Books.json"

Books = {
    "Books": [
        {"Book": "Gospel of John", "Covenant": "New Testament"},
        {"Book": "Gospel of Mark", "Covenant": "New Testament"},
        {"Book": "Revelation", "Covenant": "New Testament"},
        {"Book": "Genesis", "Covenant": "Old Testament"},
        {"Book": "Isaiah", "Covenant": "Old Testament"},
        {"Book": "Exodus", "Covenant": "Old Testament"}
    ]
}

def write_json():

    with path.open("w") as file:
        json.dump(Books, file, indent=2)
    return

def read_json():
    with path.open("r") as file:
        data = json.load(file)
    return data

def main():
    write_json()

    data = read_json()
    print(data)
    return


if __name__ == "__main__":
    main()