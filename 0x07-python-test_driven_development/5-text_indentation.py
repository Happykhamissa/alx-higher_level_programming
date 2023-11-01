#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()  # Remove leading/trailing whitespaces

    punctuations = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char
        if char in punctuations:
            print(current_line.strip())  # Print current line without leading/trailing whitespaces
            print()  # Print 2 new lines
            current_line = ""

    if current_line:  # Check if there's any remaining text after the last punctuation
        print(current_line.strip())  # Print the remaining text without leading/trailing whitespaces
