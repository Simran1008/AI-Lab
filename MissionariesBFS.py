def generateNext(state,capacity):
    m=state[0]
    n=state[1]
    c=state[2]
    if(c==0):
        output=set()
        for i in range(0,capacity+1):
            for j in range(0,capacity+1):
                if((i!=0 or j!=0) and i<=j):
                    output.add((m-i,n-j+i,1))
        return output
    elif(c==1):
        output=set()
        for i in range(0,capacity+1):
            for j in range(0,capacity+1):
                if((i!=0 or j!=0) and i<=j):
                    output.add((m+i,n+j-i,0))
        return output


def checkvalid(state,x,y):
    m=state[0]
    c=state[1]
    # print(state)
    #if m>x or c>y or (x-m)>x or (y-c)>y or m<0 or c<0 or (x-m)<0 or (y-c)<0:
        #return 0
    if m>0 and m<c:
        return 0
    elif (x-m)>0 and (x-m)<(y-c):
        return 0
    
    return 1


def Missionary_Cannibal(start,x,y,capacity):
    visited=[]
    queue=[]
    queue.append(start)
    parent={start:(0,0,-1)}
    visited.append(start)
    state = (0,0,1)
    while queue:
        state=queue.pop(0)
        if state==(0,0,1):
            break
        states=generateNext(state,capacity)
        for nextstate in states:
            if checkvalid(nextstate,x,y) and nextstate not in visited:
                queue.append(nextstate)
                visited.append(nextstate)
                parent[nextstate]=state
    if state!=(0,0,1):
        print("No solution found")
    else:
        path=[]
        while(state!=(0,0,-1)):
            path.append(state)
            state=parent[state]
        path=path[::-1]
        print(path)

        
#x=int(input("Enter number of missionaries on bank 1: "))
#y=int(input("Enter number of cannibals on bank 1: "))
#capacity=int(input("Enter the capacity of the boat: "))

Missionary_Cannibal((3,3,0),3,3,2)