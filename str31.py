N, M = map(int, input().split(' '))
count = 1
for _ in range(N // 2):
    print(f"{'.|.' * count:-^{M}}")
    count += 2
print(f"{'WELCOME':-^{M}}")
for _ in range(N // 2):
    count -= 2
    print(f"{'.|.' * count:-^{M}}")