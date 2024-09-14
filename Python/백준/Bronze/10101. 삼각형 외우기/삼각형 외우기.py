seq = list(map(int, open(0).readlines()))
sseq = set(seq)
if sseq == {60}:
    print("Equilateral")
else:
    if sum(seq) != 180:
        print("Error")
    elif len(sseq) == 2:
        print("Isosceles")
    elif len(sseq) == 3:
        print("Scalene")
