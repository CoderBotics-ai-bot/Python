import sys
from collections import defaultdict


class Heap:
    def __init__(self):
        self.node_position = []

    def get_position(self, vertex):
        return self.node_position[vertex]

    def set_position(self, vertex, pos):
        self.node_position[vertex] = pos

    def top_to_bottom(self, heap, start, size, positions):
        if start > size // 2 - 1:
            return
        else:
            if 2 * start + 2 >= size:
                smallest_child = 2 * start + 1
            else:
                if heap[2 * start + 1] < heap[2 * start + 2]:
                    smallest_child = 2 * start + 1
                else:
                    smallest_child = 2 * start + 2
            if heap[smallest_child] < heap[start]:
                temp, temp1 = heap[smallest_child], positions[smallest_child]
                heap[smallest_child], positions[smallest_child] = (
                    heap[start],
                    positions[start],
                )
                heap[start], positions[start] = temp, temp1

                temp = self.get_position(positions[smallest_child])
                self.set_position(
                    positions[smallest_child], self.get_position(positions[start])
                )
                self.set_position(positions[start], temp)

                self.top_to_bottom(heap, smallest_child, size, positions)

    # Update function if value of any node in min-heap decreases
    def bottom_to_top(self, val, index, heap, position):
        temp = position[index]

        while index != 0:
            parent = int((index - 2) / 2) if index % 2 == 0 else int((index - 1) / 2)

            if val < heap[parent]:
                heap[index] = heap[parent]
                position[index] = position[parent]
                self.set_position(position[parent], index)
            else:
                heap[index] = val
                position[index] = temp
                self.set_position(temp, index)
                break
            index = parent
        else:
            heap[0] = val
            position[0] = temp
            self.set_position(temp, 0)

    def heapify(self, heap, positions):
        start = len(heap) // 2 - 1
        for i in range(start, -1, -1):
            self.top_to_bottom(heap, i, len(heap), positions)

    def delete_minimum(self, heap, positions):
        temp = positions[0]
        heap[0] = sys.maxsize
        self.top_to_bottom(heap, 0, len(heap), positions)
        return temp


def prisms_algorithm(ref_adjacency_list: dict) -> list:
    heap, visited, nbr_tv, distance_tv, positions = prepare_heap_data(
        ref_adjacency_list
    )

    tree_edges = []
    for _ in range(1, len(ref_adjacency_list)):
        vertex = heap.delete_minimum(distance_tv, positions)
        if visited[vertex] == 0:
            tree_edges.append((nbr_tv[vertex], vertex))
            update_heap_data(
                vertex,
                distance_tv,
                positions,
                heap,
                ref_adjacency_list,
                nbr_tv,
                visited,
            )

    return tree_edges


if __name__ == "__main__":  # pragma: no cover
    # < --------- Prims Algorithm --------- >
    edges_number = int(input("Enter number of edges: ").strip())
    adjacency_list = defaultdict(list)
    for _ in range(edges_number):
        edge = [int(x) for x in input().strip().split()]
        adjacency_list[edge[0]].append([edge[1], edge[2]])
        adjacency_list[edge[1]].append([edge[0], edge[2]])
    print(prisms_algorithm(adjacency_list))

def prepare_heap_data(adjacency_list: dict):
    heap = Heap()

    visited = [0] * len(adjacency_list)
    nbr_tv = [-1] * len(adjacency_list)
    distance_tv, positions = [], []
    for vertex in range(len(adjacency_list)):
        distance_tv.append(sys.maxsize)
        positions.append(vertex)
        heap.node_position.append(vertex)

    return heap, visited, nbr_tv, distance_tv, positions


def update_heap_data(
    vertex: int,
    distance_tv: list,
    positions: list,
    heap: Heap,
    adjacency_list: dict,
    nbr_tv: list,
    visited: list,
):
    visited[vertex] = 1
    for neighbor, distance in adjacency_list[vertex]:
        if (
            visited[neighbor] == 0
            and distance < distance_tv[heap.get_position(neighbor)]
        ):
            distance_tv[heap.get_position(neighbor)] = distance
            heap.bottom_to_top(
                distance, heap.get_position(neighbor), distance_tv, positions
            )
            nbr_tv[neighbor] = vertex
