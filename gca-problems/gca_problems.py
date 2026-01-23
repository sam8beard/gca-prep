"""
GCA Practice – LeetCode-Style Test Harness
----------------------------------------
Instructions:
1. Implement each function where marked.
2. Run this file: `python gca_tests.py`
3. Fix failures, re-run.
"""

# ============================================================
# 1. Array Mutation
# ============================================================
"""
Problem: Array Mutation

Given an integer n and an array a of length n, apply the following mutation:

- Create a new array b of length n
- For each index i:
    b[i] = a[i-1] + a[i] + a[i+1]
- If an index is out of bounds, treat its value as 0

Example:
Input:  n = 5, a = [4, 0, 1, -2, 3]
Output: [4, 5, -1, 2, 1]
"""


def array_mutation(n, a):
    b = [0] * n

    def correct_index(num):
        if not (0 <= num < len(a)):
            return 0
        return a[num]

    for i in range(len(a)):
        left, right = correct_index(i - 1), correct_index(i + 1)
        b[i] = left + a[i] + right

    return b


def test_array_mutation():
    assert array_mutation(5, [4, 0, 1, -2, 3]) == [4, 5, -1, 2, 1]
    assert array_mutation(1, [10]) == [10]
    assert array_mutation(3, [0, 1, 0]) == [1, 1, 1]


# ============================================================
# 2. Array Triplets with Pythagorean Property
# ============================================================
"""
Problem: Array Triplets with Pythagorean Property

Given an integer array of length n, return a result array of length n-2.
For each i, result[i] = 1 if ANY of the following is true:

- array[i]^2 + array[i+1]^2 == array[i+2]^2
- array[i+1]^2 + array[i+2]^2 == array[i]^2
- array[i]^2 + array[i+2]^2 == array[i+1]^2

Otherwise, result[i] = 0.
"""


def pythagorean_triplets(arr):
    res = [None] * (len(arr) - 2)

    def produce_val(index):
        val = 0

        first = (arr[index]**2 + arr[index+1]**2) == arr[index+2]**2
        second = (arr[index+1]**2 + arr[index+2]**2) == arr[index]**2
        third = (arr[index]**2 + arr[index+2]**2) == arr[index+1]**2

        if first or second or third:
            val = 1
        return val

    for i in range(len(res)):
        val = produce_val(i)
        res[i] = val
    return res


def test_pythagorean_triplets():
    assert pythagorean_triplets([3, 4, 5, 6]) == [1, 0]
    assert pythagorean_triplets([5, 12, 13]) == [1]
    assert pythagorean_triplets([1, 2, 3]) == [0]


# ============================================================
# 3. Card Hand Validation
# ============================================================
"""
Problem: Card Hand Validation

Each card consists of:
- A suit: '+', '-', '='
- A value: 'A', 'B', or 'C'
- A count: 1 to 3 (number of letters)

A valid hand contains exactly 3 cards such that:
- Suits are all the same OR all different
- Values are all the same OR all different
- Counts are all the same OR all different

Return the FIRST valid hand found.
If no valid hand exists, return None.
"""


def first_valid_hand(cards):
    """
    Given a list of strings, we need to find the first combination of 3 strings whose characters are either:
    - Exactly the same
    OR
    - Completely unique

    Given a list of tuples, we need to find the first 3 tuples that either:
    - Are exactly the same
        OR
    - Are completely unique

    """

    # Build tuples from strings for evaluation
    d = {}
    for i in range(len(cards)):

        c = cards[i]
        letters = [char for char in c if char.isalpha()]
        count = len(letters)
        val = set(letters).pop()
        suit = [char for char in c if not char.isalpha()].pop()

        d[i] = (count, suit, val)

    def is_valid(hand):
        # validate hand under constraints
        counts = [hand[0][0], hand[1][0], hand[2][0]]
        suits = [hand[0][1], hand[1][1], hand[2][1]]
        values = [hand[0][2], hand[1][2], hand[2][2]]

        valid_counts = (len(counts) == len(set(counts))
                        or (len(set(counts)) == 1))
        valid_suits = (len(suits) == len(set(suits))
                       or (len(set(suits)) == 1))
        valid_values = (len(values) == len(set(values))
                        or (len(set(values)) == 1))

        if valid_counts and valid_suits and valid_values:
            return True
        return False

    # Brute force
    for i in range(len(d)):
        for j in range(i + 1, len(d)):
            for k in range(j + 1, len(d)):
                if is_valid([d[i], d[j], d[k]]):
                    return [cards[i], cards[j], cards[k]]
    return None


