import tkinter as tk  # This library is for GUI

def calculate(operation, entry1, entry2, result_label):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

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
        print(result_label)
    except ValueError:
        result_label.config(text="Enter valid numbers")

# GUI Setup
root = tk.Tk()
root.title("Calculator- Aya")
root.geometry("300x300")

tk.Label(root, text="Number 1:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Number 2:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

tk.Button(root, text="+", command=lambda: calculate("+", entry1, entry2, result_label), width=5).pack(pady=5)
tk.Button(root, text="-", command=lambda: calculate("-", entry1, entry2, result_label), width=5).pack(pady=5)
tk.Button(root, text="*", command=lambda: calculate("*", entry1, entry2, result_label), width=5).pack(pady=5)
tk.Button(root, text="/", command=lambda: calculate("/", entry1, entry2, result_label), width=5).pack(pady=5)

root.mainloop()
