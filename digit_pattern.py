# %%
def get_lcd_digit(number):
    """Handle digit building."""

    LCD_DIGITS = {
        "-": [
            "   ",
            " --",
            "   ",
        ],
        0: [
            ".-.",
            "| |",
            "|_|",
        ],
        1: [
            " . ",
            " | ",
            " | ",
        ],
        2: [
            " -.",
            " _|",
            "|_.",
        ],
        3: [
            "--.",
            "--|",
            "__|",
        ],
        4: [
            ". .",
            "|_|",
            "  |",
        ],
        5: [
            ".- ",
            "|_ ",
            "._|",
        ],
        6: [
            ".- ",
            "|-.",
            "|_|",
        ],
        7: [
            ".-.",
            "  |",
            "  |",
        ],
        8: [
            ".-.",
            "|-|",
            "|_|",
        ],
        9: [
            ".-.",
            "|_|",
            " _|",
        ],
    }

    try:
        lcd_digit = LCD_DIGITS[number]
    except KeyError:
        raise KeyError(f"{number} is not in LCD_DIGITS.")

    return lcd_digit


def convert_pattern_to_row(pattern, sep=" "):
    """Convert pattern into a string inside a list."""
    return [sep.join(pattern)]


def lcd_digits(num):
    """Print an LCD-type display for the numbers provided."""

    # defence against case where num is not an integer
    if not isinstance(num, int):
        raise TypeError(f"`num` is not an integer, got {num}.")

    # convert num into a string - to go through each digit
    digits_str = str(num)

    lcd_digits = []
    for digit_str in digits_str:

        # convert string to individual integer
        if digit_str == "-":
            digit = "-"
        else:
            digit = int(digit_str)

        # retrieve digit
        lcd_digit = get_lcd_digit(digit)

        # add pattern to end of lcd_digits
        lcd_digits.append(lcd_digit)

    # extract all the top, middle, and bottom patterns for each digit
    top_patterns = [pattern[0] for pattern in lcd_digits]
    middle_patterns = [pattern[1] for pattern in lcd_digits]
    bottom_patterns = [pattern[2] for pattern in lcd_digits]

    # converts parterns into single strings, with a space inbetween
    # puts the string in a list to concatenate them together more easily
    top_row = convert_pattern_to_row(top_patterns)
    middle_row = convert_pattern_to_row(middle_patterns)
    bottom_row = convert_pattern_to_row(bottom_patterns)

    # concatenate the strings
    rows = top_row + middle_row + bottom_row

    # print out each row separated by a new line
    print("\n".join(rows))


# %%
lcd_digits(10549)

# %%