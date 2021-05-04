def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    number_frequency = {}
    for num in nums:
        number_frequency[num] = nums.count(num)
    max_number = max(number_frequency.values())
    for number, frequency in number_frequency.items():
        if frequency == max_number:
            print(number)
    
