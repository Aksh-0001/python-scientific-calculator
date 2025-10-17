[README.md](https://github.com/user-attachments/files/22975709/README.md)
# Python Scientific Calculator 🧮

A comprehensive scientific calculator application written in Python with both command-line interface (CLI) and graphical user interface (GUI) versions. This project demonstrates advanced Python programming concepts including object-oriented programming, GUI development with Tkinter, mathematical computations, and software engineering best practices.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey.svg)

## 🚀 Features

### 🔢 Basic Operations
- **Arithmetic**: Addition, Subtraction, Multiplication, Division
- **Advanced**: Power, Square Root, Nth Root, Absolute Value
- **Modular arithmetic**: Modulo, Floor Division
- **Sign operations**: Positive/Negative toggle

### 🔬 Scientific Functions
- **Trigonometric**: sin, cos, tan, asin, acos, atan
- **Hyperbolic**: sinh, cosh, tanh, asinh, acosh, atanh
- **Logarithmic**: Natural log (ln), log base 10, log base 2, custom base
- **Exponential**: e^x, 10^x, 2^x
- **Factorial**: n! and double factorial (n!!)

### 📊 Statistical Functions
- **Descriptive Statistics**: Mean, Median, Mode, Range
- **Variability**: Standard Deviation, Variance
- **Aggregate**: Sum, Product, Min, Max

### 🧮 Advanced Mathematics
- **Combinatorics**: Combinations (nCr), Permutations (nPr)
- **Number Theory**: GCD, LCM, Prime checking, Fibonacci
- **Constants**: π, e, τ, Golden Ratio, Physical Constants
- **Complex Numbers**: Support for complex arithmetic

### 💾 Memory & History
- **Memory Operations**: Store, Recall, Add, Subtract, Clear
- **Variable Storage**: Named variables (x, y, etc.)
- **Calculation History**: Last 50+ calculations saved
- **Expression History**: View and replay previous expressions

### 🎯 User Interface Options
- **Command Line Interface (CLI)**: Full-featured text-based interface
- **Graphical Interface (GUI)**: Modern Tkinter-based GUI
- **Keyboard Support**: Full keyboard shortcuts for GUI
- **Angle Modes**: Degrees and Radians support
- **Customizable Precision**: Adjustable decimal places

## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required for basic functionality

### Quick Install
```bash
# Clone the repository
git clone https://github.com/yourusername/python-scientific-calculator.git
cd python-scientific-calculator

# Install as a package (optional)
pip install -e .

# Or run directly
python calculator_cli.py    # For CLI version
python calculator_gui.py    # For GUI version
```

### Install with Optional Dependencies
```bash
# Install with all optional features
pip install -r requirements.txt

# Or install specific feature sets
pip install -e .[scientific]    # NumPy, SciPy
pip install -e .[plotting]      # Matplotlib
pip install -e .[dev]           # Development tools
```

### Using Setup Script
```bash
# Automated setup (checks dependencies and builds)
chmod +x setup_calculator.py
python setup_calculator.py

# Or use the installer script
python installer.py
```

## 🎮 Usage

### Command Line Interface (CLI)

```bash
# Run the CLI calculator
python calculator_cli.py

# Or if installed as package
pycalc
```

**CLI Features:**
- Interactive menu with 42+ operations
- Real-time angle mode display
- Memory status indicator
- Calculation history
- Expression evaluation
- Keyboard shortcuts
- Help system

**Example CLI Session:**
```
===============================
      PYTHON SCIENTIFIC CALCULATOR    
===============================

📐 Current Settings: Angle Mode = Degrees, Precision = 6
💾 Memory: 0

➤ Enter your choice (1-42): 10
Enter angle in degrees: 30
✅ Result: sin(30) = 0.5
```

### Graphical User Interface (GUI)

```bash
# Run the GUI calculator
python calculator_gui.py

# Or if installed as package
pycalc-gui
```

**GUI Features:**
- Modern dark theme interface
- Scientific function buttons
- Memory operation buttons
- Real-time expression display
- History viewer window
- Keyboard input support
- Resizable responsive layout

### Programming Interface

```python
# Use as a module in your code
from calculator_core import MathematicalFunctions, CalculatorMemory

calc = MathematicalFunctions()
memory = CalculatorMemory()

# Basic operations
result = calc.basic_operations(5, 3, '+')  # 8.0

# Scientific functions  
result = calc.trigonometric_functions(30, 'sin', 'degrees')  # 0.5
result = calc.logarithmic_functions(100, 'log')  # 2.0

# Statistical analysis
data = [1, 2, 3, 4, 5]
mean = calc.statistical_functions(data, 'mean')  # 3.0

# Memory operations
memory.store(42.5)
value = memory.recall()  # 42.5
memory.add(7.5)  # Memory now contains 50.0
```

