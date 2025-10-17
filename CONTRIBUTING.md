# Contributing to Python Scientific Calculator

Thank you for your interest in contributing to the Python Scientific Calculator project! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### 1. Fork the Repository

1. Fork the repository on GitHub
2. Clone your fork locally:
```bash
git clone https://github.com/yourusername/python-scientific-calculator.git
cd python-scientific-calculator
```

### 2. Set Up Development Environment

#### Prerequisites
- Python 3.6 or higher
- Git
- Text editor or IDE (VS Code, PyCharm, etc.)

#### Install Dependencies
```bash
# Install the package in development mode
pip install -e .

# Install development dependencies
pip install -r requirements.txt

# Or install with development extras
pip install -e .[dev]
```

#### Optional Tools for Quality Assurance
```bash
# Code formatting
pip install black

# Code linting  
pip install flake8

# Type checking
pip install mypy

# Testing framework
pip install pytest pytest-cov
```

### 3. Making Changes

1. **Create a new branch** for your feature or bug fix:
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-description
```

2. **Make your changes** following the coding standards below

3. **Test your changes** thoroughly:
```bash
# Run unit tests
python test_calculator_core.py

# Or with pytest
pytest test_calculator_core.py -v

# Test both CLI and GUI
python calculator_cli.py
python calculator_gui.py
```

4. **Commit your changes** with clear, descriptive messages:
```bash
git add .
git commit -m "Add new trigonometric function: secant

- Implement sec(x) function in MathematicalFunctions class
- Add corresponding GUI button in scientific functions panel
- Include unit tests for secant function
- Update documentation with secant function usage"
```

### 4. Testing Requirements

Before submitting your changes, ensure:

#### Automated Testing
```bash
# Run all unit tests
python test_calculator_core.py

# Run with coverage (if pytest installed)
pytest --cov=calculator_core --cov-report=html

# All tests should pass with no failures
```

#### Manual Testing
1. **Test CLI calculator:**
   - Launch `python calculator_cli.py`
   - Test your new functionality
   - Verify existing functions still work
   - Check error handling

2. **Test GUI calculator:**
   - Launch `python calculator_gui.py`
   - Test your changes in the GUI
   - Verify button layouts and functionality
   - Test keyboard shortcuts

3. **Test edge cases:**
   - Division by zero
   - Invalid inputs
   - Very large/small numbers
   - Boundary conditions

#### Code Quality Checks
```bash
# Format code (if black installed)
black .

# Check code style (if flake8 installed)
flake8 calculator_*.py

# Type checking (if mypy installed)
mypy calculator_core.py
```

### 5. Submit Changes

1. **Push your changes** to your fork:
```bash
git push origin feature/your-feature-name
```

2. **Create a Pull Request** on GitHub with:
   - **Clear title** describing the change
   - **Detailed description** explaining:
     - What changes were made
     - Why the changes were necessary
     - How the changes were tested
   - **Reference to related issues** (if any)
   - **Screenshots** (for GUI changes)

## 📝 Coding Standards

### Python Style Guide
- Follow **PEP 8** Python style guidelines
- Use **4 spaces** for indentation (no tabs)
- Keep **line length under 88 characters** (Black formatter default)
- Use **descriptive variable and function names**
- Add **docstrings** for all functions and classes

### Code Organization
```python
def calculate_hypotenuse(a: float, b: float) -> float:
    """
    Calculate the hypotenuse of a right triangle.
    
    Args:
        a (float): Length of first side
        b (float): Length of second side
        
    Returns:
        float: Length of hypotenuse
        
    Raises:
        ValueError: If either side is negative
    """
    if a < 0 or b < 0:
        raise ValueError("Side lengths must be non-negative")
    
    return math.sqrt(a**2 + b**2)
```

### Function Documentation Format
```python
def function_name(param1: type, param2: type) -> return_type:
    """
    Brief description of what the function does.
    
    Args:
        param1 (type): Description of parameter 1
        param2 (type): Description of parameter 2
        
    Returns:
        return_type: Description of return value
        
    Raises:
        ExceptionType: Description of when this exception is raised
        
    Example:
        >>> result = function_name(5, 10)
        >>> print(result)
        15
    """
```

### Error Handling Guidelines
```python
# Good: Specific exception types with helpful messages
try:
    result = math.log(x)
except ValueError:
    raise ValueError(f"Logarithm requires positive input, got {x}")

# Good: Input validation
def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("Factorial requires integer input")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n > 170:
        raise ValueError("Factorial input too large (max 170)")
    return math.factorial(n)
