# Dry Fruits Ordering System

Hi! I made this simple program for my project. It's a basic ordering system for dry fruits.

## What it does

You can see different dry fruits, pick what you want, and place an order. The program shows you the menu, you choose items, and it calculates the total.

## The Products

Here are all the products available:

1. Cashew - Rs. 799 per kg
2. Masala Kaju - Rs. 1299 per kg
3. Peri Peri Cashew - Rs. 1399 per kg
4. Chocolate Cashew - Rs. 1599 per kg
5. Black Pepper Cashew - Rs. 1199 per kg
6. Salted Cashew - Rs. 999 per kg
7. California Almond - Rs. 799 per kg
8. Chocolate Almond - Rs. 1599 per kg
9. Pista - Rs. 1499 per kg
10. Salted Pista - Rs. 1799 per kg
11. Cranberry - Rs. 1999 per kg

## How to run it

You need Python on your computer. Then just open terminal and type:

```bash
python dryfruits_order.py
```

Press Enter and it will start.

## How to use

**Step 1:** Program starts and shows all products with prices

**Step 2:** Enter a number (1-11) to pick a product

**Step 3:** Choose how much you want:
- Type 1 for 250 grams
- Type 2 for 500 grams
- Type 3 for 750 grams
- Type 4 for 1 kilogram

**Step 4:** Item gets added to your cart and you can see what's in it

**Step 5:** You can keep adding more items or type 0 when you're done shopping

**Step 6:** Program shows your complete bill with total amount

**Step 7:** Type yes to confirm your order or no to cancel

## Example of how it works

```
Enter product number (or 0 to checkout): 1

You selected: Cashew

1. 250 grams
2. 500 grams
3. 750 grams
4. 1 kilogram

Enter quantity choice (1-4): 2

Added to cart: Cashew - 0.5kg - Rs.399.50
Press Enter to continue...
```

## Features

- Shows menu with all products and prices
- You can add multiple items to cart
- Shows your cart after each item
- Calculates total price automatically
- Let you confirm before placing order
- Simple interface, easy to understand

## Problems I faced while making this

At first I tried making it really complicated with lots of functions and stuff. But then I realized that keeping it simple is better. My code was getting messy so I cleaned it up.

I also had some trouble with the price calculations. Like converting kg to grams and all. But I figured it out by doing weight times price per kg.

Another thing was handling wrong inputs. Like what if someone types a letter instead of number? So I added try-except to catch those errors.

## What I learned from this project

This was my first proper Python project so I learned a lot:

- How to use dictionaries to store product data
- How to make loops that keep running until user wants to stop
- How to handle user input properly
- How to calculate things and format numbers (like showing 2 decimal places)
- How to clear screen to make it look cleaner
- Basic error handling so program doesn't crash

It was challenging but fun. I understand Python much better now.

## Things I want to add later

If I get more time, I want to improve this:

- Save orders to a text file so they don't disappear
- Ask for customer name and phone number
- Show order history of previous orders
- Add more products maybe
- Make it look nicer with colors maybe
- Add a way to remove items from cart

These are just ideas. Right now it does the basic job which is good enough.

## Important Note

This is my college project. It's simple and basic. I know it's not perfect and there are better ways to do things. But I made it work and learned a lot while doing it. That was the main goal.

## What you need to run this

- Python 3 (any version should work)
- A computer (Windows, Mac, or Linux doesn't matter)
- Terminal or command prompt

That's all. No need to install any extra libraries or packages.

## If something goes wrong

If program doesn't start, make sure Python is installed. Type this to check:

```bash
python --version
```

If you see errors while running, just restart the program. Most problems get fixed that way.

If you type wrong input, program will tell you and ask again. Just follow what it says.

## Final thoughts

I'm happy with how this turned out. It's simple but it works. I learned a lot making this and that's what matters. If you're a student like me, you can use this for reference or modify it for your own project.

## Contact

If you have questions or find any bugs, feel free to reach out.

---

Made by a fresher student learning Python  
Created for college project - 2024
