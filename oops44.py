class Movie(object):
    def __init__(self,title,mins,hero):
        self.title=title
        self.runtime=mins
        self.hero=hero
    def Printer(self):
        print(f"title is {self.title}\ runtime is{self.runtime}\ hero is {self.hero}")
list_of_movies=[]
while True:
    title=input("enter the title of movies")
    mins=input("enter the time of movies")
    hero=input("enter the name of hero")
    obj=Movie(title,mins,hero)
    list_of_movies.append(obj)
    print("mo ie added to list")
    ans=input("do you want to another movie (y/n)")
    if ans!='y':
        break
print("All movie information")
for obj in list_of_movies:
    obj.Printer()
