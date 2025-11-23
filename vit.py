import os
import time

# Product catalog with prices per kg
products = {
    1: {"name": "Cashew", "price_per_kg": 799},
    2: {"name": "Masala Kaju", "price_per_kg": 1299},
    3: {"name": "Peri Peri Cashew", "price_per_kg": 1399},
    4: {"name": "Chocolate Cashew", "price_per_kg": 1599},
    5: {"name": "Black Pepper Cashew", "price_per_kg": 1199},
    6: {"name": "Salted Cashew", "price_per_kg": 999},
    7: {"name": "California Almond", "price_per_kg": 799},
    8: {"name": "Chocolate Almond", "price_per_kg": 1599},
    9: {"name": "Pista", "price_per_kg": 1499},
    10: {"name": "Salted Pista", "price_per_kg": 1799}, 
    11: {"name": "Cranberry", "price_per_kg": 1999}
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to continue...")

def show_menu():
    clear()
    print("\n" + "="*65)
    print("             WELCOME TO DRY FRUITS STORE")
    print("="*65)
    print("\nOur Products:")
    print("-"*65)
    print(f"{'No.':<6} {'Product Name':<28} {'Per Kg':<15} {'Per 250g':<15}")
    print("-"*65)
    
    for num, item in products.items():
        price_250g = item['price_per_kg'] / 4
        print(f"{num:<6} {item['name']:<28} Rs.{item['price_per_kg']:<12} Rs.{price_250g:<12.2f}")
    
    print("-"*65)

def display_cart(cart):
    if not cart:
        return
    
    print("\n" + "-"*65)
    print("Your Cart:")
    print("-"*65)
    
    for i, item in enumerate(cart, 1):
        print(f"{i}. {item['product']:<25} {item['weight_kg']}kg - Rs.{item['price']:.2f}")
    
    total = sum(item['price'] for item in cart)
    print("-"*65)
    print(f"Total Items: {len(cart)}")
    print(f"Cart Total: Rs.{total:.2f}")
    print("-"*65)

def select_quantity(product_name, price_per_kg):
    while True:
        print(f"\nYou selected: {product_name}")
        print("\nHow much would you like?")
        print("1. 250 grams")
        print("2. 500 grams")
        print("3. 750 grams")
        print("4. 1 kilogram")
        print("5. Enter custom amount")
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                packs = 1
            elif choice == '2':
                packs = 2
            elif choice == '3':
                packs = 3
            elif choice == '4':
                packs = 4
            elif choice == '5':
                packs = int(input("How many 250g packs? "))
                if packs <= 0:
                    print("Please enter a valid number.")
                    time.sleep(1)
                    continue
            else:
                print("Invalid choice. Please try again.")
                time.sleep(1)
                continue
            
            weight = packs * 0.25
            price = price_per_kg * weight
            
            print(f"\nQuantity: {weight}kg ({packs} packs of 250g)")
            print(f"Price: Rs.{price:.2f}")
            
            return packs, weight, price
            
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(1)

def shopping():
    cart = []
    
    while True:
        show_menu()
        display_cart(cart)
        
        print("\nWhat would you like to do?")
        print("Enter product number to add to cart")
        print("Enter 0 when you're ready to checkout")
        
        try:
            choice = input("\nYour choice: ").strip()
            
            if choice == '0':
                if not cart:
                    print("\nYour cart is empty. Please add some items first.")
                    pause()
                    continue
                break
            
            choice = int(choice)
            
            if choice not in products:
                print("Sorry, that's not a valid product number.")
                pause()
                continue
            
            product = products[choice]
            packs, weight, price = select_quantity(product['name'], product['price_per_kg'])
            
            cart.append({
                'product': product['name'],
                'packs': packs,
                'weight_kg': weight,
                'price': price
            })
            
            print(f"\nGreat! {product['name']} has been added to your cart.")
            time.sleep(1.5)
            
        except ValueError:
            print("Please enter a valid number.")
            pause()
    
    return cart

def show_bill(cart):
    clear()
    print("\n" + "="*65)
    print("                    YOUR ORDER SUMMARY")
    print("="*65)
    print(f"\n{'Product':<30} {'Quantity':<15} {'Price':<15}")
    print("-"*65)
    
    total = 0
    for item in cart:
        print(f"{item['product']:<30} {item['weight_kg']}kg{'':<11} Rs.{item['price']:<12.2f}")
        total += item['price']
    
    print("-"*65)
    print(f"{'Total Amount:':<45} Rs.{total:.2f}")
    print("="*65)
    
    return total

def main():
    while True:
        clear()
        print("\n" + "="*65)
        print("             WELCOME TO DRY FRUITS STORE")
        print("="*65)
        print("\nWhat would you like to do today?")
        print("\n1. Browse products and place an order")
        print("2. Exit")
        
        choice = input("\nPlease enter your choice (1 or 2): ").strip()
        
        if choice == '1':
            cart = shopping()
            
            if cart:
                total = show_bill(cart)
                
                print("\nWould you like to confirm this order?")
                print("1. Yes, place my order")
                print("2. No, cancel")
                
                confirm = input("\nYour choice: ").strip()
                
                if confirm == '1':
                    clear()
                    print("\n" + "="*65)
                    print("                 ORDER CONFIRMED!")
                    print("="*65)
                    print(f"\nOrder Total: Rs.{total:.2f}")
                    print("\nThank you for your order!")
                    print("Your order will be delivered soon.")
                    print("\nHave a great day!")
                    print("="*65)
                    pause()
                else:
                    print("\nOrder cancelled. No problem!")
                    pause()
        
        elif choice == '2':
            clear()
            print("\n" + "="*65)
            print("Thank you for visiting!")
            print("We hope to see you again soon.")
            print("="*65 + "\n")
            break
        
        else:
            print("\nSorry, that's not a valid option. Please choose 1 or 2.")
            pause()

if __name__ == "__main__":
    main()
