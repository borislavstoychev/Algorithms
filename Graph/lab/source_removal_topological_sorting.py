from collections import deque


def find_dependencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1
    return result


def find_node_to_remove(dep):
    for node, count in dep.items():
        if count == 0:
            return node


def remove_independent_nodes(dependencies, sorted_nodes, graph):
    while dependencies:
        node_to_remove = find_node_to_remove(dependencies)
        sorted_nodes.append(node_to_remove)
        if node_to_remove is None:
            break
        dependencies.pop(node_to_remove)
        for child in graph[node_to_remove]:
            dependencies[child] -= 1

    print(f"Topological sorting: {', '.join(sorted_nodes)}") if not dependencies else print(
        "Invalid topological sorting")


def main():
    nodes_count = int(input())
    graph = {}
    for _ in range(nodes_count):
        key, value = input().split(' ->')
        graph[key] = value.strip().split(', ') if value else []
    dependencies = find_dependencies(graph)
    sorted_nodes = deque()
    remove_independent_nodes(dependencies, sorted_nodes, graph)
    # dfs_topological_sorting(graph, sorted_nodes)


def top_sort_dfs(node, sorted_nodes, graph, visited, cycles):
    if node in cycles:
        raise Exception("Invalid topological sorting")
    if node in visited:
        return
    visited.add(node)
    cycles.add(node)
    for child in graph[node]:
        top_sort_dfs(child, sorted_nodes, graph, visited, cycles)
    sorted_nodes.appendleft(node)
    cycles.remove(node)


def dfs_topological_sorting(graph, sorted_nodes):
    visited = set()
    cycles = set()
    for node in graph:
        top_sort_dfs(node, sorted_nodes, graph, visited, cycles)
    print(*sorted_nodes, sep=", ")


main()
