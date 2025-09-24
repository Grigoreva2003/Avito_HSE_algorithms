def is_palindrome(num: int, length: int) -> bool:
    while num != 0:
        first = num // 10 ** length         # extract first digit
        last = num % 10                     # extract last digit
        if first == last:
            num %= 10 ** length             # remove first digit
            num //= 10                      # remove last digit
            length -= 2                     # reduce length for future calculations
        else:
            return False
    return True

if __name__ == "__main__":
    num = int(input())
    length = len(str(num)) - 1

    print(is_palindrome(num, length))
