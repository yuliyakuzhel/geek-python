revenue = int(input("Введите сумму выручки компании "))
costs = int(input("Введите сумму издержек компании "))

profit = revenue - costs

if profit:
    profitability = profit / revenue
    print(f"Прибыль = {profit}, рентабельность = {profitability}")

    workers_count = int(input("Укажите количество сотрудников "))

    profit_worker = profit / workers_count
    print(f"Прибыль на одного сотрудника = {profit_worker}")
else:
    print(f"Убыток = {profit}")
