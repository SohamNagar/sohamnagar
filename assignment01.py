class Library:

    def __init__(self):
        self.book=[]
        self.patron=[]


    def add_books (self):
        name=input("enter book name:")
        self.book.append(name)
        print("book added successfully")

    def display_book(self):
        
        print("books name:",self.book)


        
            
l=Library()
l.add_books()
l.add_books()
l.display_book()
