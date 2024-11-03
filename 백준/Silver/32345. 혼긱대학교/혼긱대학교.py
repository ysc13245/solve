import math
import sys

input = sys.stdin.readline
print = sys.stdout.write
vowel = {"a", "i", "e", "o", "u"}

for _ in range(int(input())):
    s = input()
    vowel_idx = [i for i, c in enumerate(s) if c in vowel]
    print(
        str(
            math.prod(
                (
                    [
                        (vowel_idx[i] - vowel_idx[i - 1]) % (10**9 + 7)
                        for i in range(1, len(vowel_idx))
                    ]
                )
            )
            % (10**9 + 7)
        )
        + "\n"
        if vowel_idx
        else "-1\n"
    )