## 📖 Function Reference

### Basic Operations
| Function | CLI Menu | GUI Button | Description |
|----------|----------|------------|-------------|
| Addition | 1 | + | Add two numbers |
| Subtraction | 2 | − | Subtract second from first |
| Multiplication | 3 | × | Multiply two numbers |
| Division | 4 | ÷ | Divide first by second |
| Power | 5 | x^y | Raise to power |
| Square Root | 6 | √ | Square root |

### Scientific Functions
| Function | CLI Menu | GUI Button | Description |
|----------|----------|------------|-------------|
| Sine | 10 | sin | Sine function |
| Cosine | 11 | cos | Cosine function |
| Tangent | 12 | tan | Tangent function |
| Natural Log | 19 | ln | Natural logarithm |
| Log Base 10 | 20 | log | Common logarithm |
| Factorial | 9 | ! | Factorial function |

### Memory Operations
| Function | CLI Menu | GUI Button | Description |
|----------|----------|------------|-------------|
| Store Memory | 32 | MS | Store current value |
| Recall Memory | 33 | MR | Recall stored value |
| Clear Memory | 34 | MC | Clear memory |
| Add to Memory | 35 | M+ | Add to memory |
| Subtract from Memory | 36 | M- | Subtract from memory |

### Constants Available
| Constant | Value | Description |
|----------|-------|-------------|
| π (pi) | 3.14159... | Circle constant |
| e | 2.71828... | Euler's number |
| τ (tau) | 6.28318... | Full circle constant |
| φ (phi) | 1.61803... | Golden ratio |
| c | 299,792,458 | Speed of light (m/s) |

## 🧪 Testing

The project includes comprehensive unit tests covering all mathematical functions:

```bash
# Run all tests
python test_calculator_core.py

# Run with pytest (if installed)
pytest test_calculator_core.py -v

# Run with coverage
pytest test_calculator_core.py --cov=calculator_core --cov-report=html
```

**Test Coverage:**
- ✅ Basic arithmetic operations
- ✅ Trigonometric functions (degrees/radians)
- ✅ Logarithmic and exponential functions
- ✅ Statistical functions
- ✅ Memory operations
- ✅ Expression evaluation
- ✅ Error handling and edge cases

## 🏗️ Project Structure

```
python-scientific-calculator/
├── calculator_cli.py          # Command-line interface
├── calculator_gui.py          # Tkinter GUI interface  
├── calculator_core.py         # Core mathematical functions
├── test_calculator_core.py    # Unit tests
├── setup.py                   # Package setup script
├── requirements.txt           # Dependencies
├── setup_calculator.py        # Automated setup script
├── installer.py               # Installation wizard
├── README.md                  # This file
├── LICENSE                    # MIT License
├── CONTRIBUTING.md            # Contribution guidelines
├── .gitignore                 # Git ignore rules
└── examples/                  # Usage examples
    ├── basic_usage.py         # Basic usage examples
    ├── advanced_usage.py      # Advanced features demo
    └── integration_demo.py    # Integration with other tools
```

## 🔧 Configuration

### Angle Mode Settings
```python
# In CLI: Use option 37 to toggle
# In GUI: Click DEG/RAD button
# In code:
calc.set_angle_mode('degrees')  # or 'radians'
```

### Precision Settings
```python
# In CLI: Use option 38
# In code:
calc.set_precision(10)  # Set to 10 decimal places
```

### Memory Configuration
```python
# Custom memory operations
memory = CalculatorMemory()
memory.store_variable('x', 42.5)  # Named variables
memory.recall_variable('x')       # Returns 42.5
```

## 🚀 Advanced Features

### Expression Evaluation
```python
from calculator_core import ExpressionEvaluator

evaluator = ExpressionEvaluator()
result = evaluator.evaluate_expression("sin(30) + log(100) * sqrt(16)")
# Automatically handles operator precedence and function calls
```

### Batch Processing
```python
# Process multiple expressions
expressions = ["2 + 3", "sin(45)", "log(1000)"]
results = [evaluator.evaluate_expression(expr) for expr in expressions]
```

### Statistical Analysis
```python
# Analyze datasets
data = [1.2, 2.4, 3.6, 4.8, 5.0, 6.2, 7.4, 8.6, 9.8]
stats = {
    'mean': calc.statistical_functions(data, 'mean'),
    'std_dev': calc.statistical_functions(data, 'std_dev'),
    'median': calc.statistical_functions(data, 'median')
}
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup
```bash
# Clone and setup development environment
git clone https://github.com/yourusername/python-scientific-calculator.git
cd python-scientific-calculator

