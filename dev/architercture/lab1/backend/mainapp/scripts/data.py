import random
from mainapp.models import Monowheel

def run():
    brands = ['BrandA', 'BrandB', 'BrandC', 'BrandD', 'BrandE']
    models = ['ModelX', 'ModelY', 'ModelZ', 'ModelW', 'ModelV']
    entries = []

    for i in range(1000):
        entry = Monowheel(
            brand=random.choice(brands),
            model=random.choice(models),
            max_speed=round(random.uniform(10, 50), 2),  # Скорость от 10 до 50 км/ч
            range=round(random.uniform(20, 100), 2),     # Дальность от 20 до 100 км
            price=round(random.uniform(100, 1000), 2)     # Цена от 100 до 1000
        )
        entries.append(entry)

    Monowheel.objects.bulk_create(entries)
    print("Successfully inserted 1000 entries")
