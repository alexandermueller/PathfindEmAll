#!/usr/bin/python

nonPassable = {(0, -1) : ['X', 'j'], (-1, 0) : ['X'], (0, 1) : ['X', 'J'] , (1, 0) : ['X', 'J']}


def pathFind(mapping, x, y, xV, yV, iterations):
    width = len(mapping[y])
    height = len(mapping)
    if iterations == 0:
        return None if mapping[y][x] not in ['E', 'H'] else [[x, y]]

    elif mapping[y][x] == 'i' and mapping[y + yV][x + xV] not in nonPassable[(xV, yV)]:
        path = pathFind(mapping, x + xV, y + yV, xV, yV, iterations - 1)
        return None if path == None else [[x, y]] + path
        
    else:
        mapping[y] = mapping[y][:x] + 'X' + mapping[y][x + 1:]
        up = None
        right = None
        down = None
        left = None
        if (y - 1) >= 0 and mapping[y - 1][x] not in nonPassable[(0, -1)]:
            up = pathFind(list(mapping), x, y - 1, 0, -1, iterations - 1)
        if (x + 1) < width and mapping[y][x + 1] not in nonPassable[(1, 0)]:
            right = pathFind(list(mapping), x + 1, y, 1, 0, iterations - 1)
        if (y + 1) < height and mapping[y + 1][x] not in nonPassable[(0, 1)]:
            down = pathFind(list(mapping), x, y + 1, 0, 1, iterations - 1)
        if (x - 1) >= 0 and mapping[y][x - 1] not in nonPassable[(-1, 0)]:
            left = pathFind(list(mapping), x - 1, y, -1, 0, iterations - 1)
        if up != None:
            return [[x, y]] + up
        elif right != None:
            return [[x, y]] + right
        elif down != None: 
            return [[x, y]] + down
        elif left != None:
            return [[x, y]] + left
        else:
            return None