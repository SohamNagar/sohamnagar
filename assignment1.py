class Book:
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.auther=author

class Library:
    def __init__(self,):
        self.book=[]
        self.patrons=[]

    def add_book(self):
        book_id=int(input("enter book id"))
        title=input("enter book title:")
        author=input("enter book author:")

        book=book(book_id,title,author)
        self.book.append(book)
          
        print("book added successfully")

    def desplay_book(self):
        print("/n books in library:")
        for book in self.books:
            print("book id:",book.book_id)
            print("title:",book.title)
            print("book author:",book.author)
            

library= Library()

library.add_book()

library.display_book()
