def all_unique(lst):
    return len(lst) == len(set(lst))


def chunk(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]


def compact(lst):
    return list(filter(None, lst))


def transpose(lst):
    transposed = zip(*lst)
    return list(transposed)


def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


def deep_flatten(xs):
    flat_list = []
    [flat_list.extend(deep_flatten(x)) for x in xs] if isinstance(xs, list) else flat_list.append(xs)
    return flat_list


def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)


def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]


def has_duplicates(lst):
    return len(lst) != len(set(lst))


def to_dictionary(keys, values):
    return dict(zip(keys, values))


def most_frequent(list):
    return max(set(list), key=list.count)
