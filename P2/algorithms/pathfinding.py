from structures.entry import Entry
from structures.dynamic_array import DynamicArray
from structures.graph import Graph, LatticeGraph
from structures.map import Map
from structures.pqueue import PriorityQueue


def bfs_traversal(
    graph: Graph | LatticeGraph, origin: int, goal: int
    ) -> tuple[DynamicArray, DynamicArray]:
    """
    Task 2.1: Breadth First Search

    @param: graph
      The general graph or lattice graph to process
    @param: origin
      The ID of the node from which to start traversal
    @param: goal
      The ID of the target node

    @returns: tuple[DynamicArray, DynamicArray]
      1. The ordered path between the origin and the goal in node IDs
      (or an empty DynamicArray if no path exists);
      2. The IDs of all nodes in the order they were visited.
    """
    # Stores the keys of the nodes in the order they were visited
    visited_order = DynamicArray()
    # Stores the path from the origin to the goal
    path = DynamicArray()

    discovered = Map()
    visited = PriorityQueue()

    # Initialize BFS
    visited.insert_fifo(origin)
    discovered[origin] = True

    while not visited.is_empty():
        curr = visited.remove_min()
        visited_order.append(curr)

        # Check if we've reached the goal
        if curr == goal:
            while curr != origin:
                path.append(curr)
                curr = discovered[curr]
            path.append(curr)  # Add the origin to the path
            path.reverse()
            return (path, visited_order)

        # Explore neighbours
        for neighbour in graph.get_neighbours(curr):
            nid = neighbour.get_id()

            if discovered[nid] is None:  # Ensure it's not discovered yet
                discovered[nid] = curr
                visited.insert_fifo(nid)

    # If the goal was not reached, return an empty path
    return DynamicArray(), visited_order  

def dijkstra_traversal(graph: Graph, origin: int) -> DynamicArray:
    """
    Task 2.2: Dijkstra Traversal

    @param: graph
      The *weighted* graph to process (POSW graphs)
    @param: origin
      The ID of the node from which to start traversal.

    @returns: DynamicArray containing Entry types.
      The Entry key is a node identifier, Entry value is the cost of the
      shortest path to this node from the origin.

    NOTE: Dijkstra does not work (by default) on LatticeGraph types.
    This is because there is no inherent weight on an edge of these
    graphs. It should of course work where edge weights are uniform.
    """
    valid_locations = DynamicArray()  # Holds the final shortest path results
    shortest = Map()  # To store the shortest known distance to each node
    visited = PriorityQueue()  # Priority queue for exploring nodes by priority (distance)

    # Initialize the Dijkstra algorithm
    for node in range(len(graph._nodes)):  # Assuming you have direct access to nodes
        if node == origin:
            shortest.insert_kv(node, 0)  # Set distance to origin as 0
        else:
            shortest.insert_kv(node, float('inf'))  # Set all other distances to infinity
        visited.insert(shortest[node], node)  # Insert all nodes with their initial distances

    # Main loop to extract and process nodes
    while not visited.is_empty():
        # Get the node with the smallest distance
        node = visited.remove_min()
        current_distance = shortest[node]

        # Store the shortest path to this node
        valid_locations.append(Entry(node, current_distance))

        # Explore the edges of the current node
        for neighbor, weight in graph.get_neighbours(node):
            neighbor_id = neighbor.get_id()
            new_distance = current_distance + weight

            # If a shorter path to the neighbor is found, update it
            if new_distance < shortest[neighbor_id]:
                shortest[neighbor_id] = new_distance
                visited.insert(new_distance, neighbor_id)  # Update the queue with the new distance

    # Return the DynamicArray containing Entry types (node ID and shortest distance)
    return valid_locations


def dfs_traversal(graph: Graph | LatticeGraph, origin: int, goal: int
    ) -> tuple[DynamicArray, DynamicArray]:
    """
    @param: graph
      The general graph or lattice graph to process
    @param: origin
      The ID of the node from which to start traversal
    @param: goal
      The ID of the target node

    @returns: tuple[DynamicArray, DynamicArray]
      1. The ordered path between the origin and the goal in node IDs
      (or an empty DynamicArray if no path exists);
      2. The IDs of all nodes in the order they were visited.
    """
    # Stores the keys of the nodes in the order they were visited
    visited_order = DynamicArray()
    # Stores the path from the origin to the goal
    path = DynamicArray()

    # ALGO GOES HERE

    # Return the path and the visited nodes list
    pass
