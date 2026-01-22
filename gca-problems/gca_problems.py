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
    print(f'\n\nTesting first_valid_hand: {cards}')
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
    # How should we approach? 
    # ---> I dont think we should look at every possible combination of cards until we find 3 
    # What conditions cause updates? 
    # ---> 
    # will keep track of seen cards
    tups = []
    d = {}
    for i in range(len(cards)):

        c = cards[i]
        letters = [char for char in c if char.isalpha()]
        count = len(letters)
        val = set(letters).pop()
        suit = [char for char in c if not char.isalpha()].pop()

        d[i] = (count, suit, val)
        tups.append((count, suit, val))
    """
    Now that we have a hashmap of each strings position in the cards and its properties,
    whats next?

    hand = []
    for i, props in d.items():
        # base case
        if len(hand) == 3: return hand
         
        if these props are the same as every element in the hand,
        --> add the props to the hand

        if these props are distinct from every element in the hand, 
        --> add the props to the hand 

        else, 
        --> do nothing
    """
    def is_valid(hand): 
        # validate hand under constraints
        # print(hand[0])
        chars = list(hand[0]) + list(hand[1]) + list(hand[2])
        print(list(hand[0]))
        all_chars = set(chars)
        print(chars)
        if (len(set(hand)) == 1):
            # print("Valid triplet found:", hand)
            return True
        elif len(set(chars)) == len(chars):
            return True
        return False
        
    # Brute force
    for i in range(len(d)):
        for j in range(i + 1, len(d)): 
            for k in range(j + 1, len(d)):
                # print(d[i], d[j], d[k])
                if is_valid([d[i], d[j], d[k]]):
                    return [cards[i], cards[j], cards[k]]
    return None
    """
    Optimal approach attempt

    hand = []
    tups = []
    e = 0
    for i, props in d.items():
        print(e)
        # print("Current props:", props)
        # base case
        if len(hand) == 3:
            print(len(tups))
            print(len(set(tups)))
            # if every element in the hand of 3 is not distinct or every element is not identical
            # --> how should we reset state and continue? 

            # This says "if 3 cards are in the hand and they are all distinct"
            if len(tups) == len(set(tups)):
                print()
                return hand
            # This says "if 3 cards are in the hand and they are all the same"
            elif len(set(tups)) == 1:
                print()
                return hand

        # how do we reset the state properly??? 
        # something that allows us to try every possible combination

        unique = set(tups)
        if len(unique) == 1 and props in unique: 
            print("Same as every element")
            print(f'Adding {props} to hand')
            tups.append(props)
            hand.append(cards[i])
        if props not in tups:
            print(props)
            print(tups)
            print("Distinct from all other props")
            print(f'Adding {props} to hand')
            tups.append(props)
            hand.append(cards[i])
        e += 1
    return None
    """

    


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

    # case 3: duplicates early, valid later
    CURRENT_TEST_CASE = "duplicates early, valid later"
    cards = ["+AA", "+AA", "-AA", "+B", "-C", "=D"]
    res = first_valid_hand(cards)
    assert res == ["+B", "-C", "=D"]

    # case 4: no valid hand
    CURRENT_TEST_CASE = "no valid hand"
    cards = ["+AA", "-AA", "=AA", "+AB", "-AB"]
    res = first_valid_hand(cards)
    assert res is None

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

    # case 7: valid hand appears later, mixed lengths
    CURRENT_TEST_CASE = "valid hand appears later, mixed lengths"
    cards = ["+A", "+A", "-AA", "+B", "=CC", "-D"]
    res = first_valid_hand(cards)
    assert res == ["+B", "=CC", "-D"]

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
    # TODO: implement
    pass


def test_char_cascade():
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
    # TODO: implement
    pass


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


def find_full_line(field, figure):
    # TODO: implement
    pass


def test_find_full_line():
    field = [
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 0]
    ]
    figure = [
        [1, 1, 1],
        [0, 1, 0],
        [0, 1, 0]
    ]
    assert find_full_line(field, figure) in [0, 1, -1]


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
