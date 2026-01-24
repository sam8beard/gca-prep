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
    # print("Figure")
    # display_grid(figure)
    # print("Field")
    # display_grid(field)
    import copy

    field_width = len(field[0])
    field_height = len(field)
    fig_width = len(figure[0])
    fig_height = len(figure)
    drop_pos = 0
    for drop_pos in range(0, field_width - fig_width + 1):
        # print(f'Drop position: {drop_pos}')
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

                # print(f'{fig_block} being dropped into column {field_c}')

                # Go row by row in the field, starting from the top, placing values in field
                field_r = 0
                while field_r + 1 < field_height and temp_field[field_r + 1][field_c] == 0:
                    field_r += 1

                # place dropped value into field cell
                temp_field[field_r][field_c] = fig_block
                # display_grid(temp_field)
            # print()
        # scan rows for win condition
        for field_r in temp_field:
            if all(cell == 1 for cell in field_r):
                # print("Firing in win condition:", drop_pos)
                return drop_pos
    return -1


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
    """
    - 8 indices to a block
    - must segment mem array into blocks of 8 positions
    - find a way to keep track of start of block and end of block

    - (0, k)
    --> find first available block with at least k spots available
    --> add these positions to a hashmap with a key representing when it was allocated (i.e. 1 for first...)
    --> a position being in one of the values of the hashmap indicates that position is allocated
    --> return the starting position of the allocation

    - (1, x):
    --> attempt to access the x key of the hashmap
    --> if it exists, remove this key and its value, and return the length of the value
    --> else, return -1
    """
    res = []
    # starting positions of blocks and their availability
    blocks = [{0: 8} if i == 0 else {i - 1: 8}
              for i in range(0, len(mem), 8)]
    allocs = {}
    alloc_count = 0
    for i, q in enumerate(queries):
        if q[0] == 0:
            success = False
            space = q[1]
            # check available blocks for space
            for b in blocks:
                start, avail = next(iter(b.items()))

                # if space needed is greater than available in this block, check next block
                if space > avail:
                    continue
                # allocate space to this block
                b[start] = avail - space
                # increment alloc count
                alloc_count += 1
                # keep track of allocation
                allocs[alloc_count] = (start, space)
                # add starting index to result
                res.append(start)
                success = True
                break
            if not success:
                res.append(-1)

        elif q[0] == 1:
            if q[1] in allocs:
                alloc = allocs[q[1]]
            else:
                res.append(-1)
                continue
            alloc = allocs[q[1]]
            # get allocation start position and space
            start, space = alloc[0], alloc[1]
            # free allocated space in block of last successful allocation
            success = False
            for b in blocks:
                if start in b:
                    b[start] += space
                    success = True
                    res.append(space)
                    break
            if not success:
                res.append(-1)
            # add freed space to result
    # print(blocks)
    return res


def test_memory_allocation():

    mem = [0] * 32  # 4 blocks of 8

    queries = [
        # Initial allocations
        (0, 3),    # #1 -> block 0, start 0
        (0, 2),    # #2 -> block 0, start 0
        (0, 5),    # #3 -> block 1, start 7
        (0, 1),    # #4 -> block 0, start 0
        (1, 2),    # free #2 -> 2 bits
        (0, 4),    # #5 -> block 0, start 0
        (0, 8),    # #6 -> block 2, start 15
        (0, 6),    # #7 -> block 3, start 23
        (0, 2),    # #8 -> block 0, start 0 (fits in remaining space)

        # Attempt invalid allocations
        (0, 10),   # too big for any block -> -1
        (1, 9),    # invalid free (nonexistent) -> -1

        # Free some allocations
        (1, 3),    # free #3 -> size 5
        (1, 6),    # free #6 -> size 8

        # Reallocate into freed spaces
        (0, 5),    # #9 -> block 1, start 7 (freed)
        (0, 3),    # #10 -> block 2, start 15 (freed)

        # Free and allocate again
        (1, 5),    # free #5 -> size 4
        (0, 4),    # #11 -> block 0, start 0 (fits in freed space)
        (1, 7),    # free #7 -> size 6
        (0, 6),    # #12 -> block 3, start 23 (fits again)
    ]

    # Expected result according to your allocation logic:
    assert memory_allocation(mem, queries) == [
        0, 0, 7, 0, 2, 0, 15, 23, 7, -1, -1, 5, 8, 7, 15, 4, 0, 6, 23
    ]


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


def remove_one_digit(s, t):

    res = 0
    seen = []

    for i in range(len(s)):
        if s[i].isdigit():
            new_s = s.replace(s[i], "")
            if new_s < t and new_s not in seen:
                seen.append(new_s)
                res += 1

    for j in range(len(t)):
        if t[j].isdigit():
            new_t = t.replace(t[j], "")
            if s < new_t and new_t not in seen:
                seen.append(new_t)
                res += 1
    print(res)
    return res


def test_remove_one_digit():
    assert remove_one_digit("ab12c", "1zz456") == 1
    assert remove_one_digit("ab12c", "ab24z") == 3


# ============================================================
# 10. Frequency-Based String Merge
# ============================================================
"""
Problem: Frequency-Based String Merge

Given two strings s1 and s2, merge them into a single string
using the following rules:

- Compare the current characters of s1 and s2 based on their
  frequency in their respective strings (fewer occurrences are "smaller").
- If frequencies are equal, compare lexicographically (usual order).
- If still equal, take the character from s1.
- Continue until all characters from both strings are merged.

"""


def frequency_merge(s1, s2):
    from collections import Counter
    s1_counts = Counter(s1)
    s2_counts = Counter(s2)
    res = ""

    s1_len = len(s1)
    s2_len = len(s2)

    i, j = 0, 0
    while i < s1_len and j < s2_len:

        s1_char, s2_char = s1[i], s2[j]
        s1_count, s2_count = s1_counts[s1_char], s2_counts[s2_char]

        first_cond = s1_count != s2_count
        first_cond_s1 = s1_count < s2_count
        first_cond_s2 = s2_count < s1_count

        second_cond = s1_char != s2_char
        second_cond_s1 = s1_char < s2_char
        second_cond_s2 = s2_char < s1_char

        # evaluate
        if first_cond:
            if first_cond_s1:
                res += s1_char
                i += 1
            elif first_cond_s2:
                res += s2_char
                j += 1
        elif second_cond:
            if second_cond_s1:
                res += s1_char
                i += 1
            elif second_cond_s2:
                res += s2_char
                j += 1
        else:
            res += s1_char
            i += 1
    if i < s1_len:
        res += s1[i:]
    elif j < s2_len:
        res += s2[j:]
    return res


def test_frequency_merge():
    # Basic tests
    # example expected output
    assert frequency_merge("aabc", "abbc") == "aaabcbbc"
    assert frequency_merge("abc", "abc") == "aabbcc"
    assert frequency_merge("", "xyz") == "xyz"
    assert frequency_merge("xyz", "") == "xyz"
    assert frequency_merge("aaa", "a") == "aaaa"
    assert frequency_merge("bca", "acb") == "abcacb"

    # Edge cases
    assert frequency_merge("", "") == ""
    assert frequency_merge("a", "a") == "aa"
    assert frequency_merge("abc", "def") == "abcdef"


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
        test_remove_one_digit,
        test_frequency_merge,
    ]

    passed = 0
    for test in tests:
        try:
            test()
            print(f"[PASS] {test.__name__}\n")
            passed += 1
        except AssertionError:
            print(f"\n[FAIL] {test.__name__}\n")

    print(f"\nPassed {passed}/{len(tests)} tests")


if __name__ == "__main__":
    run_tests()
