print("------ shopping bill generator------")

items = []
prices = []
quantities = []

n = int(input("enter number of items you want to buy: "))
for i in range(n):
    print(f"\nitem {i+1}")
    name=input("enter item name")
    price=float(input("enter price of the item: "))
    qty = int(input("enter quantity: "))

    items.append(name)
    prices.append(price)
    quantities.append(qty)

total = 0
for i in range(n):
    total+= prices[i] * quantities[i]

print("\n------final bill------")
for i in range(n):
    print(f"{items[i]}  X {quantities[i]} = rs {prices[i] * quantities[i]}")
print("\ntotal amount to pay: rs", total)
print("--------------------------------------------")
