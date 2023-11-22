def rotThirteen(s):
    result = ""
    for v in s:
        if v.isalpha():
            ascii_offset = 65 if v.isupper() else 97
            result += chr((ord(v) - ascii_offset + 13) % 26 + ascii_offset)
        else:
            result += v
    return result
