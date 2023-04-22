#Todo: Terminology for user, being able to upload a photo

# frulbd



cube = [['g', 'g', 'r', 'g', 'g', 'g', 'g', 'g', 'g'],
 ['b', 'o', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
 ['w', 'w', 'w', 'w', 'w', 'y', 'w', 'w', 'w'],
 ['o', 'r', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
 ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
 ['y', 'y', 'y', 'w', 'y', 'y', 'y', 'y', 'y']]



#cube[r][c]

tp = " tperm "

a = 'g'
b = 'g'
c = 'g'
d = 'g'
e = 'g'
f = 'g'
g = 'g'
h = 'g'
i = 'g'
j = 'g'
k = 'g'


#[All edges on front side, all edges on back side, all edges on slice layer]
edges = [[cube[0][1], cube[2][7]], [cube[0][5], cube[1][3]], [cube[0][7], cube[5][1]], [cube[0][3],
            cube[3][5]], [cube[4][1], cube[2][1]], [cube[4][3], cube[1][5]], [cube[4][7], cube[5][7]], [cube[4][5],
            cube[3][3]], [cube[2][5], cube[1][1]], [cube[5][5], cube[1][7]], [cube[5][3], cube[3][7]], [cube[2][3], cube[3][1]]]

#The variables a-k represent the state of each edge where b is unsolved and g is solved
if (edges[0][1], edges[0][0]) != ('w', 'g'):
    a = 'b'
elif (edges[1][1], edges[1][0]) != ('r', 'g'):
    b = 'b'
elif (edges[2][1], edges[2][0]) != ('y', 'g'):
    c = 'b'
elif (edges[3][1], edges[3][0]) != ('o', 'g'):
    d = 'b'
elif (edges[4][1], edges[4][0]) != ('w', 'b'):
    e = 'b'
elif (edges[5][1], edges[5][0]) != ('r', 'b'):
    f = 'b'
elif (edges[6][1], edges[6][0]) != ('y', 'b'):
    g = 'b'
elif (edges[7][1], edges[7][0]) != ('o', 'b'):
    h = 'b'
elif (edges[11][1], edges[11][0]) != ('o', 'w'):
    i = 'b'
elif (edges[10][0], edges[10][1]) != ('o', 'y'):
    j = 'b'
elif (edges[9][1], edges[9][0]) != ('r', 'y'):
    k = 'b'

def swapper(buffer):
# Swapper function takes every case for what buffer piece is and returns setup moves for that edge, tperm, and the reverse of the setup moves green on top and white on the right
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global j
    global k

    x=11
    if buffer == ['g','w']:
        notation = "L, d', l2" + tp + "l2, d, L'"
        newbuffer = edges[0]
        a = 'g'
    elif buffer == ['w', 'g']:
        notation = "L2, d, l2" + tp + "l2, d', L2"
        newbuffer = [edges[0][1], edges[0][0]]
        a = 'g'
    #Green and red edge
    elif buffer == ['g', 'r']:
        notation = "D2, l" + tp + "l', D2"
        newbuffer = edges[1]
        b = 'g'
    elif buffer == ['r', 'g']:
        notation = "D', l'" + tp + "l, D"
        newbuffer = [edges[1][1], edges[1][0]]
        b = 'g'
    #Green and yellow edge
    elif buffer == ['g', 'y']:
        notation = "L, d', l2" + tp + "l2, d, L'"
        newbuffer = edges[2]
        c = 'g'
    elif buffer == ['y', 'g']:
        notation = "d', l2" + tp + "l2, d"
        newbuffer = [edges[2][1], edges[2][0]]
        c = 'g'
    #Green and orange edge
    elif buffer == ['g', 'o']:
        notation = "l'" + tp + "l"
        newbuffer = edges[3]
        d = 'g'
    elif buffer == ['o', 'g']:
        notation = "D', l" + tp + "l', D"
        newbuffer = [edges[3][1], edges[3][0]]
        d = 'g'
    #Blue and white edge
    elif buffer == ['b', 'w']:
        notation = "L', d, l2" + tp + "l2, d', L"
        newbuffer = edges[4]
        e = 'g'
    elif buffer == ['w', 'b']:
        notation = "L2, d', l2" + tp + "l2, d, L2"
        newbuffer = [edges[4][1], edges[4][0]]
        e = 'g'
    #Blue and red edge
    elif buffer == ['b', 'r']:
        notation = "D2, l'" + tp + "l, D2"
        newbuffer = edges[5]
        f = 'g'
    elif buffer == ['r', 'b']:
        notation = "D, l" + tp + "l', D'"
        newbuffer = [edges[5][1], edges[5][0]]
        f = 'g'
    #Blue and yellow edge
    elif buffer == ['b', 'y']:
        notation = "L', d', l2" + tp + "l2, d, L"
        newbuffer = edges[6]
        g = 'g'
    elif buffer == ['y', 'b']:
        notation = "d, l2" + tp + "l2, d'"
        newbuffer = [edges[6][1], edges[6][0]]
        g = 'g'
    #Blue and orange edge
    elif buffer == ['b', 'o']:
        notation = "l" + tp + "l'"
        newbuffer = edges[7]
        h = 'g'
    elif buffer == ['o', 'b']:
        notation = "D, l'" + tp + "l, D'"
        newbuffer = [edges[7][1], edges[7][0]]
        h = 'g'
    #White and orange edge
    elif buffer == ['w', 'o']:
        notation = tp
        newbuffer = edges[11]
        i = 'g'
    elif buffer == ['o', 'w']:
        notation = "l, D', l" + tp + "l', D, l'"
        newbuffer = [edges[11][1], edges[11][0]]
        i = 'g'
    #Orange and yellow edge
    elif buffer == ['o', 'y']:
        notation = "l', D', l" + tp + "l', D, l"
        newbuffer = edges[10]
        j = 'g'
    elif buffer == ['y', 'o']:
        notation = "l2" + tp + "l2"
        newbuffer = [edges[10][0], edges[10][1]]
        j = 'g'
    #Yellow and red edge
    elif buffer == ['r', 'y']:
        notation = "d2, l2" + tp + "l2, d2"
        newbuffer = edges[9]
        k = 'g'
    elif buffer == ['y', 'r']:
        notation = "d', L, d, l2" + tp + "l2, d', L', d"
        newbuffer = [edges[9][1], edges[9][0]]
        k = 'g'
    elif buffer == ['w','r'] or ['r','w']:
        if a == 'b':
            notation = "L2, d, l2" + tp + "l2, d', L2"
            newbuffer = (edges[0][1], edges[0][0])
            edges[0][1], edges[0][0] = buffer[0], buffer[1]
        elif b == 'b':
            notation = "D', l'" + tp + "l, D"
            newbuffer = (edges[1][1], edges[1][0])
            edges[1][1], edges[1][0] = buffer[0], buffer[1]
        elif c == 'b':
            notation = "d', l2" + tp + "l2, d"
            newbuffer = (edges[2][1], edges[2][0])
            edges[2][1], edges[2][0] = buffer[0], buffer[1]
        elif d == 'b':
            notation = "D', l" + tp + "l', D"
            newbuffer = (edges[3][1], edges[3][0])
            edges[3][1], edges[3][0] = buffer[0], buffer[1]
        elif e == 'b':
            notation = "L', d, l2" + tp + "l2, d', L"
            newbuffer = (edges[4][1], edges[4][0])
            edges[4][1], edges[4][0] = buffer[0], buffer[1]
        elif f == 'b':
            notation = "L2, d', l2" + tp + "l2, d, L2"
            newbuffer = (edges[5][1], edges[5][0])
            edges[5][1], edges[5][0] = buffer[0], buffer[1]
        elif g == 'b':
            notation = "d, l2" + tp + "l2, d'"
            newbuffer = (edges[6][1], edges[6][0])
            edges[6][1], edges[6][0] = buffer[0], buffer[1]
        elif h == 'b':
            notation = "D, l'" + tp + "l, D'"
            newbuffer = (edges[7][1], edges[7][0])
            edges[7][1], edges[7][0] = buffer[0], buffer[1]
        elif i == 'b':
            notation = "l, D', l" + tp + "l', D, l'"
            newbuffer = (edges[11][1], edges[11][0])
            edges[11][1], edges[11][0] = buffer[0], buffer[1]
        elif j == 'b':
            notation = "l2" + tp + "l2"
            newbuffer = (edges[10][0], edges[10][1])
            edges[10][0], edges[10][1] = buffer[0], buffer[1]
        elif k == 'b':
            notation = "d', L, d, l2" + tp + "l2, d', L', d"
            newbuffer = (edges[9][1], edges[9][0])
            edges[9][1], edges[9][0] = buffer[0], buffer[1]

    return(notation, newbuffer)
def solver(edges2):
    notation, newbuffer = swapper(edges[8])
    print(notation)
    while a == 'b' or b == 'b' or c == 'b' or d == 'b' or e == 'b' or f == 'b' or g == 'b' or h == 'b' or i == 'b' or j == 'b' or k == 'b':
        notation, newbuffer = swapper(newbuffer)
        print(notation)

solver(edges)


