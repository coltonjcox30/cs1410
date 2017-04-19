import random
class player:

    def __init__(self,name):
        self.letters = []
        self.name = name
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
    def add_letter(self):
        self.letters.append(random.choice(self.alphabet))
        return self

    def remove(self,string):
        newlst = self.letters[:]
        for char in string:
            if char in newlst:
                newlst.pop(newlst.index(char))
            else:
                return False
        self.letters = newlst
        return True


def take_turn(player):
    print(player.name, "these are your letters",player.letters)
    word = input("Enter a word(press Enter to pass): ")
    if word == "":
        player.add_letter()
        print("You got an extra letter!")
    elif player.remove(word):
        print("Great job!")
    else:
        print ("check you letters and try again!")
        print ("")
        return take_turn(player)

    if len(player.letters) == 0:
        print ("")
        print (player.name, "WINS!")
        return True
    return False

def main():
    print ("Welcome! Time to play! Try to use all of your letters. The first player that uses all of their letters wins!")
    print ("")

    n = 8
    players = []                        
    numPlayers = int(input("How many players?"))
    
    for i in range(numPlayers):
        name = input("Enter name for player"+str(i+1)+":")
        p=player(name)
        players.append(p)

       
    print ("Game on!")
    for p in players:
        for i in range(n):
            p.add_letter()

    while True:
        for p in players:
            print ("")
            print(p.name+(", it's your turn."))
            if take_turn(p):
                print("Okay! Next round!")
                return

if __name__ == "__main__":
    main()








                
            
    
    
        
                 
