# im a 17 year old self taught software developer here are some of my python toy problems

### Average List Calculator
- This Python script calculates the average of a list of numbers - - provided by the user.

**Features**
1. Calculates the average of a list of numbers.
2. Takes user input for custom lists of numbers.

### Days Until Date Calculator
- This Python script calculates the number of days remaining until a specific date (like a birthday) in the current year or the next - year, if the date has already passed.

**Features**
1. Takes user input for a month and day (e.g., "January 25").
2. Calculates the number of days remaining until the given date.
3. Handles invalid month names and incorrect input formats.

### Palindrome Checker
- This Python script checks if a given string is a palindrome. A - palindrome is a word, phrase, or sequence that reads the same backward as forward (ignoring spaces and punctuation).

**Features**
1. Checks if a string is a palindrome.
2. Iterates through each character in the string to compare it with 3. the corresponding character from the end.

### Password Strength Checker
- This Python script checks the strength of a password based on length, uppercase letter inclusion, and special character inclusion. If the password doesn't meet the criteria, the user will be prompted to provide a stronger one.

**Features**
1. Ensures the password is at least 8 characters long.
2. Checks if the password contains at least one uppercase letter.
3. Checks if the password contains at least one special character.
4. Provides helpful prompts to guide the user in creating a stronger - password.

### Goal Achievement Time Estimator
- This Python script calculates how long it will take to reach a specific financial goal based on your hourly rate, work hours per day, and workdays per week.

**Features**
1. Estimates how many weeks and months it will take to reach a 
2. specified financial goal.
3.Takes user input for hourly rate, hours worked per day, days worked per week, and financial goal.
4. Provides the estimated time in weeks and months to reach the goal.

### Pyramid Generator
- This Python script generates a pyramid pattern of characters based on user input. You provide the height of the pyramid and the character to use, and the script will display a pyramid shape.

**Features**
1. Generates a pyramid pattern with a specified height.
2. Allows you to specify the character used to build the pyramid.
3. The pyramid starts with one character at the top and grows in width as it goes down.


### Receipt Generator
- This Python script generates a formatted receipt based on user input, including their name, purchase details, and the current date and time. The receipt includes calculations for subtotal, sales tax, and total amount.

**Features**
1. Captures the user's first name, middle initial, and last name.
2. Retrieves and rounds the current date and time to the nearest minute.
3. Computes the subtotal, sales tax, and total for the purchase.
4. Displays a formatted receipt with relevant purchase information.

### Reverse String
- This Python script defines a function that reverses the order of characters in a string. It works by iterating through each character in the string and progressively building a new string that contains the characters in reverse order.

**Features**
1. Reverses the input string by iterating through each character.
2. Builds the reversed string one character at a time.

### Temperature Converter
- This Python script allows the user to convert between Celsius and Fahrenheit. It prompts the user to choose the conversion type, then asks for the temperature in the chosen unit. The script performs the appropriate conversion and displays the result.

**Features**
1. Prompts the user to choose between Fahrenheit and Celsius.
2. Converts the temperature from Fahrenheit to Celsius or vice versa.
3. Ensures valid input for temperature type (F or C).
4. Outputs the converted temperature in the correct unit.



###### TESTS

### Unit Test for Palindrome Checker
- This Python script contains unit tests for the palindrome() function. It tests the function for different inputs to verify if it correctly identifies palindromes and non-palindromes.

**Features**
1. Tests the palindrome() function with various types of input.
2. Verifies if the function returns True for palindromes and False for non-palindromes.
3. Includes test cases for an empty string, a valid palindrome, and a non-palindrome word.

### Unit Test for Reverse String Function
- This Python script contains unit tests for the reverse_string() function. It tests the function for different string inputs to ensure it correctly reverses the input string.

**Features**
1. Tests the reverse_string() function with various types of input, including single letters, multiple letters, and longer words.
2. Verifies that the function correctly reverses strings.
3. Includes a commented-out test for handling invalid inputs (e.g., numbers) to check for TypeError.

### Unit Test for Temperature Converter
- This Python script contains unit tests for a temperature conversion program. It tests various functions involved in the program, including user input for temperature type, the conversion logic between Fahrenheit and Celsius, and the main execution of the program.

**Features**
1. User Input: Verifies that the user is prompted to input the temperature type (Fahrenheit or Celsius) correctly.
2. Temperature Conversion: Tests the logic for converting between Fahrenheit and Celsius.
3. Main Program Execution: Ensures that the main function calls the necessary functions and produces the correct output.

