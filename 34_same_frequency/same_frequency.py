def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_frequency = {}
    num2_frequency = {}
    num1 = str(num1)
    num2 = str(num2)

    for num in num1:
        num1_frequency[num] = num1.count(num)

    for num in num2:
        num2_frequency[num] = num2.count(num)

    for name1 in num1_frequency.keys():
        num1_value = num1_frequency[name1]
        if name1 in num2_frequency:
            num2_value = num2_frequency[name1]
            if num1_value != num2_value:
                return False
        else:
            return False
    return True
                
