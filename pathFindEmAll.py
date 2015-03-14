#!/usr/bin/python

from os import walk
from pathFind import *
from pathDraw import *

testingPath = './Assets/Mappings/Testing'
mappingsPath = './Assets/Mappings'
workingDirectory = mappingsPath

maps = []
for (dirpath, dirnames, filenames) in walk(workingDirectory):
  maps.extend(filenames)
  break

for mappingName in [m[:-4] for m in maps if '.txt' in m]:
    f = open('%s/%s.txt' % (workingDirectory, mappingName), 'r')
    mapping = list(f) 
    f.close()
    
    height = len(mapping)
    width = len(mapping[0])
    visited = dict()
    paths = list()
    ladders = list()
    exits = list()
    
    i = 0
    for line in mapping:
        j = 0
        for char in line:
            if char == 'H':
                ladders.append([j, i])
            elif char == 'E':
                exits.append([j,i])
            j += 1
        i += 1
    
    # Exit order doesn't matter here, we're just trying to find an ordering of checkpoints to break the map up
    checkpoints = list()
    checkpoints.append(exits[0])
    laddersCopy = list(ladders)
    while True:
        x = checkpoints[-1][0]
        y = checkpoints[-1][1]
        visited['%d,%d' % (x, y)] = 1
        path = None
        for i in xrange(1, 1000):
            print "Currently on mapping %s, checkpoint %d, with %d iterations" % (mappingName, len(checkpoints), i)
            path = pathFindApproxIDDFS(mapping, dict(visited), x, y, 0, 0, i)
            if path != None:
                paths.append(path)
                checkpoint = list(path[-1])
                checkpoints.append(checkpoint)
                if checkpoint in ladders:
                    laddersCopy.remove(checkpoint)
                    checkpoints.append(laddersCopy[0])
                break
        if checkpoints[-1] in exits:
            break

    # Then do the fine-grained search.
    
    print "Checkpoints in the map: ", checkpoints

    if workingDirectory != testingPath:
        visited = dict()
        paths = list()
        while len(checkpoints) > 1:
            goal = checkpoints[1]
            x = checkpoints[0][0]
            y = checkpoints[0][1]
            visited['%d,%d' % (x, y)] = 1
            path = None
            for i in xrange(1, 1000):
                print "Currently on mapping %s, %d checkpoints left, with %d iterations" % (mappingName, len(checkpoints), i)
                path = pathFindIDDFS(mapping, goal, dict(visited), x, y, 0, 0, i)
                if path != None:
                    paths.append(path)
                    checkpoints = checkpoints[1:]
                    if goal in ladders:
                        checkpoints = checkpoints[1:]
                    break

    directions = list()
    for path in paths:
        for tile in path:
                x = tile[0]
                y = tile[1]
                directions += [(x * 16 + 8, y * 16 + 7)]
                if mapping[y][x] not in ['E', 'H', 's']:
                    mapping[y] = mapping[y][:x] + '=' + mapping[y][x + 1:]

    for row in mapping:
        print row
    
    pathDraw(directions, mappingName, height, width)