# Install development dependencies
pip install -e .[dev]

# Run tests
python -m pytest

# Format code
black .

# Lint code  
flake8 .
```

### Areas for Contribution
- 🔢 Additional mathematical functions
- 🎨 GUI themes and styling
- 📱 Mobile-responsive interface
- 🧮 Complex number operations
- 📈 Graphing capabilities
- 🌐 Web-based interface
- 📝 Documentation improvements
- 🧪 More test cases
- 🐛 Bug fixes and optimizations

## 📚 Examples

### Basic Calculator Usage
```python
from calculator_core import MathematicalFunctions

calc = MathematicalFunctions()

# Chain calculations
result1 = calc.basic_operations(10, 5, '+')      # 15
result2 = calc.power_and_root_functions(result1, 'square')  # 225
result3 = calc.power_and_root_functions(result2, 'sqrt')    # 15
```

### Scientific Computing
```python
import math

# Convert between angle modes
angle_deg = 45
angle_rad = math.radians(angle_deg)

sin_deg = calc.trigonometric_functions(angle_deg, 'sin', 'degrees')
sin_rad = calc.trigonometric_functions(angle_rad, 'sin', 'radians')
# Both should give approximately 0.707
```

### Statistical Analysis
```python
# Analyze test scores
test_scores = [85, 92, 78, 96, 88, 74, 91, 83, 95, 87]

statistics = {
    'average': calc.statistical_functions(test_scores, 'mean'),
    'median': calc.statistical_functions(test_scores, 'median'),
    'std_dev': calc.statistical_functions(test_scores, 'std_dev'),
    'range': calc.statistical_functions(test_scores, 'range')
}

print(f"Class Average: {statistics['average']:.2f}")
print(f"Median Score: {statistics['median']:.2f}")
print(f"Standard Deviation: {statistics['std_dev']:.2f}")
```

## 🐛 Troubleshooting

### Common Issues

**1. Import Errors**
```bash
# Make sure you're in the correct directory
cd python-scientific-calculator
python calculator_cli.py
```

**2. Tkinter Not Available (Linux)**
```bash
# Install tkinter
sudo apt-get install python3-tk  # Ubuntu/Debian
sudo dnf install tkinter          # Fedora
```

**3. Permission Errors**
```bash
# Make scripts executable
chmod +x *.py
```

**4. Module Not Found**
```python
# Add current directory to Python path
import sys
import os
sys.path.insert(0, os.getcwd())
```

### Performance Tips
- Use CLI version for batch calculations
- Close history window in GUI for better performance
- Clear memory and history periodically for long sessions
- Use appropriate precision settings (6-10 digits usually sufficient)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Python Community** for excellent mathematical libraries
- **Tkinter Documentation** for GUI development guidance
- **Mathematical References** from various educational institutions
- **Testing Framework** pytest community
- **Open Source Contributors** worldwide

## 📞 Support

- 📧 **Email**: calculator@example.com
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/yourusername/python-scientific-calculator/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/yourusername/python-scientific-calculator/discussions)
- 📖 **Documentation**: [Wiki](https://github.com/yourusername/python-scientific-calculator/wiki)

## 🗺️ Roadmap

### Version 2.0 (Planned)
- [ ] **Graphing Calculator**: Plot functions and data
- [ ] **Unit Converter**: Length, weight, temperature, currency
- [ ] **Equation Solver**: Solve algebraic equations
- [ ] **Matrix Operations**: Linear algebra functions
- [ ] **Web Interface**: Browser-based calculator
- [ ] **Mobile App**: Android/iOS versions

### Version 1.5 (In Progress)
- [ ] **Complex Numbers**: Full complex number support
- [ ] **Symbolic Math**: Integration with SymPy
- [ ] **Custom Functions**: User-defined functions
- [ ] **Themes**: Multiple GUI themes
- [ ] **Plugin System**: Extensible architecture

### Version 1.1 (Next Release)
- [ ] **Export/Import**: Save calculations to files
- [ ] **Scripting Mode**: Batch calculation scripts
- [ ] **Better Error Messages**: More descriptive errors
- [ ] **Undo/Redo**: Reverse operations
- [ ] **Calculator Modes**: Basic, Scientific, Programmer

---

Made with ❤️ by Python Calculator Project | [⭐ Star us on GitHub](https://github.com/yourusername/python-scientific-calculator)
