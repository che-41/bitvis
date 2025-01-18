# Bit Converter Application

This project is a Python application built with PyQt6 that allows users to convert numbers between Decimal, Hexadecimal, and Binary formats while displaying the corresponding bit positions. It features a modern GUI with a focus on usability and functionality.

## Features

- **Number Conversion:** Enter a number in Decimal, Hexadecimal, or Binary format, and view the equivalent in all three formats.
- **Bit Display:** Visualize which bits are set (1) or unset (0) for numbers up to 32 bits.
- **Interactive Bit Toggle:** Click on any bit position to toggle its value, with all formats updating automatically.
- **Keyboard Shortcuts:**
  - `Alt+1`: Select Decimal input format.
  - `Alt+2`: Select Hexadecimal input format.
  - `Alt+3`: Select Binary input format.
  - `Ctrl+C`: Copy the current input value to the clipboard.
- **Tausender-Trennzeichen:** Input numbers with thousands separators for better readability.
- **Focus Control:**
  - Press `Enter` to switch focus to the input field.
  - Automatic focus handling when clicking outside the bit display.
- **Modern Design:** Rounded corners and adaptive styling for a polished user experience.

## Requirements

- Python 3.8 or later
- PyQt6

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bit-converter.git
   cd bit-converter
   ```
2. Install the required packages:
   ```bash
   pip install PyQt6
   ```
3. Run the application:
   ```bash
   python bit_converter.py
   ```

## Usage

1. Start the application.
2. Enter a number in the input field and select the input format (Dec, Hex, Bin) from the dropdown.
3. View the converted values in the output area and interact with the bit display to toggle specific bits.

## Shortcuts

| Shortcut       | Action                      |
|----------------|-----------------------------|
| `Alt+1`        | Select Decimal format       |
| `Alt+2`        | Select Hexadecimal format   |
| `Alt+3`        | Select Binary format        |
| `Ctrl+C`       | Copy input value to clipboard |
| `Enter`        | Switch focus to input field |
| `Escape`       | Clear input (or exit if empty) |

## Screenshots

*Add screenshots here to showcase the GUI and features.*

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests to improve the application.

---

Happy converting!

