class player:
    def play(self):
        print("the player is playing cricket") 
class Batsman(player):
    def play(self):
        print("the batsman is batting") 
class Bowler(player):
    def play(self):
        print("the bowler is bowling")  
batsman = Batsman() 
bowler = Bowler()
# call the play() method of each object
batsman.play()
bowler.play()
    