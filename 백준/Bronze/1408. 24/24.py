t1, t2 = map(lambda x: list(map(int, x.split(":"))), open(0).readlines())

sub = (t2[0] - t1[0]) * 3600 + (t2[1] - t1[1]) * 60 + t2[2] - t1[2]
sub += 0 if sub > 0 else 3600 * 24

print(f"{sub // 3600:02}:{sub % 3600 // 60:02}:{sub % 60:02}")
