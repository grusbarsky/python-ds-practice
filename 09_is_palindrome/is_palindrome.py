def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    san_phrase = phrase.lower().replace(" ", "")
    reverse_phrase = san_phrase[::-1]
    msg = "True" if (reverse_phrase) == san_phrase else "false"
    print(msg)
