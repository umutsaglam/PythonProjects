# Kenar listesi ve düğümleri tanımlıyoruz
edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('A', 'D', 10),
    ('B', 'C', 5),
    ('B', 'D', 3),
    ('C', 'E', 8),
    ('D', 'E', 4),
    ('D', 'F', 6),
    ('E', 'F', 1)
]

# Union-Find veri yapısını tanımlıyoruz
class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

# Kruskal algoritması
def kruskal(nodes, edges):
    uf = UnionFind(nodes)
    mst = []
    total_weight = 0

    # Kenarları ağırlığa göre sırala
    sorted_edges = sorted(edges, key=lambda edge: edge[2])

    for edge in sorted_edges:
        node1, node2, weight = edge

        # Döngü oluşturmadan ekle
        if uf.find(node1) != uf.find(node2):
            uf.union(node1, node2)
            mst.append(edge)
            total_weight += weight

    return mst, total_weight

# Düğümleri ve MST'yi hesapla
nodes = {'A', 'B', 'C', 'D', 'E', 'F'}
mst, total_weight = kruskal(nodes, edges)
print("Minimum Yayılan Ağaç:", mst)
print("Toplam Ağırlık:", total_weight)
