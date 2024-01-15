def roman_to_int(roman_string):
    # Check if the input is a valid string
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Define a dictionary mapping Roman numerals to their integer values
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Initialize a variable to keep track of the result
    result = 0

    # Iterate through the Roman numeral string
    for i in range(len(roman_string)):
        # If the current numeral is smaller than the next numeral, subtract its value
        if i < len(roman_string) - 1 and roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
            result -= roman_dict[roman_string[i]]
        else:
            # Otherwise, add its value to the result
            result += roman_dict[roman_string[i]]

    # Return the final result
    return result
