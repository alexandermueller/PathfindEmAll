#!/usr/bin/python

nonPassable = {(0, -1) : ['X', 'j'], (-1, 0) : ['X'], (0, 1) : ['X', 'J'] , (1, 0) : ['X', 'J']}

# def h():
# def g():
# def pathFindAStar():


# Iterative Deepening DFS Implementation #
def pathFindIDDFS(mapping, visited, x, y, xV, yV, iterations):
    width = len(mapping[y])
    height = len(mapping)
    if iterations == 0 or mapping[y][x] in ['E', 'H'] and not visited.get('%d,%d' % (x, y)):
        return None if mapping[y][x] not in ['E', 'H'] else [[x, y]]

    elif mapping[y][x] == 'i' and mapping[y + yV][x + xV] not in nonPassable[(xV, yV)]:
        path = pathFindIDDFS(mapping, visited, x + xV, y + yV, xV, yV, iterations - 1)
        return None if path == None else [[x, y]] + path
        
    else:
        visited['%d,%d' % (x, y)] = 1
        up = None
        right = None
        down = None
        left = None
        if (y - 1) >= 0 and not visited.get('%d,%d' % (x, y - 1)) and mapping[y - 1][x] not in nonPassable[(0, -1)]:
            up = pathFindIDDFS(mapping, dict(visited), x, y - 1, 0, -1, iterations - 1)
        if (x + 1) < width and not visited.get('%d,%d' % (x + 1, y)) and mapping[y][x + 1] not in nonPassable[(1, 0)]:
            right = pathFindIDDFS(mapping, dict(visited), x + 1, y, 1, 0, iterations - 1)
        if (y + 1) < height and not visited.get('%d,%d' % (x, y + 1)) and mapping[y + 1][x] not in nonPassable[(0, 1)]:
            down = pathFindIDDFS(mapping, dict(visited), x, y + 1, 0, 1, iterations - 1)
        if (x - 1) >= 0 and not visited.get('%d,%d' % (x - 1, y)) and mapping[y][x - 1] not in nonPassable[(-1, 0)]:
            left = pathFindIDDFS(mapping, dict(visited), x - 1, y, -1, 0, iterations - 1)
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

def pathFindDFS(mapping, visited, x, y, xV, yV):
    width = len(mapping[y])
    height = len(mapping)
    if not visited.get('%d,%d' % (x, y)) and mapping[y][x] in ['E','H']:
        return [[x, y]]

    elif mapping[y][x] == 'i' and mapping[y + yV][x + xV] not in nonPassable[(xV, yV)]:
        path = pathFindDFS(mapping, visited, x + xV, y + yV, xV, yV)
        return None if path == None else [[x, y]] + path
        
    else:
        visited['%d,%d' % (x, y)] = 1
        (up,right,down,left) = [None,None,None,None]
        if (y - 1) >= 0 and not visited.get('%d,%d' % (x, y - 1)) and mapping[y - 1][x] not in nonPassable[(0, -1)]:
            up = pathFindDFS(mapping, dict(visited), x, y - 1, 0, -1)
        if (x + 1) < width and not visited.get('%d,%d' % (x + 1, y)) and mapping[y][x + 1] not in nonPassable[(1, 0)]:
            right = pathFindDFS(mapping, dict(visited), x + 1, y, 1, 0)
        if (y + 1) < height and not visited.get('%d,%d' % (x, y + 1)) and mapping[y + 1][x] not in nonPassable[(0, 1)]:
            down = pathFindDFS(mapping, dict(visited), x, y + 1, 0, 1)
        if (x - 1) >= 0 and not visited.get('%d,%d' % (x - 1, y)) and mapping[y][x - 1] not in nonPassable[(-1, 0)]:
            left = pathFindDFS(mapping, dict(visited), x - 1, y, -1, 0)

        shortest = []
        for direction in (up, right, down, left):
            if direction != None and len(direction) > len(shortest):
                shortest = direction
        return None if shortest == None else [[x, y]] + shortest