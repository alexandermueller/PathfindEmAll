#!/usr/bin/python

from os import walk
from pathFind import pathFind

maps = []
for (dirpath, dirnames, filenames) in walk('./Assets/Mappings'):
  maps.extend(filenames)
  break

for mappingName in [m[:-4] for m in maps if 'simplePath.txt' in m]:
    f = open('./Assets/Mappings/%s.txt' % (mappingName), 'r')
    mapping = list(f) 
    f.close()

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
    
    for exit in exits:
        x = exit[0]
        y = exit[1]
        visited['%d,%d' % (x, y)] = 1
        path = pathFind(mapping, dict(visited), x, y, 0, 0)
        if path != None:
            print path
            paths.append(path)
        visited['%d,%d' % (x, y)] = 0
    
    for path in paths:
        for tile in path:
            x = tile[0]
            y = tile[1]
            mapping[y] = mapping[y][:x] + '=' + mapping[y][x + 1:]

    for line in mapping:
        print line