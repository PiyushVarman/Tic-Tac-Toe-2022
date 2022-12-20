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
corner=[1,3,7,9]

play=[]
comp=[]
while True:
    attack,defense=0,0
    
    while len(l)!=0:
        matprint()
        a=int(input("\nEnter the index number here:"))
        if a in l:
            play.append(a)
            if a in corner:
                corner.remove(a)
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
            
            upd=l
            def kyodaimax():  #DEKAKU IKOZE!! (Start of AI)
                global attack
                global defense
                m,n,=0,0
                global cpu
                print("Attack")
                for i in range(len(comp)):
                    for j in range(len(comp)):
                        if comp[j]-comp[i]==1 and ((comp[i]>=1 and comp[j]<=2) or (comp[i]>=4 and comp[j]<=5) or (comp[i]>=7 and comp[j]<=8)): #Rows
                            attack+=10
                            print("row end, right hand")
                            if comp[j]+1 in upd:
                                m=comp[j]+1
                                print(m)
                                break
                        if comp[j]-comp[i]==2 and (comp[i]==3 and comp[j]==5): #Secondary diagonal
                            print("Secondary Diagonal")
                            attack+=10
                            if comp[j]+2 in upd:
                                m=comp[j]+2
                                break
                        if comp[j]-comp[i]==4 and (comp[i]==3 and comp[j]==7):#Middle Elememt of Secondary Diagonal
                            attack+=10
                            print("middle gap of sec diag")
                            if comp[i]+2 in upd:
                                m=comp[i]+2
                                break
                        if comp[j]-comp[i]==2 and ((comp[i]>=1 and comp[j]<=3) or (comp[i]>=4 and comp[j]<=6) or (comp[i]>=7 and comp[j]<=9)): #Middle Element of a Row
                            attack+=10
                            print("Middle Gap in row")
                            if comp[i]+1 in upd:
                                m=comp[i]+1
                                break
                        if comp[j]-comp[i]==8: #Middle Elememt of Main Diagonal
                            attack+=10
                            print("Middle gap of main diag")
                            if comp[j]-4 in upd:
                                m=comp[i]+3
                                break
                        if comp[j]-comp[i]==3 and (comp[j] not in[7,8,9]): #Columns
                            attack+=10
                            print("column ender")
                            if comp[j]+3 in upd:
                                m=comp[j]+3
                                break
                        if comp[j]-comp[i]==3 and (comp[j] not in[1,2,3]): #Columns
                            attack+=10
                            print("column starter")
                            if comp[i]-3 in upd:
                                m=comp[i]-3
                                break
                        
                            if comp[j] in [4,5,6] and (comp[j]+3 in upd):
                                m=comp[j]+3
                                break
                
                print("\nDefensor:")
                for i in range(len(play)):
                    for j in range(len(play)):
                        if play[j]-play[i]==1 and play[j]%3!=0 and (play[j]+1 not in comp): #Rows
                            defense+=1
                            print("Rows")
                            if play[j]+1 in upd:
                                n=play[j]+1
                                break
                        elif play[j]-play[i]==4 and play[j]!=9 and (play[i] in [1,5,9] and play[j] in [1,5]): #main Diagonal
                            defense+=1
                            print("main Diagonal")
                            if play[j]-4 in upd:
                                n=play[j]-4
                                break
                        elif play[j]-play[i]==2 and (play[i] in [3,5] and play[j] in [5,7]): #Secondary diagonal
                            defense+=1
                            print("Secondary Diagonal")
                            if play[j]+2 in upd:
                                n=play[j]+2
                                break                        
                        elif play[j]-play[i]==4: #Middle Element of Secondary Diagonal
                            defense+=1
                            print("Middle Gap in secondary diagonal")
                            if play[i]+2 in upd:
                                n=play[i]+2
                                break
                        elif play[j]-play[i]==2 and ((play[i]>=1 and play[j]<=3) or (play[i]>=4 and play[j]<=6) or (play[i]>=7 and play[j]<=9)): #Middle Element of a Row
                            defense+=1
                            print("Middle Gap in row")
                            if play[i]+1 in upd:
                                n=play[i]+1
                        elif play[j]-play[i]==6: #Middle Elememt of Columns
                            defense+=1
                            print("middle Gap in columns")
                            if play[j]-3 in upd:
                                n=play[j]-3
                                break
                        if play[j]-play[i]==3 and (play[j] not in[7,8,9]): #Columns
                            defense+=1
                            print("column ender")
                            if play[j]+3 in upd:
                                n=play[j]+3
                                break
                        if play[j]-play[i]==3 and (play[j] not in[1,2,3]): #Columns
                            defense+=1
                            print("column starter")
                            if play[i]-3 in upd:
                                n=play[i]-3
                                break
                        elif play[j]-play[i]==8: #Middle Elememt of Main Diagonal
                            print("Middle gap of main diag")
                            defense+=1
                            if play[j]-4 in upd:
                                n=play[j]-4
                                break

                if attack>defense:
                    print("Attack won here",attack)
                    print("Defense is:",defense)
                    if m in upd:
                        cpu=m
                    else:
                        print("yep It happened no att in upd")
                        cpu=random.choice(upd)
                elif defense>attack:
                    print("Defense won here",defense)
                    print("attack",attack)
                    if n in upd:
                        cpu=n
                    else:
                        print("yep It happened no def in upd")
                        cpu=random.choice(upd)
                else:
                    print(attack,defense)
                    cpu=random.choice(upd)

                

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
