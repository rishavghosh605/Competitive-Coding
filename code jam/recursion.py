def solve(a, b):
  m = (a + b) // 2
  print(m,a,b)
  s = input()
  if s == "CORRECT":
    return
  elif s == "TOO_SMALL":
    a = m + 1
  else:
    b = m - 1
  solve(a, b)

T = int(input())
a, b = map(int, input().split())
for i in range(T):
  print('i',i)
  solve(a + 1, b)
