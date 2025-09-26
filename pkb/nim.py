graph = { 
    '2A': ['5B', '2C'],   
    '5B': ['2A','4D', '1E'],
    '2C': ['2A','0F','1G'],
    '4D': ['5B','0H'],
    '0H': ['4D'],
    '1E': ['5B','1I'], 
    '1I': ['1E'],
    '0F': ['2C','0J'],
    '0J': ['0F'],
    '1G': ['2A','9K'],
    '9K': ['1G','0L'],
    '0L': ['9K']
}
   

# BFS
queue = [] 
visited =  []

def bfs(visited, graph, node):  
     visited.append(node) 
     queue.append(node) 
     while queue:       
            m = queue.pop(0) 
            print (m, end = " ") 
            for neighbour in graph[m]:    
                if neighbour not in visited: 
                    visited.append(neighbour) 
                    queue.append(neighbour)                         
print("Urutan node yang dikunjungi :") 
bfs(visited, graph, '2A') 



#DFS
visited = set() 
# visited =  [] ini diperlukan jika line 43 menggunakan methode .append(node)

def dfs(visited, graph, node):     
    if node not in visited:         
        print (node)       
        visited.add(node)        
        for neighbour in graph[node]:             
            dfs(visited, graph, neighbour) 

print("urutan node yang dikunjungi (dengan metode bfs):") 
dfs(visited, graph, '2A') 