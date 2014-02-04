import geometry
import numpy as np

def josh(colors, target):
    print "josh", colors, target
    
#     all_colors = [(name, float(X), float(Y), float(Z))
#                   for name, X, Y, Z in csv.reader(open(colorcsv))]
    all_colors = [(name, float(X), float(Y), float(Z))
                  for name, X, Y, Z in colors]
    
    # background is marked SUPPORT
    support_i = [i for i, color in enumerate(all_colors) if color[0] == 'SUPPORT']
    if len(support_i)>0:
        support = np.array(all_colors[support_i[0]][1:])
        del all_colors[support_i[0]]
    else:
        support = None
    
    tg, hull_i = geometry.tetgen_of_hull([(X,Y,Z) for name, X, Y, Z in all_colors])
    colors = [all_colors[i] for i in hull_i]
    
    print ("thrown out: "
           + ", ".join(set(zip(*all_colors)[0]).difference(zip(*colors)[0])))
    
#     targets = [(name, float(X), float(Y), float(Z), float(BG))
#                for name, X, Y, Z, BG in csv.reader(open(targetcsv))]
    
#     for target in targets:
    name, X, Y, Z, BG = target
    
    target_point = support + (np.array([X,Y,Z]) - support)/(1-BG)
    
    tet_i, bcoords = geometry.containing_tet(tg, target_point)
           
    if tet_i == None:
        print "%s: Not in gamut" % target[0]
        # not in gamut
    else:
        
        names = [colors[i][0] for i in tg.tets[tet_i]]
        print "%s:" % target[0], names, bcoords

if __name__=="__main__":
    #import sys
    colorslist = [
                  [
                   ['SUPPORT', 5,5,5],
                   ['a',0,0,0],
                   ['b',1,0,1],
                   ['c',0,5,2],
                   ['d',3,7,0]],
                  [
                   ['SUPPORT', 1,2,3],
                   ['e',0,2,4],
                   ['f',2,0,4],
                   ['g',5,9,0],
                   ['h',4,4,4]]
                ]
    targetlist = [['tA?', 3,3,3,0], ['tB', 4,4,4,0]]
    
    for colors, target in zip(colorslist, targetlist):
        josh(colors, target)