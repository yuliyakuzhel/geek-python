user_input = input("Введите целое положительное число")
if not user_input.isdigit():
    print("Неверный формат числа")
    exit()
Number = int(user_input)
max = -1

while Number > 10:
    present = Number % 10
    Number //= 10
    if present > max:
        max = present

print("Максимальная цифра в числе", max)
