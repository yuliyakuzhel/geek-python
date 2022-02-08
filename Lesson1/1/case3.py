user_input = input("Введите число")
Number = int(user_input)
Count = 0
Temp_Number = Number
while Temp_Number:
    Temp_Number //= 10
    Count += 1
First_level = (10 ** Count) + 1
Second_level = (10 ** (Count * 2)) + First_level
result = Number + (Number * First_level) + (Number * Second_level)
print("Сумма чисел", result)
