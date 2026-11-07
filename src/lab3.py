# ============================= УВАГА! =============================
# Цей файл містить ПРИКЛАД виконання лабораторної роботи.
# Ваше завдання - розробити ВЛАСНУ програму згідно з вашим варіантом.
#
# Ви можете використовувати цей код як зразок, але не копіювати його.
# Повністю замініть цей код своєю реалізацією.
#
# Ваш код повинен відповідати таким вимогам:
# 1. Обрана предметна область згідно з вашим варіантом.
# 2. Реалізовано всі необхідні функції:
#    - додавання, видалення, оновлення даних
#    - пошук та фільтрація
#    - обчислення статистик (середнє, min/max)
#    - групування та агрегація
# 3. Використано map(), filter(), reduce(), сортування, зрізи.
# 4. Реалізовано операції з множинами та словниками.
# 5. Створено інтерактивне меню для користувача.
# =================================================================

# Ваш код повинен відповідати таким вимогам:
# 1. Обрана предметна область згідно з вашим варіантом.
# 2. Реалізовано всі необхідні функції:
#    - додавання, видалення, оновлення даних
#    - пошук та фільтрація
#    - обчислення статистик (середнє, min/max)
#    - групування та агрегація
# 3. Використано map(), filter(), reduce(), сортування, зрізи.
# 4. Реалізовано операції з множинами та словниками.
# 5. Створено інтерактивне меню для користувача.
# =================================================================

# Ваш код повинен відповідати таким вимогам:
# 1. Обрана предметна область згідно з вашим варіантом.
# 2. Реалізовано всі необхідні функції:
#    - додавання, видалення, оновлення даних
#    - пошук та фільтрація
#    - обчислення статистик (середнє, min/max)
#    - групування та агрегація
# 3. Використано map(), filter(), reduce(), сортування, зрізи.
# 4. Реалізовано операції з множинами та словниками.
# 5. Створено інтерактивне меню для користувача.
# =================================================================

# Предметна область: Система бронювання готелів (номери, гості, бронювання)
from functools import reduce

# Початкові дані: номери готелю, гості та бронювання
rooms = [
    {"room_id": 101, "type": "Single", "price": 1200, "capacity": 1, "amenities": {"Wi-Fi", "TV", "AC"}},
    {"room_id": 102, "type": "Double", "price": 1800, "capacity": 2, "amenities": {"Wi-Fi", "TV", "AC", "Minibar"}},
    {"room_id": 201, "type": "Suite", "price": 3500, "capacity": 3,
     "amenities": {"Wi-Fi", "TV", "AC", "Minibar", "Balcony"}},
    {"room_id": 202, "type": "Single", "price": 1300, "capacity": 1, "amenities": {"Wi-Fi", "TV"}},
    {"room_id": 301, "type": "Double", "price": 2000, "capacity": 2, "amenities": {"Wi-Fi", "TV", "AC", "Balcony"}}
]

guests = [
    {"guest_id": 1, "name": "Олександр Шевченко", "email": "shev@gmail.com", "vip": False},
    {"guest_id": 2, "name": "Марія Коваленко", "email": "mariya@ukr.net", "vip": True},
    {"guest_id": 3, "name": "Іван Мельник", "email": "melnyk@gmail.com", "vip": False}
]

bookings = [
    {"booking_id": 1, "guest_id": 1, "room_id": 101, "nights": 3, "total_paid": 3600},
    {"booking_id": 2, "guest_id": 2, "room_id": 201, "nights": 5, "total_paid": 17500},
    {"booking_id": 3, "guest_id": 3, "room_id": 102, "nights": 2, "total_paid": 3600},
    {"booking_id": 4, "guest_id": 1, "room_id": 301, "nights": 4, "total_paid": 8000}
]


#  2. Базові операції зі структурами даних (CRUD)
def add_room(rooms_list, room_id, r_type, price, capacity, amenities):
    #Додає новий номер до системи.
    new_room = {"room_id": room_id, "type": r_type, "price": price, "capacity": capacity, "amenities": set(amenities)}
    rooms_list.append(new_room)
    return f"Номер {room_id} успішно додано."


def update_room_price(rooms_list, room_id, new_price):
    #Оновлює вартість номера за його ID.
    for room in rooms_list:
        if room["room_id"] == room_id:
            room["price"] = new_price
            return f"Ціну номера {room_id} оновлено до {new_price} грн."
    return "Номер не знайдено."


def delete_booking(bookings_list, booking_id):
    #Видаляє бронювання за ID.
    global bookings
    initial_len = len(bookings_list)
    bookings_list[:] = [b for b in bookings_list if b["booking_id"] != booking_id]
    if len(bookings_list) < initial_len:
        return f"Бронювання №{booking_id} успішно видалено."
    return "Бронювання з таким ID не знайдено."


def search_rooms_by_type(rooms_list, r_type):
    #Шукає номери за типом.
    return [r for r in rooms_list if r["type"].lower() == r_type.lower()]


def filter_rooms_by_max_price(rooms_list, max_price):
    #Фільтрує номери за максимальною ціною.
    return list(filter(lambda r: r["price"] <= max_price, rooms_list))


# 3. Специфічні функції аналізу (Статистика, групування, агрегація)
def get_room_price_statistics(rooms_list):
    #Обчислює мінімальну, максимальну та середню вартість номерів."""
    if not rooms_list:
        return 0, 0, 0
    prices = [r["price"] for r in rooms_list]
    min_p = min(prices)
    max_p = max(prices)
    avg_p = sum(prices) / len(prices)
    return min_p, max_p, avg_p


