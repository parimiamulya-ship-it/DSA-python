name = "Ananya"

print("Length:", len(name))

for i in range(len(name)):
    print(f"Index {i}: {name[i]}")

    
    first = "Ananya"
second = "Karan"

# Traversal
print(f"Traversing '{first}': ", end="")
for char in first:
    print(char, end=" ")
print()

# Concatenation
full_team_name = first + " & " + second
print("Concatenated:", full_team_name)

# Comparison
if first < second:
    print(f"{first} comes before {second}")
else:
    print(f"{second} comes before {first}")


    def reverse_string(s):
    chars = list(s)
    left = 0
    right = len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)


def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


word = "madam"
print("Reversed:", reverse_string(word))

check1 = "racecar"
check2 = "hello"
print(f"{check1} is palindrome:", is_palindrome(check1))
print(f"{check2} is palindrome:", is_palindrome(check2))

def is_subsequence(smaller, larger):
    i = 0
    j = 0

    while i < len(smaller) and j < len(larger):
        if smaller[i] == larger[j]:
            i += 1
        j += 1

    return i == len(smaller)


word = "CARPET"

sub = word[1:4]
print("Substring (index 1 to 4):", sub)

print("Is 'CRT' a subsequence of 'CARPET'?", is_subsequence("CRT", word))
print("Is 'CRT' a substring of 'CARPET'?", "CRT" in word)

def is_valid_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


phrase = "A man, a plan, a canal: Panama"
print("Is valid palindrome:", is_valid_palindrome(phrase))

not_palindrome = "This is not one"
print("Is valid palindrome:", is_valid_palindrome(not_palindrome))



def longest_unique_substring(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


text = "abcabcbb"
print("Longest substring without repeats:", longest_unique_substring(text))

def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    counts = {}

    for c in s1:
        counts[c] = counts.get(c, 0) + 1
    for c in s2:
        counts[c] = counts.get(c, 0) - 1

    return all(count == 0 for count in counts.values())


def first_non_repeating_char(s):
    counts = {}

    for c in s:
        counts[c] = counts.get(c, 0) + 1

    for c in s:
        if counts[c] == 1:
            return c

    return None


print("Are 'listen' and 'silent' anagrams?", are_anagrams("listen", "silent"))

word = "swiss"
result = first_non_repeating_char(word)
print(f"First non-repeating character in '{word}':", result)