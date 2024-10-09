def guessNumber(n: int) -> int:
    """
    Guess the number that the picker is thinking of.

    The picker will give a hint about the number by calling the guess function.
    The guess function will return -1 if the picked number is lower than the
    guessed number, 1 if it is higher and 0 if it is equal.

    We use a binary search approach to guess the number in the minimum number
    of attempts.
    """
    low = 0
    high = n
    
    # While the range of possible numbers is not empty
    while low <= high:
        # Calculate the middle of the range
        mid = low + (high - low) // 2

        # Ask the picker if the number is higher or lower than the guessed
        # number
        result = guess(mid) # type: ignore
        print(mid)
        print(result)

        # If the picker said that the number is equal to the guessed number
        # then we have the answer
        if result == 0:
            return mid
        
        # If the picker said that the number is lower than the guessed number
        # then we can discard the upper half of the range
        elif result == -1:
            high = mid - 1
        
        # If the picker said that the number is higher than the guessed number
        # then we can discard the lower half of the range
        else:
            low = mid + 1
