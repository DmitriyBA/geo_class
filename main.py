import pandas as pd

data = pd.read_csv('/content/keywords.csv')

centr = []
sev_zapad = []
dal_vostok = []

geo_data = {}

centr_dict = []
sev_zapad_dict = []
dal_vostok_dict = []

region_column = [0 for i in range(100000)]

with open('/content/центр.txt', 'r') as fl:
  for line in fl:
    centr.append(line[:len(line)-1].lower())

with open('/content/севзапад.txt', 'r') as fl:
  for line in fl:
    sev_zapad.append(line[:len(line)-1].lower())

with open('/content/дальнийвосток.txt', 'r') as fl:
  for line in fl:
    dal_vostok.append(line[:len(line)-1].lower())

count = 0 #счетчик добавления в результирующий набор

for item in range(len(data['keyword'])):
  city_array = data['keyword'][item].lower().split()
  for city in city_array:
    if city in centr:
      count += 1
      centr_dict.append(city)
      region_column[item] = city
    elif city in sev_zapad:
      count += 1
      sev_zapad_dict.append(city)
      region_column[item] = city
    elif city in dal_vostok:
      count += 1
      dal_vostok_dict.append(city)
      region_column[item] = city
  if count != 1:
    region_column[item] = 'undefined'
  else:
    count = 0


geo_data = {
    'Центр': centr_dict,
    'Северо-Запад': sev_zapad_dict,
    'Дальний Восток': dal_vostok_dict
}

data['region'] = region_column
data.head(100)