Class Book:
  def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
  
  def show_info(self):
        print(f"Назва: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Рік видання: {self.year}")
