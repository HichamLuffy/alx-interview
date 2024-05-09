#!/usr/bin/python3
""" Validate UTF8 encoding """


def validUTF8(data):
    """ Validate UTF8 encoding """
    def bytes_needed(first_byte):
        # Count the number of leading 1s to determine the number of bytes needed
        if first_byte & 0b10000000 == 0:
            return 1
        count = 0
        mask = 0b10000000
        while mask & first_byte:
            count += 1
            mask >>= 1
        if count == 1 or count > 4:
            return -1
        return count

    i = 0
    while i < len(data):
        first_byte = data[i]
        needed = bytes_needed(first_byte)

        if needed == -1:
            return False
        if needed == 1:
            i += 1
            continue

        if i + needed > len(data):
            return False

        for j in range(1, needed):
            if not (data[i + j] & 0b11000000 == 0b10000000):
                return False

        i += needed

    return True