def test_first_valid_hand():
    global CURRENT_TEST_CASE

    CURRENT_TEST_CASE = "original"
    cards = ["+AA", "-AA", "+AA", "-C", "-B", "+AA", "-AAA", "-A", "=AA"]
    res = first_valid_hand(cards)
    assert res is not None
    assert len(res) == 3

    # case 1: first three identical (same suit + value)
    CURRENT_TEST_CASE = "first three identical"
    cards = ["+AA", "+AA", "+AA", "-AA", "=AA"]
    res = first_valid_hand(cards)
    assert res == ["+AA", "+AA", "+AA"]

    # case 2: completely unique across suit and value
    CURRENT_TEST_CASE = "suit and value completely unique"
    cards = ["+A", "-B", "=C", "+A", "-A"]
    res = first_valid_hand(cards)
    assert res == ["+A", "-B", "=C"]

    # case 3: invalid
    CURRENT_TEST_CASE = "dupes early, valid later"
    cards = ["+AA", "+AA", "-AA", "+B", "-C", "=D"]
    res = first_valid_hand(cards)
    assert res == ["+B", "-C", "=D"]

    # case 4: valid hand
    CURRENT_TEST_CASE = "valid hand"
    cards = ["+AA", "-AA", "=AA", "+AB", "-AB"]
    res = first_valid_hand(cards)
    assert res == ["+AA", "-AA", "=AA"]

    # case 5: exactly three, valid (unique)
    CURRENT_TEST_CASE = "exactly three valid, unique"
    cards = ["+A", "-B", "=C"]
    res = first_valid_hand(cards)
    assert res == ["+A", "-B", "=C"]

    # case 6: exactly three, valid (identical)
    CURRENT_TEST_CASE = "exactly three valid, identical"
    cards = ["-BBB", "-BBB", "-BBB"]
    res = first_valid_hand(cards)
    assert res == ["-BBB", "-BBB", "-BBB"]

    # case 7: invalid hand
    CURRENT_TEST_CASE = "invalid hand"
    cards = ["+A", "+A", "-AA", "+B", "=CC", "-D"]
    res = first_valid_hand(cards)
    assert res is None


# ============================================================
# 4. Character Cascade from String Array
# ============================================================
"""
Problem: Character Cascade from String Array

Given an array of strings, construct a result string by:
- Taking the 0th character of each word (in order)
- Then the 1st character of each word
- Continue until all characters are consumed
- Skip words that do not have a character at index i

Example:
Input:  ["Daisy","Rose","Hyacinth","Poppy"]
Output: "DRHPaoyoisapsecpyiynth"
"""


def char_cascade(arr):
    from collections import defaultdict
    d = defaultdict(str)
    res = ""
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            d[j] += arr[i][j]

    for v in d.values():
        res += v
    return res


def test_char_cascade():
    assert char_cascade(["Daisy", "Rose", "Hyacinth", "Poppy"]
                        ) == "DRHPaoyoisapsecpyiynth"
    assert char_cascade(["abc", "de", "f"]) == "adfbec"
    assert char_cascade(["a", "b", "c"]) == "abc"
    assert char_cascade(["ab", ""]) == "ab"


# ============================================================
# 5. Count Valid Words from String
# ============================================================
"""
Problem: Count Valid Words from String

Given:
- A string containing words separated by spaces
- A string of valid letters

Rules:
- A word is valid if all alphabetic characters (case-insensitive)
  appear in the valid letters list
- Numbers and punctuation are always valid

Return the count of valid words.
"""


def count_valid_words(string, letters):
    import string as s

    word_list = [x.lower() for x in string.split()]
    letter_list = list(letters)
    d = {0: [], 1: []}

    for i in range(len(word_list)):
        cleaned = ""
        for c in word_list[i]:
            if (c in s.punctuation or c.isdigit()) or \
                    (c.isalpha() and c in letter_list):
                cleaned += c
        valid = cleaned == word_list[i]
        d[valid].append(word_list[i])
    return len(d[1])


def test_count_valid_words():
    assert count_valid_words("Hello, I am h2ere!", "heloiar") == 3
    assert count_valid_words("123 abc", "abc") == 2


# ============================================================
# 6. Game Field Matrix Puzzle
# ============================================================
"""
Problem: Game Field Matrix Puzzle

You are given:
- A game field matrix (n x m) of 0s and 1s
- A figure matrix (3 x 3) of 0s and 1s

The figure is dropped vertically from the top at a column position.
It falls until it collides or reaches the bottom.

Return a column index such that placing the figure results in
at least one fully occupied row.

If multiple answers exist, return any.
If none exist, return -1.
"""


