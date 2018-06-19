## Made by: Jocelyne Terrazas
## My Social Network


class User:
    def __init__(self, username):
        self.username = username
        self.firstName = ""
        self.lastName = ""
        self.bio = ""
        ##self.userID = userID
        self.friendsList = []
        self.posts = []
       

    def addfirstName(self, firstName):
        self.firstName = firstName

    def addlastName(self, lastName):
        self.lastName = lastName

    def addbio(self, bio):
        self.bio = bio

    def addFriend(self, person):
        self.friendsList.append(person)
        
    def addposts(self, posts):
        self.posts.append(post)
    
        
    def unFriend(self, obj):
        for friend in self.friendsList:
            if friend.username == obj.username:
                self.friendsList.remove(obj)

    def showUsernames(self):
        for friend in self.friendsList:
            print (friend.username)
                
    def viewNewsFeed(self):
        for friends in self.friendsList:
           print (friends.posts)
           
        

if __name__ == "__main__":

    username = "jocelyne"

    jocelyne = User("jocelyne")
    lucy = User("lucy")
    churrosanchez = User("churrosanchez")
    thejazziestjaz = User("thejazziestjaz")

    
##    print(jocelyne.firstName)
##    print(lucy.firstName)
##    print(churrosanchez.firstName)
##    print(thejazziestjaz.firstName)

    jocelyne.addFriend(lucy)
    jocelyne.addFriend(churrosanchez)
    jocelyne.addFriend(thejazziestjaz)
##    print(jocelyne.friendsList)

    lucy.posts.append("THIS IS MY FIRST POST")
    churrosanchez.posts.append("goodnight")
    thejazziestjaz.posts.append("music can end war")
##    print(lucy.posts)
##    print(churrosanchez.posts)
##    print(thejazziestjaz.posts)
print("This is your News Feed:")
jocelyne.viewNewsFeed()

print("This is your friends list:")  
jocelyne.showUsernames()

jocelyne.unFriend(churrosanchez)

print("This is your UPDATED friends list:")
jocelyne.showUsernames()


