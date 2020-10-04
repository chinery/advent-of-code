# Boy this one is messy!
# created a graph quite nicely, started doing critical path
# analysis, then realised the elves act in alphabetical order,
# not based on what will be shortest overall.
# So the simulation at the end just 'runs through' the events,
# but it is really messy. Sorry for that.
# Ignore all the functions that calculate the actual critical path,
# they assume infinite elves anyway (there would be more than 5 concurrent)
# events in this example.

import numpy as np
import math

class GraphNode:
    def __init__(self, task, time):
        self.task = task
        self.time = time
        self.children = []
        self.parents = []
        self.disttoend = 0

    def __str__(self):
        return f"Task {char(self.task)}, time: {self.time} \n" + \
                f"disttoend: {self.disttoend}\n" + \
                f"Parents: {[char(p.task) for p in self.parents]}\n" + \
                f"Children: {[char(c.task) for c in self.children]}"

def char(c):
    return chr(c + ord('A'))

dependencies = []
try:
    while True:
        line = input()
        dependencies.append((line[36], line[5]))
except EOFError:
    pass

dependencies.sort()
num = ord(dependencies[-1][0])-ord('A')+1

tasks = []
for i in range(0,num):
    tasks.append(GraphNode(i, 61+i))

depmat = np.zeros((num,num))
for dep in dependencies:
    task = ord(dep[0])-ord('A')
    depon = ord(dep[1])-ord('A')

    depmat[task, depon] = 1
    tasks[task].parents.append(tasks[depon])
    tasks[depon].children.append(tasks[task])

ix = np.where(np.sum(depmat, axis=1) == 0)
start = GraphNode(-1, 0)
for index in ix[0]:
    start.children.append(tasks[index])
    tasks[index].parents.append(start)

end = GraphNode(-1, 0)
for i in range(0,num):
    if len(tasks[i].children) == 0:
        tasks[i].children.append(end)
        end.parents.append(tasks[i])

def labelCriticalPath(ptr):
    if ptr == start:
        return
    for parent in ptr.parents:
        disttoend = ptr.disttoend + parent.time
        parent.disttoend = max(parent.disttoend, disttoend)
    for parent in ptr.parents:
        labelCriticalPath(parent)

# labelCriticalPath(end)

def printTasks():
    for task in tasks:
        print(task)
        print()

# this assumes infinite elves
def findCriticalPath(ptr):
    if ptr == end:
        return ''
    for child in ptr.children:
        if child.disttoend == (ptr.disttoend - ptr.time):
            # if there's more than one, take alphabetically first, which is hopefully first...?
            return char(child.task) + findCriticalPath(child)

def secondmin(l):
    m = min(l)
    sm = math.inf
    for i in l:
        if i != m and i < sm:
            sm = i
    return sm, l.index(sm)

# don't need to actually find critical path because the elves are stupid
numElves = 5
available = [task for task in start.children]
done = []
time = 0
elftime = [0]*numElves
elfptrs = [0]*numElves
while len(done) != num:
    freeelf = np.argmin(elftime)
    time = elftime[freeelf]
    if elfptrs[freeelf] != 0 and elfptrs[freeelf] not in done:
        justdone = elfptrs[freeelf]
        done.append(justdone)
        for task in justdone.children:
            parentsdone = True
            for parent in task.parents:
                if parent not in done:
                    parentsdone = False
                    break
            if parentsdone:
                available.append(task)
        available.sort(key=lambda x: x.task)
    if len(available) > 0:
        elfptrs[freeelf] = available.pop(0)
        elftime[freeelf] = time + elfptrs[freeelf].time
    else:
        elftime[freeelf], smix = secondmin(elftime)
        elfptrs[freeelf] = elfptrs[smix]

print(max(elftime))
