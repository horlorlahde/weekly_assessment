def isPalindrome(x: int) -> bool:
    if x < 0: 
        return False  # Return False instead of printing
    
    div = 1
    while x >= 10 * div:
        div *= 10

    while x:
        right = x % 10
        left = x // div

        if left != right:
            return False

        x = (x % div) // 10  # Remove leftmost and rightmost digits
        div = div / 100  # Adjust the divisor

    return True
