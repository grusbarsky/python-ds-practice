def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_frequency = {}
    for char in phrase:
        frequency = phrase.count(char)
        letter_frequency[f"{char}"]=f"{frequency}"
    print(f"{letter_frequency}")