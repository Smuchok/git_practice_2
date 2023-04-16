Class Book:
  def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
  
  def show_info(self):
        print(f"Назва: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Рік видання: {self.year}")
        
  def age(self):
        current_year = 2023
        return current_year - self.year

book1 = Book("Майстер і Маргарита", "Михайло Булгаков", 1967)
book1.show_info()
print(f"Вік книги: {book1.age()} років")
