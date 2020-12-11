imax = int(input("Сколько всего предметов: "))
spisok = [[], [], [], []]
cluchs = []
i = 1
while i <= imax:
    meanings = [
        (i, {"Название": input("Введите название: "), "цена": input("Введите цену: "),
         "количество": input("Введите колличество:"), "ед": input("Введите единицу измерения: ")}),
             ]
    for meaning in meanings:
        i = meaning[0]
        i += 1
        b = meaning[1]
        spisok[0].append(b['Название'])
        spisok[1].append(b['цена'])
        spisok[2].append(b['количество'])
        if b['ед'] not in spisok[3]:
            spisok[3].append(b['ед'])
finish = dict.fromkeys(['Название'], spisok[0])
finish['цена'] = spisok[1]
finish['количество'] = spisok[2]
finish['eд'] = spisok[3]
print(finish)



























