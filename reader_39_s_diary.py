books = []

def add_book():
    book = {}
    book["Название книги"] = input("Введите название книги: ")
    book["Автор"] = input("Введите автора: ")
    book["Год написания"] = input("Введите год написания: ")
    book["Герои"] = input("Введите героев: ")
    book["Краткий пересказ"] = input("Введите краткий пересказ: ")
    book["Темы и проблемы произведения"] = input("Введите темы и проблемы произведения: ")
    book["Что понравилось"] = input("Что вам понравилось в книге: ")
    book["Что не понравилось"] = input("Что вам не понравилось в книге: ")
    book["Понравившиеся цитаты"] = input("Введите понравившиеся цитаты: ")
    book["Итоговая оценка"] = input("Введите итоговую оценку книги (1-10): ")
    books.append(book)
    print("Книга добавлена!")

def view_books():
    if len(books) == 0:
        print("Список книг пуст.")
    else:
        for i, book in enumerate(books):
            print(f"\nКнига #{i+1}")
            for key, value in book.items():
                print(f"{key}: {value}")
            print("-------------------")

def main():
    while True:
        print("\nЧитательский дневник")
        print("1. Добавить книгу")
        print("2. Просмотреть список книг")
        print("3. Выйти")

        choice = input("Выберите действие (1-3): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            break
        else:
            print("Неверный выбор. Попробуйте ещё раз.")

if __name__ == "__main__":
    main()



