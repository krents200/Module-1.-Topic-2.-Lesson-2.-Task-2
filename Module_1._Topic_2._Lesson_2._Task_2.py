print ("Введите количество чисел в массиве")
N = int(input())
Ai = []
if N >= 1 and N <= 100000:
    print("Введите числа внутри списка")
    for i in range(N):
        Ai.append(int(input()))
        if Ai[i] < 1 or Ai[i] > 10e9:
            print("Формат числа не соответствует условию")
            exit()
    temp = Ai[0]
    for i in range(len(Ai)-1, 0, -1):
        Ai[i] = Ai[i-1]
    Ai[-1] = temp
    print(Ai)
else:
    print("Формат количества чисел не соответствует условию")
    