def solution():
    import sys

    input = sys.stdin.readline
    print = sys.stdout.write
    t=0

    while True:

        t += 1
        o = input()
        r = input()

        if o==r=="END\n":
            break

        print(f"Case {t}: ")

        if sorted(o)==sorted(r):
            print("same\n")
        else:
            print("different\n")



solution()
