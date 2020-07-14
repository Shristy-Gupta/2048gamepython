class Edge:
    def __init__(self,src,dest,wt):
        self.src=src
        self.dest=dest
        self.wt=wt
def getParent(v,parent):
    if(v==parent[v]):
        return v
    return getParent(parent[v],parent)

def kruskal(edges,nVertices):
    parent=[i for i in range(nVertices)]
    edges=sorted(edges, key=lambda edge: edge.wt)
    count = 0
    output = []
    i = 0
    while count < nVertices-1:
        currentEdge=edges[i]
        srcParent=getParent(currentEdge.src,parent)
        destParent=getParent(currentEdge.dest,parent)
        if srcParent!= destParent:
            output.append(currentEdge)
            count+=1
            parent[srcParent]=destParent
        i=i+1
    return output

#vertices
n=int(input())
#edges
e=int(input())
edges=[]
for i in range(e):
    curr_input = [int(ele) for ele in input().strip().split(" ")]
    src=curr_input[0]
    dest=curr_input[1]
    wt=curr_input[2]
    edge=Edge(src,dest,wt)
    edges.append(edge)
output=kruskal(edges,n)
for edge in output:
    if edge.src<edge.dest:
        print(edge.src,edge.dest,edge.wt)
    else:
        print(edge.dest,edge.src,edge.wt)
