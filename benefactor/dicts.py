def merge_two_dicts(a, b):
    c = a.copy()  # make a copy of a
    c.update(b)  # modify keys and values of a with the ones from b
    return c
