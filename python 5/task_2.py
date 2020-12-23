#2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
file = open(file="task2_less5.txt", encoding="UTF-8", mode="rt")
print(f"Колличество строк в вашем файле равно: {len(file.readlines())}.")
file = open(file="task2_less5.txt", encoding="UTF-8", mode="rt")

word_count = [len(line.split()) for line in file]
rez = ', '.join(str(el) for el in word_count)
print(f"Колличество слов в строке соответственно равно: {rez}.")

file.close()
