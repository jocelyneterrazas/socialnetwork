## Made by: Jocelyne Terrazas
## My Social Network


class User:
    def __init__(self, firstName, lastName, username, bio, userID):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.bio = bio
        self.userID = userID
        self.friends = []
        self.posts = []

    def addFriend(self, username):
        self.friends.append(username)
    ##def unFriend():

    def viewNewsFeed (self, friends):
       for friends in self.friends:
           print (friends.posts)
           
        

if __name__ == "__main__":
    firstName = "Jocelyne"
    lastName = "Terrazas"
    username = "jocelyne"
    bio = "hi"
    userID = "0000"

    jocelyne = User(firstName, lastName, username, bio, userID)
    lucy = User("Lucy", "Lucille", "lucy", "hola", "0001")
    churrosanchez = User("Churro", "Sanchez", "churrosanchez", "yeet", "0002")
    thejazziestjaz = User("Jazmin", "Solis", "thejazziestjaz", "I like animals","0003")

    
    print(jocelyne.firstName)
    print(lucy.firstName)
    print(churrosanchez.firstName)
    print(thejazziestjaz.firstName)

    jocelyne.addFriend("lucy")
    jocelyne.addFriend("churrosanchez")
    jocelyne.addFriend("thejazziestjaz")
    print(jocelyne.friends)

    lucy.posts.append("THIS IS MY FIRST POST")
    print(lucy.posts)

    churrosanchez.posts.append("goodnight")
    print(churrosanchez.posts)

    thejazziestjaz.posts.append("music can end war")
    print(thejazziestjaz.posts)
    jocelyne.viewNewsFeed(username)
