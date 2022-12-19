import random
k=1
matrix,bmatrix=[],[]
for i in range(3):
    n=[]
    for j in range(3):
        n.append(k)
        k+=1
    matrix.append(n)

for i in range(3):
    n=[]
    for j in range(3):
        n.append("-")
    bmatrix.append(n)
    
def matprint():
    for i in range(3):
        for j in range(3):
            print(matrix[i][j],end=' ')
        print()

def matterprint():
    print("\n")
    for i in range(3):
        for j in range(3):
            print(bmatrix[i][j],end=' ')
        print()

l=[1,2,3,4,5,6,7,8,9]


while True:
    attack,defense=0,0
    play=[]
    comp=[]
    while len(l)!=0:
        matprint()
        a=int(input("\nEnter the index number here:"))
        if a in l:
            play.append(a)
            play.sort()
            for i in range(3):
                for j in range(3):
                    if matrix[i][j]==a:
                        print("\nThe player has moved to position ",a,"!",sep='')
                        bmatrix[i][j]='X'
                        l.remove(a)
                        matterprint()
                        
            
            
            if 1 in play and 2 in play and 3 in play:
                print("You win!")
                break
            elif 1 in play and 4 in play and 7 in play:
                print("You win!")
                break
            elif 7 in play and 8 in play and 9 in play:
                print("You win!")
                break
            elif 3 in play and 6 in play and 9 in play:
                print("You win!")
                break
            elif 4 in play and 5 in play and 6 in play:
                print("You win!")
                break
            elif 2 in play and 5 in play and 8 in play:
                print("You win!")
                break
            elif 1 in play and 5 in play and 9 in play:
                print("You win!")
                break
            elif 3 in play and 5 in play and 7 in play:
                print("You win!")
                break
            def kyodaimax():  #DEKAKU IKOZE!! (Start of AI)
                global attack
                global defense
                global m
                global n
                global cpu
                for i in range(len(comp)):
                    for j in range(len(comp)):
                        if comp[j]-comp[i]==1 and comp[j]%3!=0: #Rows
                            attack+=1
                            if comp[j]+1 in l:
                                m=comp[j]+1
                                break
                        elif comp[j]-comp[i]==2 and comp[j]<7: #Secondary diagonal
                            attack+=1
                            if comp[j]+2 in l:
                                m=comp[j]+2
                                break
                        elif comp[j]-comp[i]==3 and comp[j] not in[7,8,9]: #Columns
                            attack+=1
                            if comp[j]+3 in l:
                                m=comp[j]+3
                                break
                        elif comp[j]-comp[i]==4: #Middle Elememt of Secondary Diagonal
                            attack+=1
                            if comp[i]+2 in l:
                                m=comp[i]+2
                                break
                        elif comp[j]-comp[i]==6: #Middle Elememt of Main Diagonal
                            attack+=1
                            if comp[j]+3 in l:
                                m=comp[i]+3
                                break
                        elif comp[j]-comp[i]==2: #Middle Elememt of a Row
                            attack+=1
                            if comp[i]+1 in l:
                                m=comp[i]+1
                
                for i in range(len(play)):
                    for j in range(len(play)):
                        if play[j]-play[i]==1 and play[j]%3!=0: #Rows
                            defense+=1
                            if play[j]+1 in l:
                                n=play[j]+1
                                break
                        elif play[j]-play[i]==2 and play[j]<7: #Secondary diagonal
                            defense+=1
                            if play[j]+2 in l:
                                n=play[j]+2
                                break
                        elif play[j]-play[i]==3 and play[j] not in[7,8,9]: #Columns
                            defense+=1
                            if play[j]+3 in l:
                                n=play[j]+3
                                break
                        elif play[j]-play[i]==4: #Middle Element of Secondary Diagonal
                            defense+=1
                            if play[i]+2 in l:
                                n=play[i]+2
                                break
                        elif play[j]-play[i]==6: #Middle Element of Main Diagonal
                            defense+=1
                            if play[j]+3 in l:
                                n=play[i]+3
                                break
                        elif play[j]-play[i]==2: #Middle Element of a Row
                            defense+=1
                            if play[i]+1 in l:
                                n=play[i]+1

                if attack>defense:
                    if m in l:
                        cpu=m
                        print("Attack won here",attack)
                    else:
                        print("yep It happened.")
                        cpu=random.choice(l)

                elif defense>attack:
                    if n in l:
                        cpu=n
                        print("Defense won here",defense)
                        print("attack",attack)
                    else:
                        print("yep It happened")
                        cpu=random.choice(l)
                else:
                    print(attack,defense)
                    cpu=random.choice(l)

            #CPU THOUGHT PROCESS BEGINS
            kyodaimax()
            l.remove(cpu)
            for i in range(3):
                for j in range(3):
                    if matrix[i][j]==cpu:
                        print("\nThe CPU has moved to position ",cpu,"!",sep='')
                        bmatrix[i][j]='O'
                        matterprint()
                        comp.sort()
                        print()

            comp.append(cpu)

            if 1 in comp and 2 in comp and 3 in comp:
                print("Oh no! The computer wins!")
                break
            elif 1 in comp and 4 in comp and 7 in comp:
                print("Oh no! The computer wins!")
                break
            elif 7 in comp and 8 in comp and 9 in comp:
                print("Oh no! The computer wins!")
                break
            elif 3 in comp and 6 in comp and 9 in comp:
                print("Oh no! The computer wins!")
                break
            elif 4 in comp and 5 in comp and 6 in comp:
                print("Oh no! The computer wins!")
                break
            elif 2 in comp and 5 in comp and 8 in comp:
                print("Oh no! The computer wins!")
                break
            elif 1 in comp and 5 in comp and 9 in comp:
                print("Oh no! The computer wins!")
                break
            elif 3 in comp and 5 in comp and 7 in comp:
                print("Oh no! The computer wins!")
                break
            if len(l)==0:
                print("What a closely contested game! It ends in a tie!")
                quit()

        
            
        else:
            print("\nSorry, invalid number! Try again!")
    
    break