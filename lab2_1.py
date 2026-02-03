import requests
import matplotlib.pyplot as plt
from collections import Counter


base_url = 'https://pokeapi.co/api/v2/'
limit = 8
url = f'{base_url}pokemon?limit={limit}&offset=0'

print("Загружаем список покемонов...")
response = requests.get(url)
if response.status_code != 200:
    print("Ошибка:", response.status_code)
    exit()

data_raw = response.json()
pokemon_list = data_raw['results']

data = []

for idx, pokemon in enumerate(pokemon_list, 1):
    pokemon_url = pokemon['url']
    resp = requests.get(pokemon_url)
    p = resp.json()

    stats_dict = {s['stat']['name']: s['base_stat'] for s in p['stats']}

    pokemon_data = {
        'id': p['id'],
        'name': p['name'].capitalize(),
        'height': p['height'],
        'weight': p['weight'],
        'hp': stats_dict.get('hp'),
        'attack': stats_dict.get('attack'),
        'defense': stats_dict.get('defense'),
        'speed': stats_dict.get('speed'),
        'types': [t['type']['name'] for t in p['types']]
        }

    data.append(pokemon_data)
    print(f"{idx:2d}) {pokemon_data['name']} загружен")

print(data)
print(f"\nВсего успешно загружено: {len(data)} покемонов\n")

#Подготовка списков
names = [p['name'] for p in data]
hp = [p['hp'] for p in data]
attack = [p['attack'] for p in data]
defense = [p['defense'] for p in data]
speed = [p['speed'] for p in data]
weight = [p['weight'] for p in data]

plt.style.use('bmh')

#Линейный график: здоровье по порядку
plt.figure(figsize=(10, 5))
plt.plot(range(1, len(data)+1), hp, marker='o', color='green')
plt.title('ЗДР покемонов по порядку')
plt.xlabel('Порядковый номер')
plt.ylabel('ЗДР')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

#Точечная диаграмма: Атака и Скорость
plt.figure(figsize=(10, 7))
plt.scatter(attack, speed, color='blue', s=60)

for i, name in enumerate(names):
    plt.text(
        attack[i],          # x-координата
        speed[i],           # y-координата
        name,               # текст
        fontsize=9,
        ha='right',         # выравнивание текста по горизонтали
        va='bottom',        # выравнивание по вертикали
        alpha=0.9
    )

plt.title('Атака vs Скорость')
plt.xlabel('Атака')
plt.ylabel('Скорость')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

#Столбчатая диаграмма: топ по атаке
top_n = 8
sorted_data = sorted(data, key=lambda x: x['attack'], reverse=True)[:top_n]
names_top = [p['name'] for p in sorted_data]
attack_top = [p['attack'] for p in sorted_data]

plt.figure(figsize=(10, 5))
plt.bar(names_top, attack_top, color='salmon')
plt.title(f'Топ-{top_n} по атаке')
plt.xlabel('Покемон')
plt.ylabel('Атака')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

#Горизонтальная столбчатая: топ по защите
sorted_def = sorted(data, key=lambda x: x['defense'], reverse=True)[:top_n]
names_def = [p['name'] for p in sorted_def]
defense_top = [p['defense'] for p in sorted_def]

plt.figure(figsize=(10, 5))
plt.barh(names_def, defense_top, color='skyblue')
plt.title(f'Топ-{top_n} по защите')
plt.xlabel('Защита')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()

#Гистограмма: распределение веса
plt.figure(figsize=(9, 6))
plt.hist(weight, bins=10, color='mediumpurple', edgecolor='white')
plt.title('Распределение веса покемонов')
plt.xlabel('Вес')
plt.ylabel('Количество')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

#Круговая диаграмма: типы
all_types = []
for p in data:
    all_types.extend(p['types'])

type_counts = Counter(all_types)
types_top = dict(type_counts.most_common(6))

plt.figure(figsize=(8, 8))
plt.pie(types_top.values(), labels=types_top.keys(), autopct='%1.0f%%',
        startangle=90, colors=plt.cm.Pastel1(range(len(types_top))))
plt.title('Распределение типов (топ-6)')
plt.axis('equal')
plt.tight_layout()
plt.show()

print("Все графики построены")