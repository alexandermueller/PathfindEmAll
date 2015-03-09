#!/usr/bin/python

nonPassable = {(0, -1) : ['X', 'j'], (-1, 0) : ['X'], (0, 1) : ['X', 'J'] , (1, 0) : ['X', 'J']}

# Very Accurate Iterative Deepening DFS Implementation #
def pathFindIDDFS(mapping, goal, visited, x, y, xV, yV, iterations):
    width = len(mapping[y])
    height = len(mapping)
    if iterations == 0 or [x,y] == goal and not visited.get('%d,%d' % (x, y)):
        return None if [x,y] != goal else [[x, y]]

    elif mapping[y][x] == 'i' and mapping[y + yV][x + xV] not in nonPassable[(xV, yV)]:
        path = pathFindIDDFS(mapping, goal, visited, x + xV, y + yV, xV, yV, iterations - 1)
        return None if path == None else [[x, y]] + path                              
    
    elif mapping[y][x] in ['J', 'j']:
        path = pathFindIDDFS(mapping, goal, visited, x + xV, y + yV, xV, yV, iterations)      # Usually you want to decrement iterations, but you aren't really
        return None if path == None else [[x, y]] + path                                # making a move here, so it we can afford to nullify the cost    
    
    else:
        visited['%d,%d' % (x, y)] = 1
        up = None
        right = None
        down = None
        left = None
        if (y - 1) >= 0 and not visited.get('%d,%d' % (x, y - 1)) and mapping[y - 1][x] not in nonPassable[(0, -1)]:
            up = pathFindIDDFS(mapping, goal, dict(visited), x, y - 1, 0, -1, iterations - 1)
        if (x + 1) < width and not visited.get('%d,%d' % (x + 1, y)) and mapping[y][x + 1] not in nonPassable[(1, 0)]:
            right = pathFindIDDFS(mapping, goal, dict(visited), x + 1, y, 1, 0, iterations - 1)
        if (y + 1) < height and not visited.get('%d,%d' % (x, y + 1)) and mapping[y + 1][x] not in nonPassable[(0, 1)]:
            down = pathFindIDDFS(mapping, goal, dict(visited), x, y + 1, 0, 1, iterations - 1)
        if (x - 1) >= 0 and not visited.get('%d,%d' % (x - 1, y)) and mapping[y][x - 1] not in nonPassable[(-1, 0)]:
            left = pathFindIDDFS(mapping, goal, dict(visited), x - 1, y, -1, 0, iterations - 1)
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

# Inaccurate, But Very Efficient Iterative Deepening DFS Implementation #
def pathFindApproxIDDFS(mapping, visited, x, y, xV, yV, iterations):
    width = len(mapping[y])
    height = len(mapping)
    if iterations == 0 or mapping[y][x] in ['E', 'H', 's'] and not visited.get('%d,%d' % (x, y)):
        return None if mapping[y][x] not in ['E', 'H', 's'] else [[x, y]]

    elif mapping[y][x] == 'i' and mapping[y + yV][x + xV] not in nonPassable[(xV, yV)]:
        path = pathFindApproxIDDFS(mapping, visited, x + xV, y + yV, xV, yV, iterations - 1)
        return None if path == None else [[x, y]] + path                                 
    
    elif mapping[y][x] in ['J', 'j']:
        path = pathFindApproxIDDFS(mapping, visited, x + xV, y + yV, xV, yV, iterations) # Usually you want to decrement iterations, but you aren't really
        return None if path == None else [[x, y]] + path                                 # making a move here, so it we can afford to nullify the cost    

    else:
        visited['%d,%d' % (x, y)] = 1
        up = None
        right = None
        down = None
        left = None
        if (y - 1) >= 0 and not visited.get('%d,%d' % (x, y - 1)) and mapping[y - 1][x] not in nonPassable[(0, -1)]:
            up = pathFindApproxIDDFS(mapping, visited, x, y - 1, 0, -1, iterations - 1)
        if (x + 1) < width and not visited.get('%d,%d' % (x + 1, y)) and mapping[y][x + 1] not in nonPassable[(1, 0)]:
            right = pathFindApproxIDDFS(mapping, visited, x + 1, y, 1, 0, iterations - 1)
        if (y + 1) < height and not visited.get('%d,%d' % (x, y + 1)) and mapping[y + 1][x] not in nonPassable[(0, 1)]:
            down = pathFindApproxIDDFS(mapping, visited, x, y + 1, 0, 1, iterations - 1)
        if (x - 1) >= 0 and not visited.get('%d,%d' % (x - 1, y)) and mapping[y][x - 1] not in nonPassable[(-1, 0)]:
            left = pathFindApproxIDDFS(mapping, visited, x - 1, y, -1, 0, iterations - 1)
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