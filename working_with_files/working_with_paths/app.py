
from pathlib import Path

apr_list = ["Tobit", "Judith", "Esther", "Wisdom of Solomon", "Gospel of Judas", "Book of Sirach", "Baruch", "Prayer of Azariah and Song of the three holy children", "Story of Susanna", "Story of Bel and the Dragon", "Prayer of Manasseh", "1 Maccabees", "2 Maccabees", "1 Esdras", "2 Esdras"]

def create_path():
    script_dir = Path(__file__).parent 
    
    path = script_dir / "Books"

    #Makes directory
    #parents=true creates any missing directories between "Path" variable and new directory (books)
    #exist_ok mitigates error of potentially creating duplicate folder (if "Books" already exists)
    path.mkdir(parents=True, exist_ok=True) 

    path = path / "apocrypha.txt"
    
    file = path.open("a+")
    
    file.write("\nThese are some of the apocryphal texts of the bible")

    file.seek(0)

    dup_list = file.readlines()

    for item in dup_list:
        print(item)

    file.close()

def main():
    create_path()
    return

if __name__ == "__main__":
    main()