def group_rooms_by_type(rooms_list):
    #Групує номери за їх типом за допомогою словників.
    grouped = {}
    for room in rooms_list:
        r_type = room["type"]
        if r_type not in grouped:
            grouped[r_type] = []
        grouped[r_type].append(room)
    return grouped


#  4. Використання вбудованих функцій (map, filter, reduce) та зрізів
def get_all_guest_emails(guests_list):
    #використовує map() для отримання списку всіх електронних адрес гостей.
    return list(map(lambda g: g["email"], guests_list))


def get_total_revenue(bookings_list):
    #використовує reduce() для обчислення загального доходу від усіх бронювань.
    if not bookings_list:
        return 0
    return reduce(lambda acc, b: acc + b["total_paid"], bookings_list, 0)


def get_top_expensive_rooms(rooms_list, top_n=3):
    # сортування та зрізи для отримання топ найдорожчих номерів.
    sorted_rooms = sorted(rooms_list, key=lambda x: x["price"], reverse=True)
    return sorted_rooms[:top_n]


#  5. Робота з множинами та словниками
def analyze_amenities(rooms_list):
    # операції з множинами для зручностей (зручності у всіх номерех, унікальні тощо).
    if not rooms_list:
        return set(), set()
    all_amenities = set.union(*(room["amenities"] for room in rooms_list))
    common_amenities = set.intersection(*(room["amenities"] for room in rooms_list))
    return all_amenities, common_amenities


def build_guest_frequency_index(bookings_list):
    # словники для підрахунку частоти бронювань на кожного гостя.
    frequency = {}
    for b in bookings_list:
        g_id = b["guest_id"]
        frequency[g_id] = frequency.get(g_id, 0) + 1
    return frequency


#  6. Інтерактивний інтерфейс (Меню)
def main():
    print("Вітаємо в Системі бронювання готелів!")

    while True:
        print("\n--- ГОЛОВНЕ МЕНЮ ---")
        print("1. Переглянути всі номери та їх зручності")
        print("2. Додати новий номер")
        print("3. Оновити ціну номера")
        print("4. Фільтрувати номери за ціною (filter)")
        print("5. Отримати статистику цін (мін, макс, середня)")
        print("6. Загальний дохід від бронювань (reduce)")
        print("7. Топ найдорожчих номерів (сортування та зрізи)")
        print("8. Аналіз зручностей номерів (операції з множинами)")
        print("9. Статистика бронювань гостей (словники)")
        print("10. Видалити бронювання")
        print("11. Вийти")

        try:
            choice = int(input("Оберіть пункт меню (1-11): "))

            if choice == 1:
                print("\nСписок номерів:")
                for r in rooms:
                    print(
                        f"Номер {r['room_id']} | Тип: {r['type']} | Ціна: {r['price']} грн | Зручності: {', '.join(r['amenities'])}")

            elif choice == 2:
                r_id = int(input("Введіть ID номера: "))
                r_type = input("Введіть тип номера (Single, Double, Suite тощо): ")
                price = float(input("Введіть ціну за добу: "))
                capacity = int(input("Введіть місткість осіб: "))
                amenities_input = input("Введіть зручності через кому (наприклад: Wi-Fi, TV): ")
                amenities = [a.strip() for a in amenities_input.split(",")]
                print(add_room(rooms, r_id, r_type, price, capacity, amenities))

            elif choice == 3:
                r_id = int(input("Введіть ID номера для оновлення: "))
                new_p = float(input("Введіть нову ціну: "))
                print(update_room_price(rooms, r_id, new_p))

            elif choice == 4:
                max_p = float(input("Введіть максимальну ціну номера: "))
                filtered = filter_rooms_by_max_price(rooms, max_p)
                print(f"\nЗнайдено номерів (<= {max_p} грн): {len(filtered)}")
                for r in filtered:
                    print(f"- Номер {r['room_id']} ({r['type']}): {r['price']} грн")

            elif choice == 5:
                min_p, max_p, avg_p = get_room_price_statistics(rooms)
                print(f"\nСтатистика цін на номери:")
                print(f"Мінімальна ціна: {min_p} грн")
                print(f"Максимальна ціна: {max_p} грн")
                print(f"Середня вартість: {avg_p:.2f} грн")

            elif choice == 6:
                total = get_total_revenue(bookings)
                print(f"\nЗагальний дохід від усіх бронювань: {total} грн")

            elif choice == 7:
                top_n = int(input("Скільки топових номерів вивести? "))
                top_rooms = get_top_expensive_rooms(rooms, top_n)
                print(f"\nТоп-{top_n} найдорожчих номерів:")
                for r in top_rooms:
                    print(f"- Номер {r['room_id']} ({r['type']}): {r['price']} грн")

            elif choice == 8:
                all_am, common_am = analyze_amenities(rooms)
                print(f"\nУсі унікальні зручності в готелі: {all_am}")
                print(
                    f"Зручності, які є абсолютно у всіх номерах: {common_am if common_am else 'Відсутні спільні для всіх'}")

            elif choice == 9:
                freq = build_guest_frequency_index(bookings)
                print("\nЧастота бронювань за ID гостей:")
                for g_id, count in freq.items():
                    guest_name = next((g["name"] for g in guests if g["guest_id"] == g_id), "Невідомий")
                    print(f"- Гість: {guest_name} (ID: {g_id}) — Бронювань: {count}")

            elif choice == 10:
                b_id = int(input("Введіть ID бронювання для видалення: "))
                print(delete_booking(bookings, b_id))

            elif choice == 11:
                print("До побачення.")
                break
            else:
                print("Оберіть число від 1 до 11.")
        except ValueError:
            print("Перевірте коректність введених даних.")


if __name__ == "__main__":
    main()
