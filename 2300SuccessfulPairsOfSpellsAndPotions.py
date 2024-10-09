class Solution:
    def successfulPairs(self, spells, potions, success: int):
        """
        Finds the number of successful pairs for each spell.

        :param spells: The list of spells.
        :type spells: list
        :param potions: The list of potions.
        :type potions: list
        :param success: The minimum number of successful spells.
        :type success: int
        :return: The number of successful pairs for each spell.
        :rtype: list
        """
        # Sort the potions in ascending order
        potions.sort()
        result = []

        # Iterate over each spell
        for spell in spells:
            # Initialize the variables
            low = 0
            high = len(potions) - 1
            count = 0
            
            # Use binary search to find the number of successful pairs
            while low <= high:
                # Calculate the middle index
                mid = low + (high - low) // 2

                # If the potion is sufficient to get the desired success
                if potions[mid] * spell >= success:
                    # Update the count
                    count = len(potions) - mid
                    # Move the right pointer to the left
                    high = mid - 1
                else:
                    # Move the left pointer to the right
                    low = mid + 1

            # Append the result
            result.append(count)

        return result
