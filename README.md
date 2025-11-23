# Dry-Fruit-Ordering-System
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Dry Fruits Order Program</title>
    <style>
        body {
            background: black;
            color: white;
            font-family: Arial;
            padding: 30px;
            line-height: 1.6;
        }

        h1 {
            color: white;
            margin-bottom: 10px;
        }

        h2 {
            color: white;
            margin-top: 25px;
            margin-bottom: 10px;
        }

        p {
            margin-bottom: 12px;
        }

        .product-list {
            background: #222;
            padding: 15px;
            margin: 15px 0;
        }

        code {
            background: #222;
            padding: 10px;
            display: block;
            margin: 10px 0;
        }

        .note {
            background: #222;
            padding: 15px;
            margin: 15px 0;
        }
    </style>
</head>
<body>
    <h1>Dry Fruits Ordering System</h1>
    <p>Hi! I made this simple program for my project. It's a basic ordering system for dry fruits.</p>

    <h2>What it does</h2>
    <p>You can see different dry fruits, pick what you want, and place an order. The program shows you the menu, you choose items, and it calculates the total.</p>

    <h2>The Products</h2>
    <p>Here are all the products available:</p>
    <div class="product-list">
        <p>1. Cashew - Rs. 799 per kg</p>
        <p>2. Masala Kaju - Rs. 1299 per kg</p>
        <p>3. Peri Peri Cashew - Rs. 1399 per kg</p>
        <p>4. Chocolate Cashew - Rs. 1599 per kg</p>
        <p>5. Black Pepper Cashew - Rs. 1199 per kg</p>
        <p>6. Salted Cashew - Rs. 999 per kg</p>
        <p>7. California Almond - Rs. 799 per kg</p>
        <p>8. Chocolate Almond - Rs. 1599 per kg</p>
        <p>9. Pista - Rs. 1499 per kg</p>
        <p>10. Salted Pista - Rs. 1799 per kg</p>
        <p>11. Cranberry - Rs. 1999 per kg</p>
    </div>

    <h2>How to run it</h2>
    <p>You need Python on your computer. Then just open terminal and type:</p>
    <code>python dryfruits_order.py</code>
    <p>Press Enter and it will start.</p>

    <h2>How to use</h2>
    <p><strong>Step 1:</strong> Program starts and shows all products with prices</p>
    <p><strong>Step 2:</strong> Enter a number (1-11) to pick a product</p>
    <p><strong>Step 3:</strong> Choose how much you want:</p>
    <div class="note">
        <p>Type 1 for 250 grams</p>
        <p>Type 2 for 500 grams</p>
        <p>Type 3 for 750 grams</p>
        <p>Type 4 for 1 kilogram</p>
    </div>
    <p><strong>Step 4:</strong> Item gets added to your cart and you can see what's in it</p>
    <p><strong>Step 5:</strong> You can keep adding more items or type 0 when you're done shopping</p>
    <p><strong>Step 6:</strong> Program shows your complete bill with total amount</p>
    <p><strong>Step 7:</strong> Type yes to confirm your order or no to cancel</p>

    <h2>Example of how it works</h2>
    <code>Enter product number (or 0 to checkout): 1

You selected: Cashew

1. 250 grams
2. 500 grams
3. 750 grams
4. 1 kilogram

Enter quantity choice (1-4): 2

Added to cart: Cashew - 0.5kg - Rs.399.50
Press Enter to continue.</code>

    <h2>Features</h2>
    <p>- Shows menu with all products and prices</p>
    <p>- You can add multiple items to cart</p>
    <p>- Shows your cart after each item</p>
    <p>- Calculates total price automatically</p>
    <p>- Let you confirm before placing order</p>
    <p>- Simple interface, easy to understand</p>

    <h2>Problems I faced while making this</h2>
    <p>At first I tried making it really complicated with lots of functions and stuff. But then I realized that keeping it simple is better. My code was getting messy so I cleaned it up.</p>
    <p>I also had some trouble with the price calculations. Like converting kg to grams and all. But I figured it out by doing weight times price per kg.</p>
    <p>Another thing was handling wrong inputs. Like what if someone types a letter instead of number? So I added try-except to catch those errors.</p>

    <h2>What I learned from this project</h2>
    <p>This was my first proper Python project so I learned a lot:</p>
    <p>- How to use dictionaries to store product data</p>
    <p>- How to make loops that keep running until user wants to stop</p>
    <p>- How to handle user input properly</p>
    <p>- How to calculate things and format numbers (like showing 2 decimal places)</p>
    <p>- How to clear screen to make it look cleaner</p>
    <p>- Basic error handling so program doesn't crash</p>
    <p>It was challenging but fun. I understand Python much better now.</p>

    <h2>Things I want to add later</h2>
    <p>If I get more time, I want to improve this:</p>
    <p>- Save orders to a text file so they don't disappear</p>
    <p>- Ask for customer name and phone number</p>
    <p>- Show order history of previous orders</p>
    <p>- Add more products maybe</p>
    <p>- Make it look nicer with colors maybe</p>
    <p>- Add a way to remove items from cart</p>
    <p>These are just ideas. Right now it does the basic job which is good enough.</p>

    <h2>Important Note</h2>
    <div class="note">
        <p>This is my college project. It's simple and basic. I know it's not perfect and there are better ways to do things. But I made it work and learned a lot while doing it. That was the main goal.</p>
    </div>

    <h2>What you need to run this</h2>
    <p>- Python 3 (any version should work)</p>
    <p>- A computer (Windows, Mac, or Linux doesn't matter)</p>
    <p>- Terminal or command prompt</p>
    <p>That's all. No need to install any extra libraries or packages.</p>

    <h2>If something goes wrong</h2>
    <p>If program doesn't start, make sure Python is installed. Type this to check:</p>
    <code>python --version</code>
    <p>If you see errors while running, just restart the program. Most problems get fixed that way.</p>
    <p>If you type wrong input, program will tell you and ask again. Just follow what it says.</p>

    <h2>Final thoughts</h2>
    <p>I'm happy with how this turned out. It's simple but it works. I learned a lot making this and that's what matters. If you're a student like me, you can use this for reference or modify it for your own project.</p>

    <h2>Contact</h2>
    <p>If you have questions or find any bugs feel free to reach out.</p>

    <p style="margin-top: 40px; color: #666;">
        Made by Jidnyesh Pujari <br>
    
    </p>
</body>
</html>
