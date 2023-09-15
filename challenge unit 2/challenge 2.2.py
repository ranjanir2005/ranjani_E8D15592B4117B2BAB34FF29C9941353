#Define the case class Player

class Player:

 def play(self): print("The player is playing cricket.")



#Define the the derived class Batsman

class Batsman (Player):

 def play(self): print("The batsman is batting.")

# Define the derived class Bowler

class Bowler (Player):

 def play(self): print("The bowler is bowling.")

#Create objects of Batang ding Bowler classes

batsman = Batsman()

bowler = Bowler()



#Call the play() method for each object

batsman.play()

bowler.play()