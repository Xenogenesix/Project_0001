
from pymongo import MongoClient

client = MongoClient("mongodb+srv://BubblyCat:mySecret123@cluster0.3murmbb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["books_db"]
collection = db["books"]

game_of_thrones = {
    "назва": "Гра престолів",
    "вартість": 350,
    "рік_випуску": 1996,
    "кількість_сторінок": 694
}

school_books = [
    {"назва": "Українська мова", "клас": 7, "кількість_сторінок": 240},
    {"назва": "Математика", "клас": 9, "кількість_сторінок": 320},
    {"назва": "Історія України", "клас": 10, "кількість_сторінок": 300},
    {"назва": "Хімія", "клас": 8, "кількість_сторінок": 210},
    {"назва": "Біологія", "клас": 11, "кількість_сторінок": 280}
]

collection.insert_one(game_of_thrones)
collection.insert_many(school_books)

print("✅ Книги успішно додано до бази даних.\n")

for book in collection.find():
    print("Книга:")
    for key, value in book.items():
        if key != "_id":
            print(f"  {key}: {value}")
    print() 