def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    word_list = phrase.split(" ")
    title_list = []
    for word in word_list:
        print(word)
        title_list.append(word.replace(word[0], word[0].upper(), 1))
    phrase = " ".join(title_list)
    return phrase
    
