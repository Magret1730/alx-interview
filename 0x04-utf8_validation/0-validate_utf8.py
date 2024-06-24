#!/usr/bin/env python3
""" Task 0 """


def validUTF8(data):
    """
    method that determines if a given data set represents a valid UTF-8
    encoding
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading bits of each byte
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Iterate through each byte in the data
    for byte in data:
        # If this is the start of a new character
        if num_bytes == 0:
            # Determine the number of bytes
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # 1 byte characters (0xxxxxxx) or invalid (10xxxxxx)
            if num_bytes == 0:
                continue

            # UTF-8 characters can be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte is a continuation byte (10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes remaining in the current character
        num_bytes -= 1

    # If num_bytes is not zero, then the last character is incomplete
    return num_bytes == 0
