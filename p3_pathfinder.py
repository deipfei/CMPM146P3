from Queue import PriorityQueue
from Queue import Queue
from math import fabs

def find_path(source, destination, mesh):
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

    '''#Dijkstra's Algorithm/ANY SEARCH THINGY HERE
    dist = {}
    prev = {}
    dist[sourcebox] = 0
    prev[sourcebox] = None
    source = (dist[sourcebox], sourcebox)
    priorityQ = PriorityQueue()
    priorityQ.put(source)

    path = []
    while not priorityQ.empty():
        #print "I'm in an infinite loop!"
        current = priorityQ.get()
        visited.append(current[1])
        if current[1] == destbox:
            end = current[1]
            while end is not None:
                path.append(end)
                end = prev[end]
            return path

        neighbors = mesh['adj'][current[1]]
        for n in neighbors:
            alt = dist[current[1]] + get_distance(current[1], n)
            if n not in dist or alt < dist[n]:
                dist[n] = alt
                prior = alt
                priorityQ.put((prior, n))
                prev[n] = current[1]'''

    #breadth first search
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
                prev[n] = v

    end = finalbox
    while prev[end] is not None:
        path.append((get_midpoint(prev[end]), get_midpoint(end)))
        end = prev[end]

    return path, visited

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
    x = x2 - ((x2 - x1)/2)
    y = y2 - ((y2 - y1)/2)
    print x
    print y

    return (x, y)