import tkinter as tk # this library for GUI

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        # check operations here 
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result_label.config(text="Division by zero is not allowed")
                return
            result = num1 / num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Enter valid numbers")

#GUI for the calculator


root = tk.Tk()
root.title("Calculator- Aya")
root.geometry("300x300")

tk.Label(root, text="Number 1:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Number 2:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

tk.Button(root, text="+", command=lambda: calculate("+"), width=5).pack(pady=5) # the function will execute when the button is clicked 
tk.Button(root, text="-", command=lambda: calculate("-"), width=5).pack(pady=5)
tk.Button(root, text="*", command=lambda: calculate("*"), width=5).pack(pady=5)
tk.Button(root, text="/", command=lambda: calculate("/"), width=5).pack(pady=5)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)


# run the main event loop
root.mainloop()