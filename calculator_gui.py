#!/usr/bin/env python3
"""
Python Scientific Calculator - GUI Version using Tkinter
Author: Python Calculator Project
Description: A comprehensive scientific calculator with graphical interface
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math
import cmath
import sys
from typing import Union


class ScientificCalculatorGUI:
    """Scientific Calculator with Tkinter GUI."""

    def __init__(self, root):
        self.root = root
        self.root.title("Python Scientific Calculator")
        self.root.geometry("500x700")
        self.root.resizable(True, True)
        self.root.configure(bg='#2b2b2b')

        # Calculator state
        self.display_var = tk.StringVar(value="0")
        self.memory = 0.0
        self.angle_mode = "degrees"  # "degrees" or "radians"
        self.current_expression = ""
        self.should_reset_display = True
        self.history = []

        # Setup GUI
        self.setup_styles()
        self.create_widgets()
        self.setup_keyboard_bindings()

    def setup_styles(self):
        """Configure styles for the calculator."""
        style = ttk.Style()

        # Configure colors and fonts
        self.colors = {
            'bg': '#2b2b2b',
            'display_bg': '#1a1a1a',
            'display_fg': '#ffffff',
            'number_bg': '#404040',
            'number_fg': '#ffffff',
            'operator_bg': '#ff9500',
            'operator_fg': '#ffffff',
            'scientific_bg': '#505050',
            'scientific_fg': '#ffffff',
            'memory_bg': '#606060',
            'memory_fg': '#ffffff'
        }

        self.fonts = {
            'display': ('Consolas', 24, 'bold'),
            'button': ('Arial', 10, 'bold'),
            'small_button': ('Arial', 8, 'bold'),
            'status': ('Arial', 9)
        }

    def create_widgets(self):
        """Create and layout all GUI widgets."""
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Display frame
        self.create_display_frame(main_frame)

        # Status frame
        self.create_status_frame(main_frame)

        # Button frames
        self.create_memory_frame(main_frame)
        self.create_scientific_frame(main_frame)
        self.create_basic_frame(main_frame)

    def create_display_frame(self, parent):
        """Create the display area."""
        display_frame = tk.Frame(parent, bg=self.colors['bg'])
        display_frame.pack(fill=tk.X, pady=(0, 10))

        # Main display
        self.display = tk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=self.fonts['display'],
            bg=self.colors['display_bg'],
            fg=self.colors['display_fg'],
            justify='right',
            state='readonly',
            bd=0,
            relief='flat'
        )
        self.display.pack(fill=tk.X, ipady=10)

        # Expression display (smaller, shows current calculation)
        self.expression_var = tk.StringVar(value="")
        self.expression_display = tk.Label(
            display_frame,
            textvariable=self.expression_var,
            font=('Arial', 10),
            bg=self.colors['bg'],
            fg='#888888',
            anchor='e',
            height=1
        )
        self.expression_display.pack(fill=tk.X, pady=(5, 0))

    def create_status_frame(self, parent):
        """Create status information display."""
        status_frame = tk.Frame(parent, bg=self.colors['bg'])
        status_frame.pack(fill=tk.X, pady=(0, 10))

        # Left side - Angle mode and Memory
        left_status = tk.Frame(status_frame, bg=self.colors['bg'])
        left_status.pack(side=tk.LEFT)

        self.angle_label = tk.Label(
            left_status,
            text=f"Mode: {self.angle_mode.title()}",
            font=self.fonts['status'],
            bg=self.colors['bg'],
            fg='#cccccc'
        )
        self.angle_label.pack(side=tk.LEFT, padx=(0, 20))

        self.memory_label = tk.Label(
            left_status,
            text=f"M: {self.memory}",
            font=self.fonts['status'],
            bg=self.colors['bg'],
            fg='#cccccc'
        )
        self.memory_label.pack(side=tk.LEFT)

        # Right side - History button
        history_btn = tk.Button(
            status_frame,
            text="History",
            font=self.fonts['status'],
            bg=self.colors['memory_bg'],
            fg=self.colors['memory_fg'],
            command=self.show_history,
            relief='flat',
            bd=1
        )
        history_btn.pack(side=tk.RIGHT)

    def create_memory_frame(self, parent):
        """Create memory and mode buttons."""
        memory_frame = tk.Frame(parent, bg=self.colors['bg'])
        memory_frame.pack(fill=tk.X, pady=(0, 5))

        memory_buttons = [
            ("MC", self.memory_clear),
            ("MR", self.memory_recall),
            ("MS", self.memory_store),
            ("M+", self.memory_add),
            ("M-", self.memory_subtract),
            ("DEG/RAD", self.toggle_angle_mode)
        ]

        for i, (text, command) in enumerate(memory_buttons):
            btn = tk.Button(
                memory_frame,
                text=text,
                font=self.fonts['small_button'],
                bg=self.colors['memory_bg'],
                fg=self.colors['memory_fg'],
                command=command,
                relief='flat',
                bd=1,
                width=8
            )
            btn.grid(row=0, column=i, padx=1, sticky='ew')

        # Configure grid weights
        for i in range(6):
            memory_frame.grid_columnconfigure(i, weight=1)

    def create_scientific_frame(self, parent):
        """Create scientific function buttons."""
        sci_frame = tk.Frame(parent, bg=self.colors['bg'])
        sci_frame.pack(fill=tk.X, pady=(0, 5))

        # First row - Basic scientific functions
        sci_buttons_1 = [
            ("sin", lambda: self.scientific_function("sin")),
            ("cos", lambda: self.scientific_function("cos")),
            ("tan", lambda: self.scientific_function("tan")),
            ("ln", lambda: self.scientific_function("ln")),
            ("log", lambda: self.scientific_function("log")),
            ("!", lambda: self.scientific_function("factorial"))
        ]

        for i, (text, command) in enumerate(sci_buttons_1):
            btn = tk.Button(
                sci_frame,
                text=text,
                font=self.fonts['button'],
                bg=self.colors['scientific_bg'],
                fg=self.colors['scientific_fg'],
                command=command,
                relief='flat',
                bd=1,
                width=6
            )
            btn.grid(row=0, column=i, padx=1, pady=1, sticky='ew')

        # Second row - More scientific functions
        sci_buttons_2 = [
            ("asin", lambda: self.scientific_function("asin")),
            ("acos", lambda: self.scientific_function("acos")),
            ("atan", lambda: self.scientific_function("atan")),
            ("e^x", lambda: self.scientific_function("exp")),
            ("x²", lambda: self.scientific_function("square")),
            ("x³", lambda: self.scientific_function("cube"))
        ]

        for i, (text, command) in enumerate(sci_buttons_2):
            btn = tk.Button(
                sci_frame,
                text=text,
                font=self.fonts['button'],
                bg=self.colors['scientific_bg'],
                fg=self.colors['scientific_fg'],
                command=command,
                relief='flat',
                bd=1,
                width=6
            )
            btn.grid(row=1, column=i, padx=1, pady=1, sticky='ew')

        # Third row - Constants and more functions
        sci_buttons_3 = [
            ("π", lambda: self.insert_constant("pi")),
            ("e", lambda: self.insert_constant("e")),
            ("√", lambda: self.scientific_function("sqrt")),
            ("∛", lambda: self.scientific_function("cbrt")),
            ("x^y", lambda: self.insert_operator("**")),
            ("1/x", lambda: self.scientific_function("reciprocal"))
        ]

        for i, (text, command) in enumerate(sci_buttons_3):
            btn = tk.Button(
                sci_frame,
                text=text,
                font=self.fonts['button'],
                bg=self.colors['scientific_bg'],
                fg=self.colors['scientific_fg'],
                command=command,
                relief='flat',
                bd=1,
                width=6
            )
            btn.grid(row=2, column=i, padx=1, pady=1, sticky='ew')

        # Configure grid weights
        for i in range(6):
            sci_frame.grid_columnconfigure(i, weight=1)

    def create_basic_frame(self, parent):
        """Create basic calculator buttons."""
        basic_frame = tk.Frame(parent, bg=self.colors['bg'])
        basic_frame.pack(fill=tk.BOTH, expand=True)

        # Button layout: [text, row, col, command, color_type]
        buttons = [
            ("C", 0, 0, self.clear_all, "operator"),
            ("CE", 0, 1, self.clear_entry, "operator"),
            ("⌫", 0, 2, self.backspace, "operator"),
            ("÷", 0, 3, lambda: self.insert_operator("/"), "operator"),

            ("7", 1, 0, lambda: self.insert_digit("7"), "number"),
            ("8", 1, 1, lambda: self.insert_digit("8"), "number"),
            ("9", 1, 2, lambda: self.insert_digit("9"), "number"),
            ("×", 1, 3, lambda: self.insert_operator("*"), "operator"),

            ("4", 2, 0, lambda: self.insert_digit("4"), "number"),
            ("5", 2, 1, lambda: self.insert_digit("5"), "number"),
            ("6", 2, 2, lambda: self.insert_digit("6"), "number"),
            ("−", 2, 3, lambda: self.insert_operator("-"), "operator"),

            ("1", 3, 0, lambda: self.insert_digit("1"), "number"),
            ("2", 3, 1, lambda: self.insert_digit("2"), "number"),
            ("3", 3, 2, lambda: self.insert_digit("3"), "number"),
            ("+", 3, 3, lambda: self.insert_operator("+"), "operator"),

            ("±", 4, 0, self.toggle_sign, "number"),
            ("0", 4, 1, lambda: self.insert_digit("0"), "number"),
            (".", 4, 2, lambda: self.insert_digit("."), "number"),
            ("=", 4, 3, self.calculate, "operator")
        ]

        for text, row, col, command, color_type in buttons:
            if color_type == "number":
                bg_color = self.colors['number_bg']
                fg_color = self.colors['number_fg']
            else:  # operator
                bg_color = self.colors['operator_bg']
                fg_color = self.colors['operator_fg']

            btn = tk.Button(
                basic_frame,
                text=text,
                font=self.fonts['button'],
                bg=bg_color,
                fg=fg_color,
                command=command,
                relief='flat',
                bd=1
            )
            btn.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')

        # Configure grid weights for responsive layout
        for i in range(5):
            basic_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            basic_frame.grid_columnconfigure(i, weight=1)

    def setup_keyboard_bindings(self):
        """Setup keyboard shortcuts."""
        self.root.bind('<Key>', self.handle_keypress)
        self.root.focus_set()

    def handle_keypress(self, event):
        """Handle keyboard input."""
        key = event.char

        if key in "0123456789":
            self.insert_digit(key)
        elif key == ".":
            self.insert_digit(".")
        elif key in "+-*/":
            self.insert_operator(key)
        elif key == "\r" or key == "=":  # Enter or equals
            self.calculate()
        elif key == "\x08":  # Backspace
            self.backspace()
        elif key.lower() == "c":
            self.clear_all()
        elif key == "\x1b":  # Escape
            self.clear_entry()

    # Calculator Logic Methods

    def insert_digit(self, digit):
        """Insert a digit into the display."""
        current = self.display_var.get()

        if self.should_reset_display or current == "0":
            if digit == ".":
                self.display_var.set("0.")
            else:
                self.display_var.set(digit)
            self.should_reset_display = False
        else:
            if digit == "." and "." in current:
                return  # Don't add multiple decimal points
            self.display_var.set(current + digit)

    def insert_operator(self, operator):
        """Insert an operator."""
        if not self.should_reset_display:
            self.calculate()  # Calculate any pending operation

        current_value = self.display_var.get()
        self.current_expression = current_value + f" {operator} "
        self.expression_var.set(self.current_expression)
        self.should_reset_display = True

    def insert_constant(self, constant):
        """Insert a mathematical constant."""
        if constant == "pi":
            value = str(math.pi)
        elif constant == "e":
            value = str(math.e)

        if self.should_reset_display:
            self.display_var.set(value)
            self.should_reset_display = False
        else:
            current = self.display_var.get()
            if current == "0":
                self.display_var.set(value)
            else:
                self.display_var.set(current + value)

    def scientific_function(self, function):
        """Apply a scientific function to the current value."""
        try:
            current_value = float(self.display_var.get())

            if function == "sin":
                if self.angle_mode == "degrees":
                    result = math.sin(math.radians(current_value))
                else:
                    result = math.sin(current_value)
            elif function == "cos":
                if self.angle_mode == "degrees":
                    result = math.cos(math.radians(current_value))
                else:
                    result = math.cos(current_value)
            elif function == "tan":
                if self.angle_mode == "degrees":
                    result = math.tan(math.radians(current_value))
                else:
                    result = math.tan(current_value)
            elif function == "asin":
                if abs(current_value) > 1:
                    raise ValueError("Input must be between -1 and 1")
                result = math.asin(current_value)
                if self.angle_mode == "degrees":
                    result = math.degrees(result)
            elif function == "acos":
                if abs(current_value) > 1:
                    raise ValueError("Input must be between -1 and 1")
                result = math.acos(current_value)
                if self.angle_mode == "degrees":
                    result = math.degrees(result)
            elif function == "atan":
                result = math.atan(current_value)
                if self.angle_mode == "degrees":
                    result = math.degrees(result)
            elif function == "ln":
                if current_value <= 0:
                    raise ValueError("Input must be positive")
                result = math.log(current_value)
            elif function == "log":
                if current_value <= 0:
                    raise ValueError("Input must be positive")
                result = math.log10(current_value)
            elif function == "exp":
                result = math.exp(current_value)
            elif function == "sqrt":
                if current_value < 0:
                    raise ValueError("Cannot calculate square root of negative number")
                result = math.sqrt(current_value)
            elif function == "cbrt":
                result = current_value ** (1/3)
            elif function == "square":
                result = current_value ** 2
            elif function == "cube":
                result = current_value ** 3
            elif function == "factorial":
                if current_value < 0 or current_value != int(current_value):
                    raise ValueError("Factorial requires non-negative integer")
                result = math.factorial(int(current_value))
            elif function == "reciprocal":
                if current_value == 0:
                    raise ValueError("Cannot divide by zero")
                result = 1 / current_value
            else:
                return

            # Format and display result
            formatted_result = self.format_number(result)
            self.display_var.set(formatted_result)

            # Add to history
            self.add_to_history(f"{function}({current_value})", formatted_result)
            self.should_reset_display = True

        except (ValueError, OverflowError, ZeroDivisionError) as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Calculation error: {str(e)}")

    def calculate(self):
        """Perform the current calculation."""
        try:
            if self.current_expression:
                full_expression = self.current_expression + self.display_var.get()
                # Replace display operators with Python operators
                full_expression = full_expression.replace("×", "*").replace("÷", "/").replace("−", "-")

                result = eval(full_expression)
                formatted_result = self.format_number(result)

                self.display_var.set(formatted_result)
                self.add_to_history(full_expression, formatted_result)

                self.current_expression = ""
                self.expression_var.set("")
                self.should_reset_display = True

        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero")
            self.clear_all()
        except Exception as e:
            messagebox.showerror("Error", f"Invalid expression: {str(e)}")
            self.clear_all()

    def clear_all(self):
        """Clear everything."""
        self.display_var.set("0")
        self.current_expression = ""
        self.expression_var.set("")
        self.should_reset_display = True

    def clear_entry(self):
        """Clear current entry."""
        self.display_var.set("0")
        self.should_reset_display = True

    def backspace(self):
        """Remove last character."""
        current = self.display_var.get()
        if len(current) > 1:
            self.display_var.set(current[:-1])
        else:
            self.display_var.set("0")
            self.should_reset_display = True

    def toggle_sign(self):
        """Toggle the sign of the current number."""
        current = self.display_var.get()
        try:
            value = float(current)
            self.display_var.set(self.format_number(-value))
        except ValueError:
            pass

    # Memory Functions

    def memory_clear(self):
        """Clear memory."""
        self.memory = 0.0
        self.update_memory_display()

    def memory_recall(self):
        """Recall value from memory."""
        self.display_var.set(self.format_number(self.memory))
        self.should_reset_display = True

    def memory_store(self):
        """Store current value in memory."""
        try:
            self.memory = float(self.display_var.get())
            self.update_memory_display()
        except ValueError:
            pass

    def memory_add(self):
        """Add current value to memory."""
        try:
            current_value = float(self.display_var.get())
            self.memory += current_value
            self.update_memory_display()
        except ValueError:
            pass

    def memory_subtract(self):
        """Subtract current value from memory."""
        try:
            current_value = float(self.display_var.get())
            self.memory -= current_value
            self.update_memory_display()
        except ValueError:
            pass

    def update_memory_display(self):
        """Update memory display label."""
        self.memory_label.config(text=f"M: {self.format_number(self.memory)}")

    # Utility Functions

    def toggle_angle_mode(self):
        """Toggle between degrees and radians."""
        self.angle_mode = "radians" if self.angle_mode == "degrees" else "degrees"
        self.angle_label.config(text=f"Mode: {self.angle_mode.title()}")

    def format_number(self, number):
        """Format number for display."""
        if abs(number) < 1e-10:
            return "0"
        elif abs(number) > 1e10:
            return f"{number:.6e}"
        else:
            # Remove trailing zeros and decimal point if not needed
            formatted = f"{number:.10f}".rstrip('0').rstrip('.')
            return formatted if formatted else "0"

    def add_to_history(self, expression, result):
        """Add calculation to history."""
        self.history.append(f"{expression} = {result}")
        if len(self.history) > 50:  # Keep last 50 calculations
            self.history.pop(0)

    def show_history(self):
        """Show calculation history in a new window."""
        history_window = tk.Toplevel(self.root)
        history_window.title("Calculation History")
        history_window.geometry("400x500")
        history_window.configure(bg=self.colors['bg'])

        # Create scrollable text widget
        frame = tk.Frame(history_window, bg=self.colors['bg'])
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        history_text = tk.Text(
            frame,
            font=('Consolas', 10),
            bg=self.colors['display_bg'],
            fg=self.colors['display_fg'],
            yscrollcommand=scrollbar.set,
            state='disabled'
        )
        history_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=history_text.yview)

        # Populate history
        history_text.config(state='normal')
        if self.history:
            for i, calc in enumerate(reversed(self.history), 1):
                history_text.insert('1.0', f"{i}. {calc}\n")
        else:
            history_text.insert('1.0', "No calculations in history.")
        history_text.config(state='disabled')

        # Clear history button
        clear_btn = tk.Button(
            history_window,
            text="Clear History",
            font=self.fonts['button'],
            bg=self.colors['operator_bg'],
            fg=self.colors['operator_fg'],
            command=lambda: self.clear_history(history_text),
            relief='flat'
        )
        clear_btn.pack(pady=10)

    def clear_history(self, history_text_widget):
        """Clear calculation history."""
        self.history.clear()
        history_text_widget.config(state='normal')
        history_text_widget.delete('1.0', tk.END)
        history_text_widget.insert('1.0', "History cleared.")
        history_text_widget.config(state='disabled')


def main():
    """Main function to run the GUI calculator."""
    root = tk.Tk()
    app = ScientificCalculatorGUI(root)

    # Center the window on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")

    root.mainloop()


if __name__ == "__main__":
    main()