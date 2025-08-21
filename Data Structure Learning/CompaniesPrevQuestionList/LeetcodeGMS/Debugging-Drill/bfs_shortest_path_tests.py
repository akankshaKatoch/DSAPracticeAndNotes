from bfs_shortest_path_bug import shortest_path

def run():
    n = 6
    edges = [(0,1),(1,2),(2,3),(3,4),(4,5)]
    assert shortest_path(n, edges, 0, 5) == 5
    assert shortest_path(n, edges, 0, 0) == 0
    # unreachable
    edges2 = [(0,1),(2,3)]
    assert shortest_path(4, edges2, 0, 3) == -1
    print("BFS tests passed")

if __name__ == "__main__":
    run()
