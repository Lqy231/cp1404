item_number = int(input("number of items: "))
total_price = 0
while item_number < 0:
    print("Invalid number of items!")
    item_number = int(input("number of items: "))
for i in range(item_number):
    price = float(input("price of item: "))
    total_price += price
if total_price > 100:
    total_price *= 0.9
print("Total price for {} items is ${:.2f}".format(item_number, total_price))