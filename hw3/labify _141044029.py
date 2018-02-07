
def connectedGraphs(mapOfGTU, index, visited, graph):
    
    tempMap = mapOfGTU
    if (visited[index] != True ): 	
        graph.append(index+1)		# key kısmının eklendiği yer
        visited[index] = True

    keys = []
    for i in range(len(mapOfGTU[index+1])):		# index+1  key değerini verir
        temp = tempMap[index+1].pop()			# temp = value
        if (visited[temp-1] != True ):
            graph.append(temp)			# value kısmının eklendiği yer
            visited[temp-1] = True 
            keys.append(temp)  


    for i in range(len(keys)):
        connectedGraphs(mapOfGTU, keys[i]-1, visited, graph)		# 	bağlantılı edge'leri bulmak için set deki value değerlerini 
    else:														# key olarak kullanarak recursion
        return




def findMinimumCostToLabifyGTU(x, y, mapOfGTU):

    size = len(mapOfGTU.keys())
    visited = [False]*size
    
    graphs = []			# tüm bağlantılı map'leri içeren değişken
    for i in range(size):
        if(visited[i] != True):
        	graph = []	# bağlantılı map
	        connectedGraphs(mapOfGTU, i, visited, graph)
	        if(len(graph) != 0):
	            graphs.append(graph)


    #print(graphs)        
    
    result =0
    for i in range(len(graphs)):
        result += y*( len(graphs[i])-1 )	
        										# cost hesabı,  x build , y repair
    result += x*len(graphs)

    return result



mapOfGTU = {
            1 : set([2,3]),
            2 : set([1,3]),
            3 : set([1,2])
                            } # graph is initialized as dictionary

minCost = findMinimumCostToLabifyGTU(2,1,mapOfGTU)
print(minCost)# Output will be 4



mapOfGTU = {
            1 : set([2,3]),
            2 : set([1,3,4]),
            3 : set([1,2,4]),
            4 : set([3,2]),
            5 : set([6]),
            6 : set([5])
                                }# graph is initialized as dictionary

minCost = findMinimumCostToLabifyGTU(5,2,mapOfGTU)
print(minCost)# Output will be 18