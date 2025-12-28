
shopping_list = []
price = 0


while True:

    item = input('Enter the item you would like to purchase. Enter "q" to quit or "l" to view the list or "d" to delete an item from the list: ')
    print('You have entered: ', item)

    def display_list():
        counter = 0
        
        if len(shopping_list) > 0: #checks to see that there are items in shopping list
            print('')
            print('SHOPPING LIST')
            print('')
            for name, item_price in shopping_list:
                print(f'{counter+1}:{name:<20} £{item_price:>8.2f}')
                counter+=1

            counter = 0
            list_total = sum(product[1] for product in shopping_list)
            print('')
            print(f'Total so far: £{list_total:.2f}')
            print('')

        else: 
            print('There are no items in the list yet...')
            

    if item.lower() == 'q': #checks if user wants to quit
        total = sum(product[1] for product in shopping_list)
        #for product in shopping_list:
         #   total = total + product[1] #calculates total amount spent in shopping list
        print(f'Your total is: £{total:.2f}')
        print('Program terminated')
        print('')
        total = 0 #resets total variable
        break
        
    elif item.lower() == 'l': #checks if user want to view shopping list 
        display_list()
        continue

    elif item.lower() == 'd':
        display_list()
        
        if len(shopping_list) == 0:
            continue

        try:
            remove_index = int(input("Enter the index of the item you would like to delete: "))
            shopping_list.pop(remove_index - 1)
            print("Item removed successfully")
        except(ValueError, IndexError):
            print("Invalid selection. No items were removed")

        continue

    try:
        price = round(float(input('Enter the price (£) of the item: ')), 2)
        print(f"You have entered: {price:.2f}")
    except ValueError as e:
        print('You have not entered a number. Please try again')
        print('Error: ',  e)
        continue
    else:
        print(f"You have entered the item - {item.upper()} - with a price - £{price:.2f} - ")


    shopping_list.append((item, price))

