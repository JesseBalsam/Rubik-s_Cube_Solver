#Todo: Terminology for user, being able to upload a photo

# frulbd
cube = [['o', 'b', 'g', 'r', 'g', 'o', 'o', 'y', 'w'],
 ['o', 'b', 'w', 'b', 'r', 'y', 'r', 'w', 'b'],
 ['b', 'w', 'b', 'y', 'w', 'w', 'w', 'r', 'y'],
 ['y', 'g', 'b', 'g', 'o', 'w', 'y', 'b', 'g'],
 ['r', 'o', 'r', 'r', 'b', 'o', 'o', 'r', 'r'],
 ['w', 'o', 'g', 'y', 'y', 'g', 'g', 'g', 'y']]


#cube[r][c]

tp = ", r,  u, r', u', r', f, r2, u', r', u', r, u, r', f', "

#[All edges on front side, all edges on back side, all edges on slice layer]
edges = [(cube[0][1], cube[2][7]), (cube[0][5], cube[1][3]), (cube[0][7], cube[5][1]), (cube[0][4],
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
        notation = "d, l'" + tp + "l, d'"
        newbuffer = (edges[1][1], edges[1][0])
        return(notation, newbuffer)
    #Green and yellow edge
    elif buffer == ('g', 'y'):
        return("L, d', l2" + tp + "l2, d, L'")
    elif buffer == ('y', 'g'):
        return("d, l2" + tp + "l2, d'")
    #Green and orange edge
    elif buffer == ('g', 'o'):
        return("l'" + tp + "l")
    elif buffer == ('o', 'g'):
        return("D', l" + tp + "l', D")
    #Blue and white edge
    elif buffer == ('b', 'w'):
        return("L', d, l2" + tp + "l2, d', L")
    elif buffer == ('w', 'b'):
        return("L2, d', l2" + tp + "l2, d, L2")
    #Blue and red edge
    elif buffer == ('b', 'r'):
        return("D2, l'" + tp + "l, D2")
    elif buffer == ('r', 'b'):
        return("D, l" + tp + "l', D'")
    #Blue and yellow edge
    elif buffer == ('b', 'y'):
        return("L', d', l2" + tp + "l2, d, L")
    elif buffer == ('y', 'b'):
        return("d, l2" + tp + "l2, d'")
    #Blue and orange edge
    elif buffer == ('b', 'o'):
        return("l" + tp + "l'")
    elif buffer == ('o', 'b'):
        return("D, l'" + tp + "l, D'")
    #White and orange edge
    elif buffer == ('w', 'o'):
        return(tp)
    elif buffer == ('o', 'w'):
        return("l, D', l" + tp + "l', D, l'")
    #Orange and yellow edge
    elif buffer == ('o', 'y'):
        return("l', D', l" + tp + "l', D, l")
    elif buffer == ('y', 'o'):
        return("l2" + tp + "l2")
    #Yellow and red edge
    elif buffer == ('y', 'r'):
        return("d2, l2" + tp + "l2, d2")
    elif buffer == ('r', 'y'):
        return("d', L, d, l2" + tp + "l2, d', L', d")

def solver(edges2):
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