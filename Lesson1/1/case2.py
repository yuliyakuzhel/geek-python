user_input = input("Введите время в секундах")

user_second = int(user_input)
Hours = user_second // 3600
Minutes = (user_second % 3600) // 60
Seconds = (user_second % 3600) % 60
print(f"{Hours:>02}:{Minutes:>02}:{Seconds:>02}")
