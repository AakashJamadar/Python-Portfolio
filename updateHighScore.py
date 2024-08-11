#A game function in a program lets the user play a game and returns score as an integer.You need to read a file highscoe.txt which is
#either blank or contains the previous highscore of the game,you need to write a program to update the highscore whenever gamer breaks 
#the highscore

def game():
    return 365
score=game()

with open("highscore.txt") as f:
    highScore=f.read().strip()      #to remove leading and trailing white spaces
    if highScore=="":       #to handle the case when .txt is empty
        highScore=0
    else:
        highScore=int(highScore)
if score>highScore :
    with open("highscore.txt",'w') as f2:
        f2.write(str(score))