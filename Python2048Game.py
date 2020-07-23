import random
def start_game():
    #4X4 matrix
    mat=[[0 for i in range(4)] for j in range(4)]
    return mat

def add_new_2(mat):
    row=random.randint(0,3)
    col=random.randint(0,3)
    while mat[row][col]!=0:
        row=random.randint(0,3)
        col=random.randint(0,3)
    mat[row][col]=2

def reverse(mat):
    new_mat=[[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            new_mat[i][j]=mat[i][3-j]
    return new_mat

def transpose(mat):
    new_mat=[[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            new_mat[i][j]=mat[j][i]
    return new_mat

def merge(mat):
    changed=False
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                mat[i][j]=2*mat[i][j]
                mat[i][j+1]=0
                changed=True
    return mat,changed

def compress(mat):
    changed=False
    new_mat=[]
    #4X4 matrix
    new_mat=[[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos]=mat[i][j]
                if pos!=j:
                    changed=True
                pos+=1
                
    return new_mat,changed

def get_current_state(mat):
    #Anywhere 2048 is present
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return 'WON'
    #Anywhere 0 is present
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return 'GAME NOT OVER'
    #for every row or col except last row and last col
    for i in range(3):
        for j in range(3):
            if mat[i][j]==mat[i+1][j] or mat[i][j]==mat[i][j+1]:
                return 'GAME NOT OVER'
    #last row and col
    for j in range(3):
        if mat[3][j]==mat[3][j+1] or mat[j][3]==mat[j+1][3]:
            return 'GAME NOT OVER'
    return 'LOST'


def move_left(grid):
    new_grid,changed1=compress(grid)
    new_grid,changed2=merge(new_grid)
    new_grid,changed3=compress(new_grid)
    #Provides info if the grid was really changed or not
    #This info is necessary because based on this data, we will add the add_new_2
    #If this is true then we will add 2 else not.
    finalchange=changed1 or changed2
    return new_grid,finalchange

def move_right(grid):
    #Two ways to achieve this
    #1 reverse, compress, merge, compress and reverse
    #2 reverse call left function and then reverse
    reversed_grid=reverse(grid)
    new_grid,changed1=compress(reversed_grid)
    new_grid,changed2=merge(new_grid)
    new_grid,changed3=compress(new_grid)
    final_reversed=reverse(new_grid)
    '''
    reversed_grid=reverse(grid)
    new_grid=move_left(reversed_grid)
    final_reversed=reverse(new_grid)
    '''
    finalchange=changed1 or changed2
    return final_reversed,finalchange

def move_up(grid):
    #Two ways to achieve this
    #1 Take transpose reverse, compress, merge and transpose
    #2 Take transpose call left function and then reverse
    transposed_grid=transpose(grid)
    new_grid,changed1=compress(transposed_grid)
    new_grid,changed2=merge(new_grid)
    new_grid,changed3=compress(new_grid)
    final_transposed=transpose(new_grid)
    '''
    transposed_grid=transpose(grid)
    new_grid=move_left(transposed_grid)
    final_transposed=transpose(new_grid)
    '''
    finalchange=changed1 or changed2
    return final_transposed,finalchange

def move_down(grid):
    #Two ways to achieve this
    #1 Transpose,Reverse, compress, merge, Reverse and Transpose
    #2 Reverse move down and then reverse
    transposed_grid=transpose(grid)
    reversed_grid=reverse(transposed_grid)
    new_grid,changed1=compress(reversed_grid)
    new_grid,changed2=merge(new_grid)
    new_grid,changed3=compress(new_grid)
    reversed_grid=reverse(new_grid)
    final_transposed=transpose(reversed_grid)
    '''
    transposed_grid=transpose(grid)
    move_down(reversed_grid)
    final_reversed=transpose(reversed_grid)
    '''
    finalchange=changed1 or changed2
    return final_transposed,finalchange
    





