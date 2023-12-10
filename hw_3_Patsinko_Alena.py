weight = int(input("Введите Ваш вес в килограммах = "))
height = float(input("Введите Ваш рост в метрах = "))
BMI = int(round(weight / height**2, 0))
print(f'Ваш индекс массы тела = {BMI}')
scale = ["="] * 24
step = BMI - 16
scale.insert(step, "|")
t = ''.join(scale)
print(f'16 {t} 40')