def lengthOfLastWord(s: str) -> int:
    """
    Returns the length of the last word in the given string.
    
    Parameters
    ----------
    s : str
        The string to find the last word in.
    
    Returns
    -------
    int
        The length of the last word in the given string.
    
    Examples
    --------
    >>> lengthOfLastWord("luffy is still joyboy")
    6
    """
    arr = s.split()
    return len(arr[len(arr) - 1])

print(lengthOfLastWord("luffy is still joyboy")) # 6