def find_first_repeating_character(s):
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
        
        if char_count[char] > 1:
            print(f"First repeating character is {char}, Memory adress : {id(char)}")
            return char, id(char)

find_first_repeating_character("Hello")

