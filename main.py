#Todo: Terminology for user, being able to upload a photo

# frulbd
cube = [['r', 'o', 'w', 'b', 'g', 'g', 'y', 'r', 'w'],
 ['g', 'b', 'o', 'w', 'r', 'r', 'g', 'g', 'r'],
 ['g', 'b', 'b', 'w', 'w', 'r', 'g', 'y', 'r'],
 ['y', 'r', 'y', 'w', 'o', 'y', 'r', 'b', 'o'],
 ['w', 'o', 'o', 'g', 'b', 'o', 'w', 'o', 'y'],
 ['b', 'y', 'o', 'w', 'y', 'y', 'b', 'g', 'b']]

cube1 = [['g','g','g','g','g','g','g','g','g'], ['r','r','r','r','r','r','r','r','r'], ['w','w','w','w','w','w','w','w','w'], ['o','o','o','o','o','o','o','o','o'], ['b','b','b','b','b','b','b','b','b'], ['y','y','y','y','y','y','y','y','y']]


#cube[r][c]

tp = ", r,  u, r', u', r', f, r2, u', r', u', r, u, r', f', "

#[All edges on front side, all edges on back side, all edges on slice layer]
edges = [(cube[0][1], cube[2][7]), (cube[0][5], cube[1][3]), (cube[0][7], cube[5][1]), (cube[0][4],
            cube[3][5]), (cube[4][1], cube[2][1]), (cube[4][3], cube[1][5]), (cube[4][7], cube[5][7]), (cube[4][5],
            cube[3][3]), (cube[2][5], cube[1][1]), (cube[5][5], cube[1][1]), (cube[5][3], cube[3][7]), (cube[2][3], cube[3][1])]

solved_edges = [(cube[0][1], cube[2][7]), (cube[0][5], cube[1][3]), (cube[0][7], cube[5][1]), (cube[0][4],
            cube[3][5]), (cube[4][1], cube[2][1]), (cube[4][3], cube[1][5]), (cube[4][7], cube[5][7]), (cube[4][5],
            cube[3][3]), (cube[2][5], cube[1][1]), (cube[5][5], cube[1][1]), (cube[5][3], cube[3][7]), (cube[2][3], cube[3][1])]

def swapper(buffer):
# Swapper function takes every case for what buffer piece is and returns setup moves for that edge, tperm, and the reverse of the setup moves
    #Green and white edge
    #If the buffer slot has green on top and white on the right
    if buffer == ('g','w'):
        notation = "L, d', l2" + tp + "l2, d, L'"
        newbuffer = edges[0]
        return(notation, newbuffer)
    elif buffer == ('w', 'g'):
        notation = "L2, d, l2" + tp + "l2, d', L2"
        newbuffer = (edges[0][1], edges[0][0])
        return(notation, newbuffer)
    #Green and red edge
    elif buffer == ('g', 'r'):
        notation = "D2, l" + tp + "l', D2"
        newbuffer = edges[1]
        return(notation, newbuffer)
    elif buffer == ('r', 'g'):
        notation = "D', l'" + tp + "l, D"
        newbuffer = (edges[1][1], edges[1][0])
        return(notation, newbuffer)
    #Green and yellow edge
    elif buffer == ('g', 'y'):
        notation = "L, d', l2" + tp + "l2, d, L'"
        newbuffer = edges[2]
    elif buffer == ('y', 'g'):
        notation = "d, l2" + tp + "l2, d'"
        newbuffer = (edges[2][1], edges[2][0])
    #Green and orange edge
    elif buffer == ('g', 'o'):
        notation = "l'" + tp + "l"
        newbuffer = edges[3]
    elif buffer == ('o', 'g'):
        notation = "D', l" + tp + "l', D"
        newbuffer = (edges[3][1], edges[3][0])
    #Blue and white edge
    elif buffer == ('b', 'w'):
        notation = "L', d, l2" + tp + "l2, d', L"
        newbuffer = edges[4]
    elif buffer == ('w', 'b'):
        notation = "L2, d', l2" + tp + "l2, d, L2"
        newbuffer = (edges[4][1], edges[4][0])
    #Blue and red edge
    elif buffer == ('b', 'r'):
        notation = "D2, l'" + tp + "l, D2"
        newbuffer = edges[5]
    elif buffer == ('r', 'b'):
        notation = "D, l" + tp + "l', D'"
        newbuffer = (edges[5][1], edges[5][0])
    #Blue and yellow edge
    elif buffer == ('b', 'y'):
        notation = "L', d', l2" + tp + "l2, d, L"
        newbuffer = edges[6]
    elif buffer == ('y', 'b'):
        notation = "d, l2" + tp + "l2, d'"
        newbuffer = (edges[6][1], edges[6][0])
    #Blue and orange edge
    elif buffer == ('b', 'o'):
        notation = "l" + tp + "l'"
        newbuffer = edges[7]
    elif buffer == ('o', 'b'):
        notation = "D, l'" + tp + "l, D'"
        newbuffer = (edges[7][1], edges[7][0])
    #White and orange edge
    elif buffer == ('w', 'o'):
        notation = tp
        newbuffer = edges[8]
    elif buffer == ('o', 'w'):
        notation = "l, D', l" + tp + "l', D, l'"
        newbuffer = (edges[8][1], edges[8][0])
    #Orange and yellow edge
    elif buffer == ('o', 'y'):
        notation = "l', D', l" + tp + "l', D, l"
        newbuffer = edges[9]
    elif buffer == ('y', 'o'):
        notation = "l2" + tp + "l2"
        newbuffer = (edges[9][1], edges[9][0])
    #Yellow and red edge
    elif buffer == ('y', 'r'):
        notation = "d2, l2" + tp + "l2, d2"
        newbuffer = edges[10]
    elif buffer == ('r', 'y'):
        notation = "d', L, d, l2" + tp + "l2, d', L', d"
        newbuffer = (edges[10][1], edges[10][0])
    return(notation, newbuffer)

def solver(edges2):
    while edges !=
    notation, newbuffer = swapper(edges[8])
    print(notation)
    notation, newbuffer = swapper(newbuffer)
    print(notation)

print(solver(edges))



#helloworld
#hello
#edit code
#click green checkamrk
#edit commit message
#click commit and push
#click push
#check in git if item I committed and puches is there
#done