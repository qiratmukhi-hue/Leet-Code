from typing import List

class Node:
    __slots__ = ('max_len', 'pref_len', 'suff_len', 'left_char', 'right_char')
    
    def __init__(self, char: str = ''):
        self.max_len = 1 if char else 0
        self.pref_len = 1 if char else 0
        self.suff_len = 1 if char else 0
        self.left_char = char
        self.right_char = char

class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.tree = [Node() for _ in range(4 * self.n)]
        self._build(s, 0, 0, self.n - 1)

    def _merge(self, left: Node, right: Node, left_len: int, right_len: int) -> Node:
        res = Node()
        res.left_char = left.left_char
        res.right_char = right.right_char
        
        res.pref_len = left.pref_len
        res.suff_len = right.suff_len
        res.max_len = max(left.max_len, right.max_len)
        
        if left.right_char == right.left_char:
            cross_len = left.suff_len + right.pref_len
            res.max_len = max(res.max_len, cross_len)
            
            if left.pref_len == left_len:
                res.pref_len = left_len + right.pref_len
            if right.suff_len == right_len:
                res.suff_len = right_len + left.suff_len
                
        return res

    def _build(self, s: str, node: int, l: int, r: int):
        if l == r:
            self.tree[node] = Node(s[l])
            return
        
        mid = (l + r) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        
        self._build(s, left_node, l, mid)
        self._build(s, right_node, mid + 1, r)
        
        self.tree[node] = self._merge(
            self.tree[left_node], 
            self.tree[right_node], 
            mid - l + 1, 
            r - mid
        )

    def update(self, idx: int, char: str, node: int = 0, l: int = 0, r: int = -1):
        if r == -1:
            r = self.n - 1
            
        if l == r:
            self.tree[node] = Node(char)
            return
        
        mid = (l + r) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        
        if idx <= mid:
            self.update(idx, char, left_node, l, mid)
        else:
            self.update(idx, char, right_node, mid + 1, r)
            
        self.tree[node] = self._merge(
            self.tree[left_node], 
            self.tree[right_node], 
            mid - l + 1, 
            r - mid
        )

    def get_max_length(self) -> int:
        return self.tree[0].max_len


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        seg_tree = SegmentTree(s)
        ans = []
        
        for char, idx in zip(queryCharacters, queryIndices):
            seg_tree.update(idx, char)
            ans.append(seg_tree.get_max_length())
            
        return ans