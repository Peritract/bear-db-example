"""An extremely hacky script that generates a bunch of fake bear attacks."""

from csv import DictWriter
from random import choice
from datetime import datetime, timedelta

if __name__ == "__main__":

    rows = []
    for i in range(10000):
        attack = {
            "bear_type": choice(['polar','grizzly','spectral','brown',
                                 'black','deep','cave','mutant']),
            "location": choice(['rural','urban','suburban','semi-rural','astral','aquatic']),
            "created_at": datetime.now() - timedelta(days=choice(range(1, 23)))
        }
        rows.append(attack)

    with open("attacks.csv", 'w', encoding="utf-8") as f:
        writer = DictWriter(f, fieldnames=["bear_type", "location", "created_at"])
        writer.writeheader()
        writer.writerows(rows)
