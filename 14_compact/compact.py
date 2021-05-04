def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    new_lst = [element for element in lst if type(element) == int or type(element) == str and element != '']
    print(new_lst)
