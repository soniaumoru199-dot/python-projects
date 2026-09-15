print("🍦 Ice Cream Order Maker")

flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint"]

print("\nAvailable flavors:")
for flavor in flavors:
    print("-", flavor)

choice = input("\nChoose a flavor: ").strip().title()
scoops = int(input("How many scoops would you like? "))

if choice in flavors:
    print(f"\nOrder confirmed: {scoops} scoop(s) of {choice} ice cream! 🍦")
else:
    print("\nSorry, that flavor is not available.")
