# Diagnostic Problem 1
# Rex Ocampo
# Could regex be used here?
def msgcompress(string):
    compress = []
    curr_char = string[0]
    count = 1

    for i in range(1, len(string)):
        if string[i] == curr_char:  # comparing the char ahead of curr char
            count += 1
        else:
            if count > 1:
                compress.append(curr_char + str(count))
            else:
                compress.append(curr_char)
            curr_char = string[i]
            count = 1
    # handling last char in the string
    if count > 1:
        compress.append(curr_char + str(count))
    else:
        compress.append(curr_char)

    return ''.join(compress)

string = "abcaaabbb"
print("Uncompressed: " + string)
print("Compressed: " + msgcompress(string))

string = "abbccc"
print("Uncompressed: " + string)
print("Compressed: " + msgcompress(string))

string = "aaaa"
print("Uncompressed: " + string)
print("Compressed: " + msgcompress(string))

string = "bb"
print("Uncompressed: " + string)
print("Compressed: " + msgcompress(string))