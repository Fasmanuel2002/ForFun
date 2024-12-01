import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # For displaying images

# Shampoo and Conditioner dictionaries with prices
shampoo = {
    "Pantene 1L": 10,
    "Pantene 0.5L": 5,
    "Pantene 0.25L": 3,
    "Loreal 1L": 12,
    "Loreal 0.5L": 5,
    "Loreal 0.25L": 3.5,
    "Head & Shoulders 1L": 15,
    "Head & Shoulders 0.5L": 5,
    "Head & Shoulders 0.25L": 3.5,
}

conditioners = {
    "Moroccanoil Hydrating Conditioner 0.5L": 54,
    "Moroccanoil Hydrating Conditioner 0.25L": 28,
    "Pantene Pro-V Smooth & Sleek Conditioner 0.5L": 12,
    "Pantene Pro-V Smooth & Sleek Conditioner 0.25L": 8,
    "TRESemmé Moisture Rich Conditioner 0.5L": 10,
    "TRESemmé Moisture Rich Conditioner 0.25L": 6,
}

# Function to handle shampoo selection
def select_shampoo(item):
    price = shampoo[item]
    messagebox.showinfo("Selected Shampoo", f"You selected {item}.\nPrice: ${price:.2f}")

# Function to handle conditioner selection
def select_conditioner(item):
    price = conditioners[item]
    messagebox.showinfo("Selected Conditioner", f"You selected {item}.\nPrice: ${price:.2f}")

# Function to create a product grid (shampoos or conditioners)
def create_product_grid(root, products, callback):
    row, col = 0,0
    for item, img_path in products.items():
        img = ImageTk.PhotoImage(Image.open(img_path).resize((100,100)))
        frame = tk.Frame(root, padx=20, pady=20)
        frame.grid(row=row, column=col)
        btn = tk.Button(frame, image=img, command=lambda i=item: callback(i))
        btn.image = img
        btn.pack()
        label = tk.Label(frame, text=item, font=("Arial",10))
        label.pack()
        
        col += 1
        if col > 2:
            col = 0
            row +=1
        
        
    

def main():
    # Initialize the main window
    root = tk.Tk()
    root.title("Machine Selector (Shampoo | Conditioner)")

    # Selection function
    def show_products(category):
        for widget in root.winfo_children():
            widget.destroy()  # Clear existing widgets

        if category == "Shampoo":
            products = {
                "Pantene 1L": "Pantene1L.png",
                "Pantene 0.5L": "Pantene500.png",
                "Pantene 0.25L": "Pantene250.png",
                "Loreal 1L": "loreal1L.png",
                "Loreal 0.5L": "loreal500.png",
                "Loreal 0.25L": "loreal250.png",
                "Head & Shoulders 1L": "Head&Shoulders1L.png",
                "Head & Shoulders 0.5L": "Head&Shoulders050.png",
                "Head & Shoulders 0.25L": "Head&Shoulders250.png",
            }
            create_product_grid(root, products, select_shampoo)
        elif category == "Conditioner":
            products = {
                "Moroccanoil Hydrating Conditioner 0.5L": "Moroccanoil500.png",
                "Moroccanoil Hydrating Conditioner 0.25L": "Moroccanoil250.png",
                "Pantene Pro-V Smooth & Sleek Conditioner 0.5L": "PanteneSmooth500.png",
                "Pantene Pro-V Smooth & Sleek Conditioner 0.25L": "PanteneSmooth250.png",
                "TRESemmé Moisture Rich Conditioner 0.5L": "Tresemme500.png",
                "TRESemmé Moisture Rich Conditioner 0.25L": "Tresemme250.png",
            }
            create_product_grid(root, products, select_conditioner)

    # Main menu buttons
    tk.Button(root, text="Shampoo", font=("Arial", 16), command=lambda: show_products("Shampoo")).pack(pady=10)
    tk.Button(root, text="Conditioner", font=("Arial", 16), command=lambda: show_products("Conditioner")).pack(pady=10)

    # Run the main loop
    root.mainloop()

# Run the program
main()
