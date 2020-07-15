import sys
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for n in range(nVertices)] for m in range(nVertices)]
    #Building adjacency matrix with respective weights
    def addEdge(self,v1,v2,wt):
        self.adjMatrix[v1][v2]=wt
        self.adjMatrix[v2][v1]=wt
    #Buidling minvertex
    def __getMinVertex(self,visited,weight):
        #lastnode
        minvertex=-1
        for i in range(self.nVertices):
            if visited[i] is False and (minvertex==-1 or weight[minvertex]>weight[i]):
                minvertex=i
        return minvertex
    #Prims algo
    def prims(self):
        #List of visited nodes initalized to false
        visited=[False for i in range(self.nVertices)]
        #List of parent nodes initialized to -1
        parent=[-1 for i in range(self.nVertices)]
        #List of weight of each nodes in graph initialized with max size
        weight=[sys.maxsize for i in range(self.nVertices)]
        #First node is initialized with zero weight
        weight[0]=0
        
        for i in range(self.nVertices-1):
            min_vertex=self.__getMinVertex(visited,weight)
            visited[min_vertex]=True
            '''
            Explore the neighbours of minVertex which is not visited and update the weight 
            corresponding to each vertex
            '''
            for j in range(self.nVertices):
                if self.adjMatrix[min_vertex][j]>0 and visited[j] is False:
                    if weight[j]>self.adjMatrix[min_vertex][j]:
                        weight[j]=self.adjMatrix[min_vertex][j]
                        parent[j]=min_vertex
            
        #Printing the MST
        for i in range(1,self.nVertices):
            if i<parent[i]:
                print(i,parent[i],weight[i])
            else:
                print(parent[i],i,weight[i])


'''
Building Input
1st Line with have Vertex 'V' and Edges 'E' separated by space.
Next it will have 'E'no. of lines depicting Edge Three integers 
ei, ej and wi, denoting that there exists an edge between vertex ei 
and vertex ej with weight wi (separated by space)
'''
li=[int(ele) for ele in input().strip().split()]
V=li[0]
E=li[1]
#creating adjacency matrix with above info.
g=Graph(V)
for i in range(E):
    edge_info=[int(ele) for ele in input().strip().split()]
    ei=edge_info[0]
    ej=edge_info[1]
    wi=edge_info[2]
    g.addEdge(ei,ej,wi)
g.prims()