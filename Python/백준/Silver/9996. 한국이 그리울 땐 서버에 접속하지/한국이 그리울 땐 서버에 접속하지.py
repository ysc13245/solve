n=int(input())
pattern = input().split("*")
for _ in range(n):
  case=input()
  if case.startswith(pattern[0]):
    if case[len(pattern[0]):].endswith(pattern[1]):
      print("DA")
    else:
      print("NE")
  else:
    print("NE")