from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val

        def dfs(curr: str, target: str, visited: set) -> float:
            if curr not in graph or target not in graph:
                return -1.0
            if curr == target:
                return 1.0
            
            visited.add(curr)
            
            for neighbor, weight in graph[curr].items():
                if neighbor not in visited:
                    res = dfs(neighbor, target, visited)
                    if res != -1.0:
                        return weight * res
            
            return -1.0

        results = []
        for src, dst in queries:
            results.append(dfs(src, dst, set()))
            
        return results