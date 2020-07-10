def has_negatives(a):
    result = []
    cache = {}
    for num in a: 
        new_num = str(num)
        if new_num.startswith("-"):
            if num not in cache:
                cache[num] = 1

    keys = list(cache.keys())
    new_keys = []
    for key in keys:
        new_keys.append(-key)

    for nk in new_keys:
        if nk in a:
            result.append(nk)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
