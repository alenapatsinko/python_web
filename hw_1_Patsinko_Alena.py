line = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"
print(f'Шаг 1 - Посчитать количество символов = {len(line)}')
print(f'Шаг 2 - Развернуть строку: {line[::-1]}')
print(f'Шаг 3 - Сделать каждое слово с большой буквы: {line.title()}')
print(f'Шаг 4 - Сделать весь текст прописными буквами: {line.upper()}')
print(f'Шаг 5 - Найти число вхождений "нд" в строку = {line.count("нд")}, "ам" = {line.count("ам")}, "о" = {line.count("о")}')
print(f'Шаг 6.1 - Заменить "собака" на "кот": {line.replace("собака","кот")}')
print(f'Шаг 6.2 - Вывести второе предложение: {line[int(line.index("."))+1:int(line.rindex("."))+1:]}')
print(f'Шаг 6.3 - Добавить "и кот" после слова собака: {line[:line.index("—"):] + "и кот " + line[line.index("—")::]}')
print(f'Шаг 6.4 - Определить, состоит ли строка только из букв: {line.isalpha()}')
print(f'Шаг 6.5 - Все предложения начинать с новой строки и удалить пробелы в начале и конце строки: \
\n{line[:int(line.find("."))+1:].strip()}\n {line[int(line.find("."))+1:int(line.rfind("."))+1:].strip()}\n \
{line[int(line.rfind("."))+1::].strip()}')

line1 = ' '.join(line.split(" ")[::-1])
print(f'Шаг 7 - Развернуть предложение: {line1}')
print(f'Шаг 8 - Вывести в консоль исходную строку: {line}')