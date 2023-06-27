def firstUniqChar(s):
    char_count = {}  # Hashmap to store character counts
    
    # Count the occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first unique character
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i

    # No unique character found
    return -1

# Test cases
s1 = "leetcode"
print(firstUniqChar(s1))  # Output: 0

s2 = "loveleetcode"
print(firstUniqChar(s2))  # Output: 2

s3 = "aabb"
print(firstUniqChar(s3))  # Output: -1
