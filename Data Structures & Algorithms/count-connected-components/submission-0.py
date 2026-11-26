class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent=list(range(n))
        size=[1] * n

        components=n

        def find(node):
            if parent[node]!=node:
                parent[node]=find(parent[node])
            return parent[node]
        
        def union(a,b):

            root_a=find(a)
            root_b=find(b)

            if root_a==root_b:
                return False
            
            # connect smaller component to larger one

            if size[root_a]<size[root_b]:
                root_a,root_b=root_b,root_a
            size[root_a]+=size[root_b]
            
            parent[root_b]=root_a
            return True

        for a,b in edges:
            if union(a,b):
                components-=1
        
        return components

