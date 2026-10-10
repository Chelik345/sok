base_fee1 = input("Введите базовую стоимость первого тарифа: ")
base_fee2 = input("Введите базовую стоимость второго тарифа: ")
rate1 = input("Введите стоимость первого тарифа кв/ч: ")
rate2 = input("Введите стоимость второго тарифа кв/ч: ")
consumption = input("Введите, сколько электричества вы потребляете: ")
base_fee1 = int(base_fee1)
base_fee2 = int(base_fee2)
rate1 = int(rate1)
rate2 = int(rate2)
consumption = int(consumption)
no_base_fee1 = rate1 * consumption
no_base_fee2 = rate2 * consumption
final1 = no_base_fee1 + base_fee1
final2 = no_base_fee2 + base_fee2
print(f"Итог первого тарифа: {final1}")
print(f"Итог второго тарифа: {final2}")
if final1 > final2:
    print("Первый дороже")
else:
    print("Второй дороже или они равны")