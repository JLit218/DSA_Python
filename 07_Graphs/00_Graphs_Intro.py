# Vertex or Vertices connected by Edges
# A vertex can edge to as many or little other vertices.
# weighted edges - one direction may be inefficient (a heavier edge) a busy street on google maps, or a slow connection between IPs in a network configuration vs 2 quicker hops
# Trees and links are limited versions of graphs (can only point 1 direction)

# Adjacency Matrix
# Must store all of the edges that are not connect
# O(vertices^2)
# quicker at removing already existing vertex/edge

# # # # # # # # #
#    A B C D E  #
#  A 0 1 0 0 1  #
#  B 1 0 1 0 0  #
#  C 0 1 0 1 0  #
#  D 0 0 1 0 1  #
#  E 1 0 0 1 0  #
# # # # # # # # #


# Adjacency Lists
# Does not store unconnected edges
# O(vertices + edges)
# quicker for adding vertex
{
    'A': ['B', 'E'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['A', 'D']
}
