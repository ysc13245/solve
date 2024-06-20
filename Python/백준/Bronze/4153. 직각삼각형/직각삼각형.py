while True:
    s=input()
    if s=="0 0 0":
        break
    seq=sorted(list(map(int,s.split())))
    if seq[0]**2 + seq[1]**2 == seq[2]**2:
        print("right")
    else:
        print("wrong")