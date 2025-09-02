import random

kolmenumeroinen_koodi = [random.randint(0, 9) for _ in range(3)]
nelinumero_koodi = [random.randint(1, 6) for _ in range(4)]

print("Kolmenumeroinen koodi:", ''.join(map(str, kolmenumeroinen_koodi)))
print("Nelinumeroinen koodi:", ''.join(map(str, nelinumero_koodi)))


