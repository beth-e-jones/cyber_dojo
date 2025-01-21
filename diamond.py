# %%
def print_diamond(letter):

    # ASCII OFFSET for captial A = 1
    CHR_OFFSET = 64
    BLANK = " "

    # input type defence, checking to make sure it's a string
    if not isinstance(letter, str):
        raise TypeError(f"`letter` is not a string. Got type {type(letter)}")

    # make sure function gets only a single letter
    if len(letter) > 1:
        raise Exception(
            f"`letter` must be single character. Got {len(letter)} characters."
        )

    # convert any lower case strings to an upper case string
    captial_letter = letter.upper()

    # convert to ASCII number and subtract a value such that "A" is 1.
    letter_num = ord(captial_letter) - CHR_OFFSET

    # make sure value is expected for a captial letter
    if (letter_num < 1) | (letter_num > 27):
        raise ValueError("`letter` must be a alphabetical character.")

    # number of character in each row
    row_size = (2 * letter_num) - 1

    rows = []
    for i in range(1, letter_num + 1):
        # get the letter to write in the row
        letter_to_write = chr(i + CHR_OFFSET)

        # setting the left side to be empty list with the number of rows equal
        # to the number of letters we're including. Then working backwards to
        # set the letter in it's desire position.
        left_side = [BLANK] * letter_num
        left_side[-1 * i] = letter_to_write

        # setting the right side to be a reversed version of the left, minus
        # the middle column
        right_side = list(reversed(left_side[:-1]))

        # setting the row to be the left and right sides
        row_list = left_side + right_side

        # joining all the individual strings together
        row_str = "".join(row_list)

        # checking the string is the expected length
        if len(row_str) != row_size:
            raise Exception(f"`row_str` ({row_str}) is not expected size.")

        # appending the rows
        rows.append(row_str)

    # create list of reversed rows (minus the centre row), and extend current
    # rows with bottom half
    bottom_half = list(reversed(rows[:-1]))
    rows.extend(bottom_half)

    # check we have the expected number of outputs
    if len(rows) != row_size:
        raise Exception(f"`rows` (len: {len(rows)}) is not expected length.")

    # print whole thing, with a new line for each row
    print("\n".join(rows))


# %%
print_diamond("E")