def display_grid(grid):
    # Print figure
    for r in range(len(grid)):
        print(f'{grid[r]}\n')

    print("\n")


def find_full_line(field, figure):
    print("Figure")
    display_grid(figure)
    print("Field")
    display_grid(field)
    """
    n = len(field)
    m = len(field[0])
    fig_h = len(figure)
    fig_w = len(figure[0])

    for drop_pos in range(m - fig_w + 1):
        # deep copy the field
        temp_field = [row[:] for row in field]

        # determine how far the figure can fell
        max_drop = n - fig_h
        for r in range(n - fig_h + 1):
            collision = False
            for fr in range(fig_h):
                for fc in range(fig_w):
                    if figure[fr][fc] == 1 and temp_field[r + fr][drop_pos + fc] == 1:
                        collision = True
                        break
                if collision:
                    break
            if collision:
                max_drop = r - 1
                break
        if max_drop < 0:
            continue

        # place the figure
        for fr in range(fig_h):
            for fc in range(fig_w):
                if figure[fr][fc] == 1:
                    temp_field[max_drop + fr][drop_pos + fc] = 1
                    display_grid(temp_field)
        # check for a full row
        for row in temp_field:
            if all(cell == 1 for cell in row):
                return drop_pos
    return - 1

    """
    import copy

    field_width = len(field[0])
    field_height = len(field)
    fig_width = len(figure[0])
    fig_height = len(figure)
    drop_pos = 0
    for drop_pos in range(0, field_width - fig_width + 1):
        print(f'Drop position: {drop_pos}')
        # reset state of field
        temp_field = copy.deepcopy(field)
        # drop each column of the figure
        for fig_c in range(fig_width):

            # print(fig_c)
            # corresponding field column to drop the figure column values into
            field_c = drop_pos + fig_c

            """
            Starting from the bottom cell in figure, 
            drop each cell value into the corresponding field column
            """
            for fig_r in range(fig_height - 1, -1, -1):
                """
                Move the value downwards, until:
                - a collision is detected (there is a 1 below the current field row)
                - the bottom is reached (field row == len(field) - 1)
                """
                # print(fig_r)
                # get figure cell value
                fig_block = figure[fig_r][fig_c]

                # if cell value is 0, skip
                if fig_block == 0:
                    continue

                print(f'{fig_block} being dropped into column {field_c}')

                # Go row by row in the field, starting from the top, placing values in field
                field_r = 0
                while field_r + 1 < len(temp_field) and temp_field[field_r + 1][field_c] == 0:
                    field_r += 1

                # place dropped value into field cell
                temp_field[field_r][field_c] = fig_block
                display_grid(temp_field)
            print()
        # scan rows for win condition
        for field_r in temp_field:
            if all(cell == 1 for cell in field_r):
                print("Firing in win condition:", drop_pos)
                return drop_pos
    return -1

    """
    # Starting column position in field that the figure is being dropped from
    drop_pos = 0

    # Iteratively drop the figure from a drop position
    while 0 <= drop_pos <= (len(field[0]) - len(figure[0])):
        # print(drop_pos, len(figure[0]), len(field[0]))
        # print(f'Dropping figure at column {drop_pos} in field')

        # Reset state for next drop
        temp_field = field[:]
        temp_fig = figure[:]

        # Figure column being dropped
        fig_col = 0
        # Drop a columns of values from the figure into the field
        for field_c in range(drop_pos, len(temp_fig[0]), 1):
            print("first level 1")
            # Current row in the field being evaluated
            field_level = 0
            # Traverse down a column of the field
            while field_level < len(temp_field):
                print("second level 1")
                # Drop a column of values from the figure
                for fig_r in range(len(temp_fig[0]) - 1, -1, -1):
                    print("third level 1")
                    # Does a piece exist in the figure column?
                    if temp_fig[fig_r][fig_col] == 1:
                        print("piece exists in figure")
                        # Move the piece down until the bottom of the field is hit, or the cell below is not empty
                        # While the cell below the piece is empty
                        inbounds = field_level + 1 < len(temp_field)
                        if inbounds:
                            print("inbounds")
                            print(temp_field[field_level + 1])
                            print(temp_field[field_level + 1][field_c])
                            while temp_field[field_level + 1][field_c] == 0:
                                print("moving down")
                                print(fig_r, fig_col)
                                print(temp_fig[fig_r][fig_col])
                                temp_field[field_level +
                                           1][field_c] = temp_fig[fig_r][fig_col]

                                # Evaluate next row of values in the field
                                field_level += 1
                # Evaluate next row of values in the field
                field_level += 1
            # Drop next column of values
            fig_col += 1
        # Move drop position right
        drop_pos += 1
        """


