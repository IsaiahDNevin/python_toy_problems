# Purchase Receipt Formatter

This is a simple command-line Python script that formats and prints a purchase receipt with user input, date, and purchase details.

## Getting Started

Follow these instructions to set up and run the Purchase Receipt Formatter on your local machine.

### Prerequisites
- Python 3.x installed on your system.

### Running the Script
1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the following command:
   ```bash
   python receipt_formatter.py
Script Flow
User Input: The script prompts the user to enter their first name, middle initial, and last name.
Date and Time Capture: Captures the current date and time, rounding it to the nearest minute.
Purchase Details: The script calculates the subtotal, sales tax, and total amount based on the predefined values.
Formatted Receipt: Outputs a formatted receipt displaying the user's name, date of purchase, and purchase details.
Functions
Input Section: Collects the user's name details via input().
Date and Time Processing: Uses datetime to capture and round the current time.
Calculation Section: Performs calculations for subtotal, sales tax, and total.
Output Formatting: Formats the receipt and prints it to the console.
Example Output
yaml
Copy code
name:              Jane D Doe
date of purchase:  2025-01-13 15:45

quantity:          3.00
unit price:    $2,000.00
subtotal:      $6,000.00
sales tax:       $390.00

total:          $6,390.00

Thank you for your purchase!
Notes
The script uses hardcoded values for quantity, unit_price, and sales_tax_rate. These can be adjusted in the script as needed.
Ensure your system's date and time settings are correct, as the script relies on them for accurate date and time capture.
Enjoy the Formatter!