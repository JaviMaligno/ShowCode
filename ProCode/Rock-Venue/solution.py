class Seating:

    def largest_block(self, layout):
        # Your code goes here
        n = len(layout)
        m = len(layout[0])
        nodes = [(a,b) for a in range(n) for b in range(m)]
        graph = self.adjacency(nodes,layout,n,m)
        components = list(map(set,self.connected_components(graph)))
        if len(components)==1:
            return layout[0][0]
        sorted_components = sorted(components, key=lambda x: (-len(x), min(x)))
        largest = sorted_components[0]
        second_largest = sorted_components[1]
        if len(sorted_components) == 2:
            if self.symbol(layout,largest) == "X":
                largest = second_largest
            elif self.symbol(layout,largest) == "O" and self.symbol(layout,second_largest) !="X":
                largest = second_largest
                
        else:
            third_largest = sorted_components[2]
            if self.symbol(layout,largest) in {"X", "O"}:
                if self.symbol(layout,second_largest) in {"X","O"}:
                    largest = third_largest
                else:
                    largest = second_largest
                
        return self.symbol(layout, largest)
    

    def symbol(self, layout, component):
        return next(map(lambda x: layout[x[0]][x[1]], component))
       
    def adjacency(self,nodes, layout,n,m):
        adjacency = {}
        for node in nodes:
           adjacency[node] = self.adjacents(node,layout,n,m)
        return adjacency
        
    @staticmethod    
    def adjacents(node,layout,n,m):
        symbol = layout[node[0]][node[1]]
        if node[0] == 0:
            if node[1] == 0:
                candidates = [(node[0]+1, node[1]), (node[0],node[1]+1)]
            elif node[1]==m-1:
                candidates = [(node[0]+1, node[1]), (node[0],node[1]-1)]
            else:
                candidates = [(node[0]+1, node[1]), (node[0],node[1]+1), (node[0],node[1]-1)]
        elif node[0] == n-1:
            if node[1] == 0:
                candidates = [(node[0]-1, node[1]), (node[0],node[1]+1)]
            elif node[1] == m-1:
                candidates = [(node[0]-1, node[1]), (node[0],node[1]-1)]
            else:
                candidates = [(node[0]-1, node[1]), (node[0],node[1]-1), (node[0],node[1]+1)]
        elif node[1] == 0:
            candidates = [(node[0]-1, node[1]), (node[0]+1,node[1]), (node[0],node[1]+1)]
        elif node[1] == m-1:
            candidates = [(node[0]-1, node[1]), (node[0]+1,node[1]), (node[0],node[1]-1)]
        else:
            candidates = [(node[0]-1, node[1]), (node[0]+1,node[1]), (node[0],node[1]-1), (node[0],node[1]+1)]
        return set([x for x in candidates if x[0]<n and x[1]<m and layout[x[0]][x[1]] == symbol])
        
    
    
    def connected_components(self,neighbors):
        seen = set()
        def component(node):
            nodes = set([node])
            while nodes:
                node = nodes.pop()
                seen.add(node)
                nodes |= neighbors[node] - seen
                yield node
        for node in neighbors:
            if node not in seen:
                yield component(node)