```

### GUI Development Standards
- Use **consistent styling** with existing interface
- Ensure **keyboard accessibility**
- Add **tooltips** for complex functions
- Test **window resizing** behavior
- Follow **responsive design** principles

## 🐛 Bug Reports

When reporting bugs, please include:

### Bug Report Template
```markdown
## Bug Description
A clear and concise description of the bug.

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. Enter value '...'
4. See error

## Expected Behavior
A clear description of what you expected to happen.

## Actual Behavior
A clear description of what actually happened.

## Environment
- OS: [e.g., Windows 10, macOS 12.0, Ubuntu 20.04]
- Python Version: [e.g., 3.9.7]
- Calculator Version: [e.g., 1.0.0]

## Screenshots
If applicable, add screenshots to help explain your problem.

## Additional Context
Add any other context about the problem here.
```

## 💡 Feature Requests

When suggesting new features:

### Feature Request Template
```markdown
## Feature Description
A clear and concise description of the feature you'd like to see.

## Use Case
Describe the problem this feature would solve or the benefit it would provide.

## Proposed Implementation
If you have ideas about how this could be implemented, describe them here.

## Alternative Solutions
Describe any alternative solutions or workarounds you've considered.

## Additional Context
Add any other context, mockups, or examples about the feature request.
```

## 🎯 Types of Contributions Welcome

### 🔢 New Mathematical Functions
- Additional trigonometric functions (sec, csc, cot)
- More statistical functions (skewness, kurtosis)
- Financial calculations (compound interest, loan payments)
- Engineering functions (decibel calculations, unit conversions)

### 🎨 User Interface Improvements
- New GUI themes (light theme, high contrast)
- Better keyboard shortcuts
- Improved button layouts
- Mobile-responsive design

### 🧪 Testing and Quality Assurance
- Additional unit tests
- Integration tests
- Performance benchmarking
- Cross-platform testing

### 📚 Documentation
- Improve README documentation
- Add usage examples
- Create video tutorials
- Translate documentation

### 🛠️ Developer Tools
- GitHub Actions for CI/CD
- Automated code formatting
- Performance profiling
- Security analysis

### 🔧 Infrastructure
- Package distribution improvements
- Installation scripts for different platforms
- Docker containerization
- Web-based version

## 📋 Development Workflow

### Branch Naming Convention
- `feature/function-name` - New features
- `bugfix/issue-description` - Bug fixes
- `docs/section-name` - Documentation updates
- `refactor/component-name` - Code refactoring
- `test/test-description` - Test improvements

### Commit Message Format
```
type: brief description

Detailed explanation of the changes made, including:
- What was changed
- Why it was changed
- How it affects existing functionality

Fixes #123 (if fixing an issue)
```

**Types:** feat, fix, docs, style, refactor, test, chore

### Pull Request Process
1. **Update documentation** if needed
2. **Add/update tests** for new functionality
3. **Ensure all tests pass**
4. **Update CHANGELOG** if significant changes
5. **Request review** from maintainers
6. **Address feedback** promptly

## 🏆 Recognition

Contributors are recognized through:
- **GitHub contributor statistics**
- **Mention in release notes** for significant contributions
- **Special thanks** in README for major features
- **Maintainer status** for consistent, high-quality contributions

## 📞 Getting Help

### Community Support
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/yourusername/python-scientific-calculator/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/yourusername/python-scientific-calculator/discussions)
- ❓ **Questions**: [GitHub Discussions Q&A](https://github.com/yourusername/python-scientific-calculator/discussions/categories/q-a)
- 📖 **Documentation**: [Project Wiki](https://github.com/yourusername/python-scientific-calculator/wiki)

### Development Questions
- **Code review questions**: Comment on your Pull Request
- **Architecture discussions**: Start a GitHub Discussion
- **Implementation help**: Create an issue with "help wanted" label

## 📜 Code of Conduct

### Our Standards
- **Be respectful** and inclusive
- **Be constructive** in feedback
- **Be patient** with newcomers
- **Be collaborative** in problem-solving

### Unacceptable Behavior
- Harassment or discrimination
- Trolling or inflammatory comments
- Publishing private information
- Any conduct that disrupts the community

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the same MIT License that covers the project.

## 🙏 Thank You!

Your contributions help make this calculator better for everyone. Whether you're fixing bugs, adding features, improving documentation, or helping other users, your efforts are appreciated!

---

**Questions?** Feel free to reach out through GitHub Issues or Discussions. We're here to help! 🚀