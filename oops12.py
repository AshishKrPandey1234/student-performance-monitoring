#book
class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.page=pages
    def ShowBook(self):
        print(self.title)
        print(self.author)
        print(self.page)
title=input("enter title of book ")
author=input("enter name of the author ")
pages=int(input("enter number of pages "))
Book1=Book(title,author,pages)
Book1.ShowBook()