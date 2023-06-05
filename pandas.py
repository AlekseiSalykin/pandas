import pandas as pd

df = pd.read_excel('films.xlsx', sheet_name='Sheet1')

print("1-Вывод таблицы\n")
print(df)

print("2 вывод первых 5 элементов таблицы\n")
print(df.head(5))

print("3 вывод последних 5 элементов таблицы\n")
print(df.tail(5))

print("4 использовать функцию describe()\n")
print(df["Название"].describe())

print("5 считывание значения конкретной ячейки\n")
print(df["Актеры"].values[1])

print("6 фильтрация строк по диапазону индекса\n")
print(df.filter(items=range(5,10), axis=0))

print("7 фильтрация набора данных по какому-либо условию\n")
print(df[df["Жанр"] == "боевик"])

print("8 работа с пропущенными значениями\n")
print("имеет пустые столбцы:{}".format(df.isnull().values.any()))
print(df.isnull())

print("9 создание нового поля вычисленного на основе значений других полей:\n")
print("9.1 через выражение на базе имеющихся колонок\n")
df["Режиссура"] = (df["Режиссер"]+df["Страна"])
print(df["Режиссура"])

print(".9.2 через DataFrame.apply\n")
df['Год'] = df['Год'].apply((lambda year: year + 50))
print(df['Год'])

print("9.3 через Series.apply\n")
print(df.apply(lambda x: pd.Series([1, 2], index=['№', 'Название'])))

print("10 сортировка по какому-либо из полей\n")
df.sort_values(by=["Жанр"], ignore_index=True, inplace=True)
print(df["Жанр"])

print("11 вычислить несколько статистик по колонкам")
print("Частота фильмов из США(в %):\n")
usa = df["Страна"].apply(lambda films: films=="США")
print(usa.value_counts(normalize=True) * 100)

print("12 .value_counts()\n")
print("Количество актеров:{}".format(df["Актеры"].value_counts()))

print("13 Вывод уникальных значений колонки через .unique()\n")
print(df["Страна"].unique())

print("14 Удалите текущий индекс и создайте новый индекс на базе новой колонки\n")
df.reset_index(drop=True, inplace=True)
df.set_index('№', inplace=True)
print(df)