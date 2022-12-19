import random
k=1
p1=input("Enter your name, Player 1!")
p2=input("Enter your name, Player 2!")
print("\nEnter symbols of your own choice! Ensure they are just one character long.")
sp1=input("\nWhat symbol would you like to use "+str(p1)+"?")
sp2=input("What symbol would you like to use "+str(p2)+"?")
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
    for i in range(3):
        for j in range(3):
            print(bmatrix[i][j],end=' ')
        print()
        

l=[1,2,3,4,5,6,7,8,9]
st=1
stat1,stat2=0,0
while True:
    play=[]
    comp=[]
    while len(l)!=0 and st!=0:
        while stat1!=1:
                matprint()
                a=int(input(p1+", enter the index number here:"))
                if a in l:
                    play.append(a)
                    for i in range(3):
                        for j in range(3):
                            if matrix[i][j]==a:
                                print(p1," has moved to position ",a,"!",sep='')
                                bmatrix[i][j]=sp1
                                l.remove(a)
                                matterprint()
                                print()
                                stat1=1
                                stat2=0
                    
                    
                        if 1 in play and 2 in play and 3 in play:
                            print(p1,"wins!")
                            st=0
                            exit()
                        elif 1 in play and 4 in play and 7 in play:
                            print(p1,"wins!")
                            st=0
                            exit()
                        elif 7 in play and 8 in play and 9 in play:
                            print(p1,"wins!")
                            st=0
                            exit()
                        elif 3 in play and 6 in play and 9 in play:
                            print(p1,"wins!")
                            st=0
                            exit()
                        elif 4 in play and 5 in play and 6 in play:
                            print(p1,"wins!")
                            st=0
                            exit()
                        elif 2 in play and 5 in play and 8 in play:
                            print(p1,"wins!")
                            st=0
                            exit()
                        elif 1 in play and 5 in play and 9 in play:
                            print(p1,"wins!")
                            st=0
                            exit()
                        elif 3 in play and 5 in play and 7 in play:
                            print(p1,"wins!")
                            st=0
                            exit()
                else:
                    print("\nSorry, invalid number, ",p1,"! Try again!",sep='')

        while stat2!=1:
                matprint()
                cpu=int(input(p2+", enter the index number here:"))
                if cpu in l:
                    comp.append(cpu)
                    for i in range(3):
                        for j in range(3):
                            if matrix[i][j]==cpu:
                                print(p2," has moved to position ",cpu,"!",sep='')
                                bmatrix[i][j]=sp2
                                l.remove(cpu)
                                matterprint()
                                print()
                                stat1=0
                                stat2=1
                                

                    if 1 in comp and 2 in comp and 3 in comp:
                        print(p2,"wins!")
                        st=0
                        exit()
                    elif 1 in comp and 4 in comp and 7 in comp:
                        print(p2,"wins!")
                        st=0
                        exit()
                    elif 7 in comp and 8 in comp and 9 in comp:
                        print(p2,"wins!")
                        st=0
                        exit()
                    elif 3 in comp and 6 in comp and 9 in comp:
                        print(p2,"wins!")
                        st=0
                        exit()
                    elif 4 in comp and 5 in comp and 6 in comp:
                        print(p2,"wins!")
                        st=0
                        exit()
                    elif 2 in comp and 5 in comp and 8 in comp:
                        print(p2,"wins!")
                        st=0
                        exit()
                    elif 1 in comp and 5 in comp and 9 in comp:
                        print(p2,"wins!")
                        st=0
                        exit()
                    elif 3 in comp and 5 in comp and 7 in comp:
                        print(p2,"wins!")
                        st=0
                        exit()
                    elif len(l)==0:
                        print("What a closely contested game! It ends in a tie!")
                        st=0
                        exit()

                else:
                    print("\nSorry, invalid number, ",p2,"! Try again!",sep='')
