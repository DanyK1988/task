def total_revenue(purchases):
    """Рассчитайте и верните общую выручку (цена * количество для всех записей)."""
    result = sum(purch["price"] * purch["quantity"] for purch in purchases)
    return result


def items_by_category(purchases):
    """Верните словарь, где ключ — категория, а значение — список уникальных товаров в этой категории"""
    result = {}
    for purch in purchases:
        result.setdefault(purch["category"], set()).add(purch["item"])
    return {cat: list(items) for cat, items in result.items()}


def expensive_purchases(purchases, min_price):
    """Выведите все покупки, где цена товара больше или равна min_price."""
    try:
        result = [purch for purch in purchases if purch["price"] >= min_price]
        return result
    except TypeError:
        return "Ошибка: min_price должен быть числом."


def average_price_by_category(purchases):
    """Рассчитайте среднюю цену товаров по каждой категории."""
    result = {}
    for purch in purchases:
        result.setdefault(purch["category"], []).append(purch["price"])
    return {cat: sum(prices) / len(prices) for cat, prices in result.items()}


def most_frequent_category(purchases):
    """Найдите и верните категорию, в которой куплено больше всего единиц товаров (учитывайте поле quantity)."""
    result = {}
    for purch in purchases:
        result[purch["category"]] = result.get(purch["category"], 0) + 1
    return max(result, key=result.get)


purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

print(f"Общая выручка: {total_revenue(purchases)}")
print(f"Товары по категориям: {items_by_category(purchases)}")
print(f"Покупки дороже 1.0: {expensive_purchases(purchases, 1.0)}")
print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
print(f"Самая частая категория: {most_frequent_category(purchases)}")
