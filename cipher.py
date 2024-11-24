import random
char_to_morse_map = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': 'x'
}

morse_to_char_map = {v: k for k, v in char_to_morse_map.items()}

morse_to_num_map= {
    '.': ['0', '1', '2'],
    '-': ['3', '4', '5'],
    'x': ['6', '7', '8', '9'],
}

num_to_morse_map = {num: char for char, nums in morse_to_num_map.items() for num in nums}

test_string = "This is a test string"

def encode_pollux(text):
    return morse_to_num(text_to_morse(text))

def decode_pollux(nums):
    return morse_to_text(num_to_morse(nums))

def text_to_morse(text):
    morse = ''
    for char in text.upper():
        if char in char_to_morse_map:
            morse += char_to_morse_map[char] + 'x'
    return morse

def morse_to_text(morse):
    text = ''
    seg = ''
    for i in range(len(morse)):
        if morse[i] == 'x':
            if morse[i-1] == 'x':
                text += ' '
            else:
                text += morse_to_char_map[seg]
                seg = ''
        else:
            seg += morse[i]
    return text

def morse_to_num(morse):
    pollux = ''
    for char in morse:
        pollux += str(random.choice(morse_to_num_map[char]))
    return pollux

def num_to_morse(nums):
    morse = ''
    for num in nums:
        morse += num_to_morse_map[num]
    return morse

print(test_string)
print("Encrypted Text:")
test = encode_pollux(test_string)
print(test)
print("Decoded Text:")
print(decode_pollux(test))
