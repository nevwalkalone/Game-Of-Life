"""Conway\'s Game of Life."""

#---------------------- Askisi 1 ------------------------
def board(n):
    dictionary={}
    i,j=0,0
    
    for item in range(n*n):
        dictionary[(i,j)]=False
        
        j+=1
        if j==n:
            i+=1
            j=0
    return dictionary



#---------------------- Askisi 2 ------------------------
def is_alive(board, p):
 
    return board[p]


def set_alive(board, p, alive):
    board[p]=alive
    
def get_size(board):
    
    from math import sqrt
    return int(sqrt(len(board)))


#---------------------- Askisi 3 ------------------------
def copy_board(board):

    new_dict=board.copy()
    return new_dict

#---------------------- Askisi 4 ------------------------
def get_iterator(board):
   
    a=list(board.items())
    a.sort()
    iterator=iter(a)
    return iterator


#---------------------- Askisi 5 ------------------------
def print_board(board):
   
    s=0
    for item in get_iterator(board):
        s=s+1
        
        if item[1]==True:
            print(chr(11035),end='')
        else:
            print(chr(11036),end='')
        if s==get_size(board):
            print('\n',end='')
            s=0

#---------------------- Askisi 6 ------------------------
def neighbors(p):
    
    newset=set
    s=p[1]-1
   
    for i in range(8):
        if i<3:
            newset=newset.union({(p[0]-1,s)})
            s=s+1
        elif i==3:
            s=p[1]-1
            newset=newset.union({(p[0],p[1]-1)})

        elif i==4:
            newset=newset.union({(p[0],p[1]+1)})

        else:
            newset=newset.union({(p[0]+1,s)})
            s=s+1
        
    return newset

#---------------------- Askisi 7 ------------------------
def place_blinker(board, p = (0,0)):
  
    s=p[0]
    for i in range(3):
        set_alive(board,(s,p[1]),True)
        s=s+1
        if s==get_size(board):
            break

def place_glider(board, p = (0,0)):
   
    if p[1]+2<get_size(board) and p[0]+2<get_size(board):
        set_alive(board,p,False)
        set_alive(board,(p[0],p[1]+2),True)
        set_alive(board,(p[0]+1,p[1]),True)
        set_alive(board,(p[0]+1,p[1]+2),True)
        set_alive(board,(p[0]+2,p[1]+1),True)
        set_alive(board,(p[0]+2,p[1]+2),True)
    else:
        print('Neighbors of this specific cell were less than 5 so the board will remain the same')
   #---------------------- Askisi 8 ------------------------
def tick(board):
    
    copied_dict=copy_board(board)
    
    for item in copied_dict.keys():
        copied_dict[item]=False
    
        
    counter=0  
    for key in board.keys():
        for item in neighbors(key):
            if item[0]>=get_size(board) or item[0]<0 or item[1]>=get_size(board) or item[1]<0:
                continue
            else:
                if is_alive(board,item)==True:
                    counter=counter+1
        if is_alive(board,key)==True:
            if counter==2 or counter==3:
                set_alive(copied_dict,key,True)
        else:
            if counter==3:
                set_alive(copied_dict,key,True)
        counter=0
   
       
    for key in copied_dict.keys():
        board[key]=copied_dict[key]
        
#---------------------- Askisi 9 ------------------------

if __name__ == '__main__':
    """Paizei to paixnidi gia mia sygkekrimeni arxiki topo8etisi, gia 
    100 genιes. O pinakas tou paixnidiou emfanizetai se  ka8e bima.
    Afiste toulaxiston 2 kenes grammes anamesa se diadoxikous pinakes.
    """

    # Arxikos pinakas
    game = board(10)
    place_blinker(game, (1,2))
    place_glider(game, (2,4))

    from time import sleep
    for i in range(100):
        tick(game)
        print_board(game)
        sleep(0.3)
        print('\n'+'\n'+'\n')

    
