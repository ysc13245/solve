def sol():

    print(*[" ".join(map(str,x)) for x in sorted([list(map(int, input().split())) for _ in range(int(input()))], key=lambda x: (x[1], x[0]))], sep="\n")
    
sol()