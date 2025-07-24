from pymongo import MongoClient

client = MongoClient("mongodb+srv://BubblyCat:Bobyr777@cluster0.3murmbb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["books_db"]
collection = db["books"]

print("\n📚 Всі книги:")
for book in collection.find():
    print(f"  - {book.get('назва', 'Без назви')} ({book.get('кількість_сторінок')} сторінок)")

print("\n🔍 Книга з назвою 'Гра престолів':")
book = collection.find_one({"назва": "Гра престолів"})
print(book if book else "  ❌ Не знайдено")

print("\n📘 Книги з кількістю сторінок > 200:")
for book in collection.find({"кількість_сторінок": {"$gt": 200}}):
    print(f"  - {book['назва']} ({book['кількість_сторінок']} сторінок)")

print("\n✏️ Змінюємо вартість книги 'Гра престолів' на 450 грн...")
collection.update_one(
    {"назва": "Гра престолів"},
    {"$set": {"вартість": 450}}
)
print("✅ Вартість оновлено.\n")

print("⭐ Додаємо поле 'favorite': True для книг 10 класу...")
collection.update_many(
    {"клас": 10},
    {"$set": {"favorite": True}}
)
print("✅ Оновлено всі відповідні книги.\n")

print("🗑 Видаляємо одну книгу (наприклад, 'Хімія')...")
collection.delete_one({"назва": "Хімія"})
print("✅ Видалено книгу 'Хімія'.\n")

print("🧹 Видаляємо всі книги з кількістю сторінок менше 100...")
deleted = collection.delete_many({"кількість_сторінок": {"$lt": 100}})
print(f"✅ Видалено {deleted.deleted_count} книг.\n")

print("Оновлений список книг:")
for book in collection.find():
    print(f"  - {book.get('назва', 'Без назви')} ({book.get('кількість_сторінок')} сторінок)")
print("@BubblyCat")