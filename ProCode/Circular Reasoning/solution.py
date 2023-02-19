from collections import defaultdict
class Network:

    def nodes_visited(self, total_nodes, starting_node, nodes_to_visit):
        # Your code goes here
        if total_nodes <= 0:
            return 0
        if starting_node > total_nodes:
            return 0
        if not nodes_to_visit:
            return 0
        
        visited = defaultdict(bool)
        current_node = starting_node
        for node_to_visit in nodes_to_visit:
            if node_to_visit > total_nodes or node_to_visit < 1:
                continue
            visited, current_node = self.nodes_visited_to_one(total_nodes, current_node, node_to_visit, visited)
            total_visited = sum(visited.values())
            if total_visited == total_nodes:
                break
        return total_visited
        
    def nodes_visited_to_one(self, total_nodes, current_node, node_to_visit, visited):
        
        next_node = current_node+1 if current_node+1 <=total_nodes else 1
        if node_to_visit > current_node:
            for i in range(next_node, node_to_visit+1):
                visited[i] = True
        elif node_to_visit < current_node:
            for i in range(next_node, total_nodes+1):
                visited[i] = True
            for i in range(1,node_to_visit+1):
                visited[i] = True
        else:
            visited[current_node] = True
        return visited, node_to_visit        
          
result = Network()
result.nodes_visited(4, 3, [ 2,4 ])        