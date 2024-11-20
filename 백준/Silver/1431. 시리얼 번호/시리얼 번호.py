def guitar_sort(guitar):
    return (
        len(guitar),
        sum(int(c) for c in guitar if c.isdigit()),
        [ord(c) for c in guitar],
    )


guitars = list(map(str.rstrip,open(0).readlines()))[1:]

print(*sorted(guitars, key=guitar_sort), sep="\n")
