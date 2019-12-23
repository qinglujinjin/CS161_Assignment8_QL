
#Author: Qing Lu
#Date: 11/25/2019
#Title: Tic-Tac-Toe Program

import random
from time import sleep

WIDTH=3

class TicTacToe:
    def __init__(self):
        self.board = [["","",""] for i in range(WIDTH)]
        print(self.board)
        self.current_state = "UNFINISHED"

    def get_current_state(self):
        return self.current_state



    def diagWinLeft(self):
        l=[self.board[i][i] for i in range(3)]
        if l[0] and l==[l[0]]*3:
            return True,l[0]
        else:
            return False,''
        
    def diagWinRight(self):
        l=[self.board[2-i][2-i] for i in range(3)]
        if l[0] and l==[l[0]]*3:
            return True,l[0]
        else:
            return False,''

    def colWin(self):
        for i in range(3):
            col=[self.board[x][i] for x in range(3)]
            if col[0] and col==[col[0]]*3:
                return True,col[0]
        else:
            return False,''

    def rowWin(self):
        for i in range(3):
            row=[self.board[i][x] for x in range(3)]
            if row[0] and row==[row[0]]*3:
                return True,row[0]
        else:
            return False,''

    def draw(self):
        for l in self.board:
            for itm in l:
                if itm=='':
                    return False
        else:
            return True

    def make_move(self,row,col,player):
        if not 0<=row<=2:
            return False
        elif not 0<=col<=2:
            return False
        elif self.board[row][col]!="":
            return False
        elif self.current_state!="UNFINISHED":
            return False
        else:
            self.board[row][col]=player
            for f in [self.diagWinLeft,self.diagWinRight,self.colWin,self.rowWin]:
                res,who=f()
                if res==True:
                    self.current_state='%s_WON'%who.upper()
                    break
            else:
                if self.draw():
                    self.current_state='DRAW'
            return True

    def play(self):
        i=random.randint(0,1)
        while self.current_state=='UNFINISHED':
            i=1-i
            p='o' if i==0 else 'x'
            while self.current_state=='UNFINISHED':
                row=random.randint(0,2)
                col=random.randint(0,2)
                res=self.make_move(row,col,p)
                if res:break
            print(self)
            print(self.current_state)
            input("pause...")
            

    def __str__(self):
        tmp=['%s\n'%x for x in self.board]
        return ''.join(tmp)



if __name__=='__main__':
    t=TicTacToe()
    t.play()
