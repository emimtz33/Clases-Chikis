from enum import Enum

class Items(Enum):
    Apple = 27
    Milk = 20
    Eggs = 46
    Cheese = 119
    Bread = 200
    Water = 10

cart = []
itemSelected = ""
totalValue = 0

print("Welcome to the shop! \n Here are the list of items with the price of each")

for item in Items:
    print(item.name , item.value)

print("What would you like to shop?\n")

while True:
    itemSelected = str(input("Enter the item you wish to purchase, or type 'done' to exit (Beware of capital letters)\n"))

    if itemSelected.lower() == "done":
        break

    if itemSelected in Items.__members__:
        selectedItem = Items[itemSelected]
        cart.append(selectedItem)
        totalValue += selectedItem.value
        print("Added ", selectedItem.name, ", total value right now is: ", totalValue)
    else:
        print("This item: ", itemSelected.upper(),  "doesn't exit, please select a valid item or write the item correctly")

print("Checkout complete!")
print("Items in cart:")
for item in cart:
    print(item.name , item.value)

print("Your total comes out to: ", totalValue)
if input("Pay? Yes/No\n").lower() == "yes":
    print("Card declined. Please get out of my store")
else:
    print("I'm calling the cops")