def test_find_full_line():
    # --- Test Case 1:  One valid column ---
    field1 = [
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0]
    ]
    figure1 = [
        [1, 1, 1],
        [0, 1, 0],
        [0, 1, 0]
    ]
    assert find_full_line(field1, figure1) == 1

    # --- Test Case 2: Empty field, figure fits anywhere ---
    field2 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    figure2 = [
        [1, 0, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    # Any column where the 3x3 figure fits horizontally is valid (0 only)
    assert find_full_line(field2, figure2) == 0

    # --- Test Case 3 ---
    field3 = [
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1]
    ]
    figure3 = [
        [1, 1, 0],
        [0, 1, 1],
        [1, 0, 1]
    ]
    assert find_full_line(field3, figure3) == 1

    # --- Test Case 4: Figure can fill bottom row exactly ---
    field4 = [
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 0]
    ]
    figure4 = [
        [1, 1, 0],
        [0, 1, 1],
        [0, 0, 1]
    ]
    # Only one column allows a full row at the bottom
    assert find_full_line(field4, figure4) == 1

    # --- Test Case 5: Figure partially occupied, multiple rows could be filled ---
    field5 = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1]
    ]
    figure5 = [
        [1, 1, 0],
        [0, 1, 1],
        [1, 0, 0]
    ]
    # Multiple columns could potentially produce a fully filled row
    assert find_full_line(field5, figure5) in [0, 1, 2, -1]

    # --- Test Case 6: Figure wider than field, invalid placement ---
    field6 = [
        [0, 0],
        [0, 0],
        [0, 0],
    ]
    figure6 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]
    assert find_full_line(field6, figure6) == -1

    # --- Test Case 7: Single valid column at the far right ---
    field7 = [
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 0]
    ]
    figure7 = [
        [0, 1, 1],
        [1, 0, 1],
        [0, 1, 0]
    ]


# ============================================================
# 7. Memory Allocation
# ============================================================
"""
Problem: Memory Allocation

Memory is represented as an array of bits (0 or 1).
Every 8 bits form a block.

Queries:
- (0, k): Allocate k consecutive 0s at the START of a block.
          Return starting index or -1 if impossible.
- (1, x): Release the x-th successful allocation.
          Return the size of memory released.

Released memory becomes available again.
"""


def memory_allocation(mem, queries):
    # TODO: implement
    pass


def test_memory_allocation():
    mem = [0]*16
    queries = [(0, 3), (0, 2), (1, 1)]
    assert memory_allocation(mem, queries) == [0, 8, 3]


# ============================================================
# 8. Phone Number to Words Converter
# ============================================================
"""
Problem: Phone Number to Words Converter

Given a string of digits (2–9), return all valid words
that can be formed using the phone keypad mapping.

Only return words that exist in the provided dictionary.
"""


def build_options(digits, dictionary):
    # TODO: implement
    pass


def test_build_options():
    dictionary = {"dog", "fish", "cat"}
    assert build_options("364", dictionary) == ["dog"]
    assert build_options("", dictionary) == []


# ============================================================
# 9. String Digit Removal for Lexicographic Order
# ============================================================
"""
Problem: String Digit Removal for Lexicographic Order

Given strings s and t (letters and digits),
count how many ways EXACTLY ONE digit can be removed
(from either string) such that:

    s < t (lexicographically) AFTER removal

Digits are lexicographically smaller than letters.
"""


def removeOneDigit(s, t):
    # TODO: implement
    pass


def test_removeOneDigit():
    assert removeOneDigit("ab12c", "1zz456") == 1
    assert removeOneDigit("ab12c", "ab24z") == 3


# ============================================================
# Test Runner
# ============================================================

def run_tests():
    tests = [
        test_array_mutation,
        test_pythagorean_triplets,
        test_first_valid_hand,
        test_char_cascade,
        test_count_valid_words,
        test_find_full_line,
        test_memory_allocation,
        test_build_options,
        test_removeOneDigit,
    ]

    passed = 0
    for test in tests:
        try:
            test()
            print(f"[PASS] {test.__name__}\n")
            passed += 1
        except AssertionError:
            case = f" — case: {CURRENT_TEST_CASE}" if CURRENT_TEST_CASE else ""
            print(f"\n[FAIL] {test.__name__}{case}\n")

    print(f"\nPassed {passed}/{len(tests)} tests")


if __name__ == "__main__":
    run_tests()
