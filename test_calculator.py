import pytest
import tkinter as tk
from calculator import calculate
import allure

@pytest.fixture
def tkinter_elements():
    root = tk.Tk()
    entry1 = tk.Entry(root)
    entry2 = tk.Entry(root)
    result_label = tk.Label(root)
    return entry1, entry2, result_label

@pytest.mark.parametrize("num1, num2, operation, expected", [
    ("5", "3", "+", "Result: 8.0"),
    ("5", "3", "-", "Result: 2.0"),
    ("5", "3", "*", "Result: 15.0"),
    ("5", "3", "/", "Result: 1.667"),  
    ("5", "0", "/", "Division by zero is not allowed"),
    ("a", "3", "+", "Enter valid numbers"),  
])
def test_calculate(tkinter_elements, num1, num2, operation, expected):
    entry1, entry2, result_label = tkinter_elements
    entry1.insert(0, num1)
    entry2.insert(0, num2)
    calculate(operation, entry1, entry2, result_label)

    # handle floating issues
    if operation == "/" and "Result:" in expected:
        actual_result = result_label.cget("text").split(": ")[1]
        expected_result = expected.split(": ")[1]
        assert abs(float(actual_result) - float(expected_result)) < 0.01
    else:
        assert result_label.cget("text") == expected
