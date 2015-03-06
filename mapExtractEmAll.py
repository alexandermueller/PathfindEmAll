#!/usr/bin/python

from PIL import Image, ImageDraw, ImageFont, ImageChops
from os import walk

tiles = {} 
tiles["ice"] = Image.open("./Assets/Tiles/ice.png")
tiles["jumpDown"] = Image.open("./Assets/Tiles/jumpDown.png")
tiles["jumpLeft"] = Image.open("./Assets/Tiles/jumpLeft.png")
tiles["groundLow"] = Image.open("./Assets/Tiles/groundLow.png")
tiles["groundHigh"] = Image.open("./Assets/Tiles/groundHigh.png")
tiles["stairs"] = Image.open("./Assets/Tiles/stairs.png")
tiles["ladder"] = Image.open("./Assets/Tiles/ladder.png")
tiles["entrance"] = Image.open("./Assets/Tiles/entrance.png")

mappings = { "ice" : "i", "groundLow" : "`", "groundHigh" : "`", "jumpLeft" : "J", "jumpDown" : "j", "stairs" : "s", "ladder" : "H", "entrance" : "E" }
frequencies = { "ice" : 0, "groundLow" : 0, "groundHigh" : 0, "jumpLeft" : 0, "jumpDown" : 0, "stairs" : 0, "ladder" : 0, "entrance" : 0  }

maps = []
for (dirpath, dirnames, filenames) in walk("./Assets/Maps"):
  maps.extend(filenames)
  break

for mapName in [m[:-4] for m in maps if '.png' in m]:
  mapFile = Image.open("./Assets/Maps/%s.png" % (mapName))
  width, height = mapFile.size
  exits = list()
  ladders = list()
  mapping = list()

  for i in xrange(height/16):
      row = ""
      for j in xrange(width/16):
          box = (16 * j, 16 * i, 16 * j + 16, 16 * i + 16)
          tile = mapFile.crop(box)
          char = ""
          for key in tiles.keys():
            if ImageChops.difference(tile, tiles[key]).getbbox() is None:
              if key == "entrance":
                exits.append([j, i])
              elif key == "ladder":
                ladders.append([j, i])
              char = mappings[key]
              frequencies[key] += 1
              break
          row += "X" if char == "" else char
      mapping.append(row)

  for exit in exits:
    x = exit[0]
    y = exit[1]
    if (x - 1) >= 0:
      mapping[y] = mapping[y][:x - 1] + 'X' + mapping[y][x:]
    if (x + 1) < width/16: 
      mapping[y] = mapping[y][:x + 1] + 'X' + mapping[y][x + 2:]
    if y + 1 < height/16:
      mapping[y + 1] = mapping[y + 1][:x] + 'X' + mapping[y + 1][x + 1:]

  f = open("./Assets/Mappings/%sMapping.txt" % (mapName), "w+")
  for line in mapping:
    f.write("%s\n" % (line))
  f.close()

  print "               Map: %s" % mapName
  print "       Frequencies: %s" % frequencies
  print "  Exit Coordinates: %s" % exits
  print "Ladder Coordinates: %s" % ladders