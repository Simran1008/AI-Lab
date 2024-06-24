def generateNext(state,capacity):
    m=state[0]
    n=state[1]
    c=state[2]
    if c==0:
        output=set()
        for i in range(0,capacity+1):
            for j in range(0,capacity+1):
                if (i!=0 or j!=0) and i<=j:
                    output.add((m-i,n-j+i,1))
        return output
    elif c==1:
        output=set()
        for i in range(0,capacity+1):
            for j in range(0,capacity+1):
                if (i!=0 or j!=0) and i<=j:
                    output.add((m+i,n+j-i,0))
        return output


def checkValid(state,x,y):
    m=state[0]
    c=state[1]
    if m>x or c>y or (x-m)>x or (y-c)>y or m<0 or c<0 or (x-m)<0 or (y-c)<0:
        return 0
    elif m>0 and m<c:
        return 0
    elif (x-m)>0 and (x-m)<(y-c):
        return 0
    return 1


def depthFirstSearch(state, x, y, capacity, visited, parent, paths):
    if state==(0,0,1):
        path=()
        while state!=(x,y,0):
            path+=(state,)
            state=parent[state]
        path+=((x,y,0),)
        paths.add(path[::-1])
        return

    states=generateNext(state, capacity)
    for next_state in states:
        if checkValid(next_state,x,y) and (next_state,state[2]) not in visited:
            visited.add((next_state,state[2]))
            parent[next_state]=state
            depthFirstSearch(next_state,x,y,capacity,visited,parent,paths)
            visited.remove((next_state,state[2]))


def Missionary_Cannibal(start,x,y,capacity):
    visited=set()
    paths = set()
    depthFirstSearch(start, x, y, capacity, visited, {}, paths)

    if not paths:
        print("No solution foun")
    else:
        print("Solutions found:")
        for idx, path in enumerate(paths):
            print(f"Solution {idx + 1}: {path}")


#x = int(input("Enter number of missionaries on 1st bank:"))
#y = int(input("Enter the number of cannibals on 1st bank:"))
#capacity = int(input("Enter the capacity:"))

Missionary_Cannibal((3, 3, 0), 3, 3, 2)