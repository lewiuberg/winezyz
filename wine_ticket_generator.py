ticket_price = 10

contestants = {
    "Kristian": 100,
    "Geir Olav": 50,
    "Asgeir": 50,
    "Magrete": 100,
    "Trond": 50,
    "Ole-Johan": 100,
    "Andreas": 0,
    "Håkon": 100,
    "Trshant": 0,
    "Uti": 50,
    "Lewi": 100,
    "Rida": 0,
    "Ahmad": 30,
    "Svein Olaf": 0,
    "Ingrid": 0,
}

contestants_ticket_count = {}

for contestant_name, contestant_value in contestants.items():
    if contestant_value > 0:
        contestants_ticket_count[contestant_name] = (
            contestant_value // ticket_price
        )

for contestant in contestants_ticket_count:
    counter = 0
    for i in range(contestants_ticket_count[contestant]):
        counter += 1
        print(counter, contestant)

print(f"\nCurrent weeks total ticket sale: {sum(contestants.values()):.0f}")
