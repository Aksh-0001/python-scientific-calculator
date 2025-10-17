#!/usr/bin/env python3
"""
installer.py - Installation wizard for Python Scientific Calculator
Author: Python Calculator Project
Description: Interactive installer that sets up the calculator with all dependencies
"""

import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path


class CalculatorInstaller:
    """Interactive installer for the Python Scientific Calculator."""

    def __init__(self):
        self.python_version = sys.version_info
        self.platform = platform.system()
        self.install_dir = Path.cwd()
        self.install_success = True

    def display_welcome(self):
        """Display welcome message."""
        print("="*60)
        print("    PYTHON SCIENTIFIC CALCULATOR INSTALLER")
        print("="*60)
        print()
        print("🔬 Welcome to the Python Scientific Calculator installation!")
        print("📦 This installer will set up the calculator with all features.")
        print()
        print(f"🐍 Python Version: {self.python_version.major}.{self.python_version.minor}.{self.python_version.micro}")
        print(f"💻 Platform: {self.platform}")
        print(f"📁 Install Directory: {self.install_dir}")
        print()

    def check_python_version(self):
        """Check if Python version is compatible."""
        print("🔍 Checking Python version...")

        if self.python_version.major < 3 or (self.python_version.major == 3 and self.python_version.minor < 6):
            print("❌ Error: Python 3.6 or higher is required.")
            print(f"   Current version: {self.python_version.major}.{self.python_version.minor}.{self.python_version.micro}")
            print("   Please upgrade Python and try again.")
            return False

        print(f"✅ Python version OK: {self.python_version.major}.{self.python_version.minor}.{self.python_version.micro}")
        return True

    def check_required_files(self):
        """Check if all required files are present."""
        print("\n📋 Checking required files...")

        required_files = [
            'calculator_cli.py',
            'calculator_gui.py', 
            'calculator_core.py',
            'requirements.txt',
            'setup.py'
        ]

        missing_files = []
        for file in required_files:
            if not Path(file).exists():
                missing_files.append(file)
            else:
                print(f"   ✅ {file}")

        if missing_files:
            print("\n❌ Missing required files:")
            for file in missing_files:
                print(f"   - {file}")
            return False

        print("✅ All required files present")
        return True

    def check_tkinter(self):
        """Check if tkinter is available for GUI."""
        print("\n🖼️  Checking GUI support (tkinter)...")

        try:
            import tkinter
            print("✅ Tkinter available - GUI calculator will work")
            return True
        except ImportError:
            print("⚠️  Tkinter not available - only CLI calculator will work")
            if self.platform == "Linux":
                print("   To install tkinter on Linux:")
                print("   Ubuntu/Debian: sudo apt-get install python3-tk")
                print("   Fedora: sudo dnf install tkinter")
                print("   Arch: sudo pacman -S tk")
            return False

    def install_dependencies(self):
        """Install optional dependencies."""
        print("\n📦 Installing dependencies...")

        # Ask user about optional dependencies
        print("\nOptional dependencies:")
        print("1. 🔬 Scientific computing (NumPy, SciPy) - Advanced calculations")
        print("2. 📊 Plotting support (Matplotlib) - Future graphing features")
        print("3. 🧪 Development tools (pytest, black, flake8) - For developers")
        print("4. Skip optional dependencies")

        choice = input("\nSelect option (1-4): ").strip()

        try:
            if choice == "1":
                print("\n🔬 Installing scientific computing packages...")
                self.pip_install("numpy scipy")
            elif choice == "2":
                print("\n📊 Installing plotting packages...")
                self.pip_install("numpy scipy matplotlib")
            elif choice == "3":
                print("\n🧪 Installing development tools...")
                self.pip_install("pytest pytest-cov black flake8 mypy")
            elif choice == "4":
                print("\n⏭️  Skipping optional dependencies")
            else:
                print("\n⚠️  Invalid choice, skipping optional dependencies")

        except Exception as e:
            print(f"\n⚠️  Warning: Could not install optional dependencies: {e}")
            print("   The calculator will still work with basic features.")

    def pip_install(self, packages):
        """Install packages using pip."""
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "--upgrade"
            ] + packages.split())
            print(f"✅ Successfully installed: {packages}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install {packages}: {e}")
            raise

    def install_package(self):
        """Install the calculator as a Python package."""
        print("\n📦 Installing calculator package...")

        install_choice = input("Install as Python package? (y/n): ").lower().strip()

        if install_choice == 'y':
            try:
                subprocess.check_call([
                    sys.executable, "-m", "pip", "install", "-e", "."
                ])
                print("✅ Package installed successfully!")
                print("   You can now use: pycalc (CLI) or pycalc-gui (GUI)")
                return True
            except subprocess.CalledProcessError as e:
                print(f"⚠️  Package installation failed: {e}")
                print("   You can still run the calculator directly with python")
                return False
        else:
            print("⏭️  Skipping package installation")
            return True

    def create_shortcuts(self):
        """Create shortcuts for easy access."""
        print("\n🔗 Creating shortcuts...")

        # Create batch files on Windows
        if self.platform == "Windows":
            self.create_windows_shortcuts()
        # Create shell scripts on Unix-like systems
        elif self.platform in ["Linux", "Darwin"]:
            self.create_unix_shortcuts()

    def create_windows_shortcuts(self):
        """Create Windows batch files."""
        try:
            # CLI shortcut
            cli_bat = self.install_dir / "calculator_cli.bat"
            with open(cli_bat, 'w') as f:
                f.write(f'@echo off\n')
                f.write(f'cd /d "{self.install_dir}"\n')
                f.write(f'python calculator_cli.py\n')
                f.write(f'pause\n')

            # GUI shortcut
            gui_bat = self.install_dir / "calculator_gui.bat"
            with open(gui_bat, 'w') as f:
                f.write(f'@echo off\n')
                f.write(f'cd /d "{self.install_dir}"\n')
                f.write(f'python calculator_gui.py\n')

            print("✅ Created Windows shortcuts:")
            print(f"   - {cli_bat}")
            print(f"   - {gui_bat}")

        except Exception as e:
            print(f"⚠️  Could not create Windows shortcuts: {e}")

    def create_unix_shortcuts(self):
        """Create Unix shell scripts."""
        try:
            # CLI shortcut
            cli_sh = self.install_dir / "calculator_cli.sh"
            with open(cli_sh, 'w') as f:
                f.write(f'#!/bin/bash\n')
                f.write(f'cd "{self.install_dir}"\n')
                f.write(f'python3 calculator_cli.py\n')
            os.chmod(cli_sh, 0o755)

            # GUI shortcut
            gui_sh = self.install_dir / "calculator_gui.sh"
            with open(gui_sh, 'w') as f:
                f.write(f'#!/bin/bash\n')
                f.write(f'cd "{self.install_dir}"\n')
                f.write(f'python3 calculator_gui.py\n')
            os.chmod(gui_sh, 0o755)

            print("✅ Created Unix shortcuts:")
            print(f"   - {cli_sh}")
            print(f"   - {gui_sh}")

        except Exception as e:
            print(f"⚠️  Could not create Unix shortcuts: {e}")

    def run_tests(self):
        """Run tests to verify installation."""
        print("\n🧪 Running tests...")

        test_choice = input("Run tests to verify installation? (y/n): ").lower().strip()

        if test_choice == 'y':
            try:
                # Check if test file exists
                if Path("test_calculator_core.py").exists():
                    print("\n🧪 Running unit tests...")
                    result = subprocess.run([
                        sys.executable, "test_calculator_core.py"
                    ], capture_output=True, text=True)

                    if result.returncode == 0:
                        print("✅ All tests passed!")
                    else:
                        print("⚠️  Some tests failed, but calculator should still work")
                        print("Check the test output above for details")
                else:
                    print("⚠️  Test file not found, skipping tests")

            except Exception as e:
                print(f"⚠️  Could not run tests: {e}")
        else:
            print("⏭️  Skipping tests")

    def display_completion(self):
        """Display completion message and usage instructions."""
        print("\n" + "="*60)
        print("                INSTALLATION COMPLETE!")
        print("="*60)

        if self.install_success:
            print("\n🎉 Python Scientific Calculator installed successfully!")
        else:
            print("\n⚠️  Installation completed with some warnings.")
            print("   The calculator should still work with basic features.")

        print("\n🚀 How to run:")
        print("   CLI Version:")
        print("   - python calculator_cli.py")
        print("   - or: pycalc (if installed as package)")
        if self.platform == "Windows":
            print("   - or: calculator_cli.bat")
        else:
            print("   - or: ./calculator_cli.sh")

        print("\n   GUI Version:")
        print("   - python calculator_gui.py")
        print("   - or: pycalc-gui (if installed as package)")
        if self.platform == "Windows":
            print("   - or: calculator_gui.bat")
        else:
            print("   - or: ./calculator_gui.sh")

        print("\n📚 Documentation:")
        print("   - README.md - Complete documentation")
        print("   - Help system built into both CLI and GUI")

        print("\n🎯 Features available:")
        print("   ✅ Basic arithmetic operations")
        print("   ✅ Scientific functions (trig, log, exp)")
        print("   ✅ Statistical functions")
        print("   ✅ Memory operations")
        print("   ✅ Calculation history")
        print("   ✅ Multiple angle modes")

        print("\n🙏 Thank you for installing Python Scientific Calculator!")
        print("   Report issues: https://github.com/yourusername/python-scientific-calculator/issues")
        print("   Documentation: https://github.com/yourusername/python-scientific-calculator/wiki")

    def run_installation(self):
        """Run the complete installation process."""
        self.display_welcome()

        # Check system requirements
        if not self.check_python_version():
            self.install_success = False
            return False

        if not self.check_required_files():
            self.install_success = False
            return False

        # Check optional components
        self.check_tkinter()

        # Install dependencies
        try:
            self.install_dependencies()
        except Exception:
            self.install_success = False

        # Install as package
        try:
            self.install_package()
        except Exception:
            pass  # Not critical

        # Create shortcuts
        try:
            self.create_shortcuts()
        except Exception:
            pass  # Not critical

        # Run tests
        self.run_tests()

        # Show completion
        self.display_completion()

        return self.install_success


def main():
    """Main installer function."""
    installer = CalculatorInstaller()

    try:
        success = installer.run_installation()

        # Ask if user wants to launch calculator
        print("\n" + "="*60)
        launch_choice = input("Launch calculator now? (cli/gui/n): ").lower().strip()

        if launch_choice == "cli":
            print("\n🚀 Launching CLI calculator...")
            try:
                subprocess.run([sys.executable, "calculator_cli.py"])
            except KeyboardInterrupt:
                print("\n\nCalculator closed by user.")
        elif launch_choice == "gui":
            print("\n🚀 Launching GUI calculator...")
            try:
                subprocess.run([sys.executable, "calculator_gui.py"])
            except KeyboardInterrupt:
                print("\n\nCalculator closed by user.")
        else:
            print("\n👋 Installation complete. You can launch the calculator anytime!")

        return 0 if success else 1

    except KeyboardInterrupt:
        print("\n\n🛑 Installation cancelled by user.")
        return 1
    except Exception as e:
        print(f"\n❌ Installation failed with error: {e}")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)