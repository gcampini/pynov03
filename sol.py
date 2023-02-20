import csv
import json
import os
import shutil
from pathlib import Path

from PIL import Image

# 1
with open('ldg', 'r') as f:
    data = f.read()
    data = json.loads(data)
    length = len(data)
    print(length)

# 2
with open('bnlc', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)
    print(len(rows))

# 3
with open('ldg', 'r') as f:
    data = f.read()
    data = json.loads(data)
    with open('ldg.json', 'w') as destination:
        json.dump(data, destination, indent=4)

# 4
# Transformer le fichier ldg (JSON) en CSV.

with open('ldg', 'r') as f:
    data = f.read()
    data = json.loads(data)
    with open('ldg.csv', 'w') as destination:
        writer = csv.writer(destination)
        headers = ['commune', 'libelle', 'x', 'y']
        writer.writerow(headers)
        for i in range(len(data)):
            item = data[i]['fields']
            fields = [
                item['commune'],
                item['libelle'],
                item['geo_shape']['coordinates'][0],
                item['geo_shape']['coordinates'][1]
            ]
            writer.writerow(fields)

# 5
clients = os.listdir(Path('data'))
with open('transactions.csv', 'w') as destination:
    writer = csv.writer(destination)
    headers = ['client', 'date', 'item', 'price', 'quantity']
    writer.writerow(headers)
    for client in clients:
        path = Path('data') / Path(str(client))
        dates = os.listdir(path)
        for date in dates:
            path = Path('data') / Path(str(client)) / Path(str(date))
            files = os.listdir(path)
            for file in files:
                with open(path / Path(str(file)), 'r') as f:
                    data = f.read()
                    data = json.loads(data)
                    fields = [client, date, data['item'], data['price'], data['quantity']]
                    writer.writerow(fields)
with open('transactions.csv', 'r') as destination:
    reader = csv.reader(destination)
    rows = list(reader)
    print(f"Number of transactions: {len(rows)}")

# 1
# Donner la moyenne des dimensions des images.

base = Path('images')

files = os.listdir(base)
total = 0
for file in files:
    path = base / Path(str(file))
    image = Image.open(path)
    width, height = image.size
    total += width + height
average = total / len(files) / 2
print(f"Average dimensions: {average} pixels")
