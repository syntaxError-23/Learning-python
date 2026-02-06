from pathlib import Path
from decimal import Decimal, InvalidOperation
import csv

# -------------------- Main Program Function --------------------

def serve_user():
    
    customer_order = []

    while True:
        item_name = input("Enter the item name (or 'q' to quit): ")

        if item_name.lower() == 'q':
            break

        try:
            item_price = Decimal(input("Enter the item's price: "))
        except (ValueError, InvalidOperation):
            print("Invalid Entry. Please enter a number")
            continue
        
        customer_order.append((item_name, item_price))

    return customer_order

# -------------------- Totals calculator function --------------------

def calc_totals(order):
    
    total = Decimal(sum(item[1] for item in order))

    while True:
        try:
            tip_percentage = int(input("\nHow much would you like to tip (percentage): "))
            break
        except ValueError:
            print("Invalid entry. Please enter an integer")
    
    grand_total = total * (Decimal(1) + tip_percentage/Decimal(100))

    print(f"\nTotal: {total:.2f}")
    print(f"Tip: £{total * tip_percentage/Decimal(100):.2f} ({tip_percentage}%)" )
    print(f"Grand Total: {grand_total:.2f}")

    total_str = ("Total", total)
    tip_str = ("Tip", total*tip_percentage/Decimal(100))
    grand_total_str = ("Grand Total", grand_total)

    return [total_str, tip_str, grand_total_str]
# -------------------- CSV Writer function --------------------

def create_csv(path, items, totals):
    with path.open("w", newline = '') as file:
        writer = csv.writer(file)

        writer.writerow(["Item name", "Cost"])
        writer.writerows(items)
        writer.writerow('')
        writer.writerows(totals)

# -------------------- Main Program Function --------------------

def main():

    #get table number from user

    while True:
        try:
            table_num = int(input("Enter the table number: "))
            print(f"Starting tab for table {table_num}\n")
            break
        except ValueError:
            print("Invalid input. Please enter a number")

    #create file path using table number

    path = Path(__file__).parent / f"table_{table_num}.csv"

    #get items from user (item name and price)

    cust_order = serve_user() 

    if not cust_order:
        print("No items were ordered...")
        return

    print("")
    for name, price in cust_order:
       
        print(f"{name}: £{price:.2f}")
        
    #calculate totals (total tip grand total)

    totals = calc_totals(cust_order)

    create_csv(path, cust_order, totals)

    #create the csv 
    return

if __name__ == "__main__":
    main()