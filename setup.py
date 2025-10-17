#!/usr/bin/env python3
"""
Setup script for Python Scientific Calculator
"""

from setuptools import setup, find_packages
import os
import sys

# Read the README file for long description
def read_readme():
    """Read README.md file for long description."""
    try:
        with open("README.md", "r", encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return "A comprehensive scientific calculator written in Python with both CLI and GUI interfaces."

# Read requirements from requirements.txt
def read_requirements():
    """Read requirements from requirements.txt."""
    try:
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            lines = fh.readlines()
            # Filter out comments and optional dependencies
            requirements = []
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#') and not line.startswith('numpy') and not line.startswith('scipy'):
                    # Skip optional dependencies for basic installation
                    if not any(x in line.lower() for x in ['matplotlib', 'sympy', 'pytest', 'sphinx', 'black', 'flake8', 'mypy', 'pillow']):
                        requirements.append(line)
            return requirements
    except FileNotFoundError:
        return []

# Get version from __init__.py or use default
def get_version():
    """Get version from package or use default."""
    try:
        version_file = os.path.join("calculator", "__init__.py")
        with open(version_file, "r") as f:
            for line in f:
                if line.startswith("__version__"):
                    return line.split("=")[1].strip().strip('"').strip("'")
    except FileNotFoundError:
        pass
    return "1.0.0"

# Ensure we have Python 3.6+
if sys.version_info < (3, 6):
    sys.exit('Python 3.6 or higher is required')

setup(
    name="python-scientific-calculator",
    version=get_version(),
    author="Python Calculator Project",
    author_email="calculator@example.com",
    description="A comprehensive scientific calculator with CLI and GUI interfaces",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/python-scientific-calculator",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/python-scientific-calculator/issues",
        "Documentation": "https://github.com/yourusername/python-scientific-calculator/wiki",
        "Source Code": "https://github.com/yourusername/python-scientific-calculator",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Education",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    keywords="calculator, scientific, mathematics, gui, cli, tkinter, math, computation",
    python_requires=">=3.6",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.2.0",
            "pytest-cov>=2.12.0",
            "black>=21.6.0",
            "flake8>=3.9.0",
            "mypy>=0.910",
        ],
        "scientific": [
            "numpy>=1.21.0",
            "scipy>=1.7.0",
        ],
        "plotting": [
            "matplotlib>=3.4.0",
        ],
        "symbolic": [
            "sympy>=1.8",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=0.5.0",
        ],
        "gui-enhanced": [
            "pillow>=8.3.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "pycalc=calculator_cli:main",
            "pycalc-gui=calculator_gui:main",
            "pycalc-cli=calculator_cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.txt", "*.md", "*.rst"],
    },
    data_files=[
        ("", ["README.md", "LICENSE", "requirements.txt"]),
    ],
    zip_safe=False,
    platforms=["any"],
    test_suite="tests",
)