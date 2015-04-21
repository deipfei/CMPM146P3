from Queue import PriorityQueue
from Queue import Queue
from math import fabs, sqrt

def find_path(source, destination, mesh):
    print "I'm in the method"
    sx, sy = source
    dx, dy = destination
    sourcebox = None
    destbox = None
    visited = []
    path = []
    detail_points = {}
    for box in mesh['boxes']:
        x1, x2, y1, y2 = box
        if x1 < sx and x2 > sx and y1 < sy and y2 > sy:
            #visited.append(box)
            sourcebox = box
        if x1 < dx and x2 > dx and y1 < dy and y2 > dy:
            #visited.append(box)
            destbox = box

    if sourcebox == destbox:
        return [(source, destination)], [sourcebox]

    #Dijkstra's Algorithm/ANY SEARCH THINGY HERE
    dist = {}
    prev = {}
    dist[sourcebox] = 0
    prev[sourcebox] = None
    firstboxsource = (dist[sourcebox], sourcebox)
    priorityQ = PriorityQueue()
    priorityQ.put(firstboxsource)
    standing_point = source

    path = []
    while not priorityQ.empty():
        #print "I'm in an infinite loop!"
        current = priorityQ.get()
        visited.append(current[1])
        if current[1] == destbox:
            end = current[1]
            boxes = []
            while end is not None:
                boxes.append(end)
                #print prev[end]
                end = prev[end]

            stand = source
            print boxes
            for box in boxes:
                path.append((stand, find_point(stand, box)))
                stand = find_point(stand, box)
            path.append((stand, destination))
            print path
            return path, visited

        neighbors = mesh['adj'][current[1]]
        for n in neighbors:
            alt = dist[current[1]] + point_distance(standing_point, find_point(standing_point, current[1]))
            if n not in dist or alt < dist[n]:
                standing_point = find_point(standing_point, current[1])
                dist[n] = alt
                prior = alt + heuristic_basic(destbox, current[1])
                priorityQ.put((prior, n))
                prev[n] = current[1]

    '''#breadth first search
    vertex = None
    prev = {}
    counter = 0
    q = Queue()
    q.put(sourcebox)
    prev[sourcebox] = None
    visited.append(sourcebox)
    finalbox = None
    while not q.empty():
        v = q.get()
        if box_equal(v, destbox):
            finalbox = v
            break
        for n in mesh['adj'][v]:
            if n not in visited:
                q.put(n)
                visited.append(n)
                prev[n] = v'''

    '''end = finalbox
    path.append(((dx, dy), (get_midpoint(end))))
   
    while prev[end] is not None:
        path.append((get_midpoint(prev[end]), get_midpoint(end)))
        end = prev[end]
    path.append(((sx, sy), get_midpoint(end)))'''

    print "No path!"
    return [], visited

def get_distance(box1, box2):
    x1, y1, x2, y2 = box1
    x3, y3, x4, y4 = box2
    if x4 - x3 == x2 - x1:
        return fabs((y4-y3)/2.0 - (y2-y1)/2.0);
    dist = fabs((((y4 - y3)/2.0) - ((y2 - y1)/2.0)) / (((x4 - x3)/2.0) - ((x2 - x1)/2.0)))
    return dist

def box_equal(box1, box2):
    x1, y1, x2, y2 = box1
    x3, y3, x4, y4 = box2
    if x1 == x3 and y1 == y3 and x2 == x4 and y2 == y4:
        return True
    return False

def get_midpoint(box):
    x1, y1, x2, y2 = box
    x = x2 - ((x2 - x1)/2.0)
    y = y2 - ((y2 - y1)/2.0)
    #print x
    #print y

    return (x, y)

def find_point(point, next_box):
    x, y = point
    x1, y1, x2, y2 = next_box
    x_next = min(x2-1, max(x1, x))
    y_next = min(y2-1, max(y1, y))
    return (x_next, y_next)

def point_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dist = sqrt(pow((x2 - x1), 2) + pow((y2-y1), 2))
    return dist

def heuristic_basic(boxa, boxb):
    x1, y1 = get_midpoint(boxa)
    x2, y2 = get_midpoint(boxb)
    return abs(x1 - x2 ) + abs(y1-y2)