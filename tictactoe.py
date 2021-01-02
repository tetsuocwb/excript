
import os
import time
from playsound import playsound
os.system('clear')
print("Bem vindo ao tic tac toe CLI.")
# input("Pressione uma tecla para iniciar.")
jg = list(" "for i in range(10))
hip = {}
continua = True
cantos = [1, 3, 7, 9]
meios = [2, 4, 6, 8]


def board():
    print("",jg[1],"|",jg[2],"|",jg[3])
    print("---|---|---")
    print("",jg[4],"|",jg[5],"|",jg[6])
    print("---|---|---")
    print("",jg[7],"|",jg[8],"|",jg[9])
# print(board)


def playerltr():
    pos = input("Qual sua jogada: 1-9 : ")
    jg[int(pos)]= "X"
    board()

def win(itr):
    global continua
    if itr[1] == itr[2] == itr[3] != " "\
    or itr[4] == itr[5] == itr[6] != " "\
    or itr[7] == itr[8] == itr[9] != " "\
    or itr[1] == itr[4] == itr[7] != " "\
    or itr[2] == itr[5] == itr[8] != " "\
    or itr[3] == itr[6] == itr[9] != " "\
    or itr[1] == itr[5] == itr[9] != " "\
    or itr[7] == itr[5] == itr[3] != " "\
        :
        return True
        # continua = False
        # if ltr == "X":
        #     print("Ganhou!")
        # else:
        #     print("Perdeu!")
    # if jg[1] == jg[2] == jg[3] == "O"\
    # or jg[4] == jg[5] == jg[6] == "O"\
    # or jg[7] == jg[8] == jg[9] == "O"\
    # or jg[1] == jg[4] == jg[7] == "O"\
    # or jg[2] == jg[5] == jg[8] == "O"\
    # or jg[3] == jg[6] == jg[9] == "O"\
    # or jg[1] == jg[5] == jg[9] == "O"\
    # or jg[7] == jg[5] == jg[3] == "O"\
    #     :
    #     continua = False
    #     print("Perdeu!")
    else:
        return False
    


def compltr():
    for i,val in enumerate(jg):
        hip = jg[:]
        if jg[i] == " ":
            hip[i] = "O"
            if win(hip):
                jg[i] = "O"
                board()
                return
            hip[i] = "X"
            if win(hip):
                jg[i] = "O"
                board()
                return
    for i in cantos:
        if jg[i] == " ":
            jg[i] = "O"
            board()
            return
    for i in meios:
        if jg[i] == " ":
            jg[i] = "O"
            board()
            return
        jg[5] = "O"
        board()
    
    
    


board()
playsound('/Users/tetsuo/dev/python/Four_Giants_x_Pam-Takes_Time_(Pamaj\'s_BG_Music).mp3',False)

while continua:
    playerltr()
    if win(jg):
        continua = False
        print("VITORIA")
        break
    print("-----COMPUTADOR-----")
    compltr()
    if win(jg):
        continua = False
        print("DERROTA")
        break
    time.sleep(2)