"""
Approach - 1: 
 Using Escape Character:
 Time Complexity: O(n)
 Space Complexity: O(k)
"""
def encode_strings_1(input_strings):
    encoded_string = ""
    for s in input_strings:
        encoded_string += s.replace("/", "//") + "/:"
    return encoded_string

def decode_strings_1(s):
    i = 0
    decoded_strings = []
    current_string = ""
    while(i < len(s)):
        if(s[i:i+2] == "/:"):
            decoded_strings.append(current_string)
            current_string = ""
            i += 2
        elif(s[i:i+2] == "//"):
            current_string += '/'
            i += 2
        else:
            current_string += s[i]
            i += 1
    return decoded_strings

"""
Approach - 2: 
 Using Chunked Tranfer (Calculating length of each string and using delimiter along with it):
 Time Complexity: O(n)
 Space Complexity: O(k)
"""
def encode_strings_2(input_strings):
    encoded_string = ""
    for s in input_strings:
        encoded_string += str(len(s)) + "/:" + s
    return encoded_string

def decode_strings_2(s):
    decoded_strings = []
    i = 0
    while(i < len(s)):
        j = i 
        while(s[j:j+2] != "/:"):
            j += 1
        length = int(s[j-1])
        decoded_strings.append(s[j+2:j+2+length])
        i = j+2+length
    return decoded_strings
 
input_strings = ["He/llo","Wo/:rld"]
print("Given String: ", input_strings)

# 1st Approach:
encoded_string = encode_strings_1(input_strings)
print("Encoded String: ", encoded_string)
print("Decoded String: ", decode_strings_1(encoded_string))

# Second Approach:
encoded_string = encode_strings_2(input_strings)
print("Encoded String: ", encoded_string)
print("Decoded String: ", decode_strings_2(encoded_string))
