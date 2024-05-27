# Dijkstra's Algorithm

## Pseudocode
```python
function Dijkstra(Graph, source):

  create vertex set Q

  for each vertex v in Graph:
      dist[v] ← INFINITY
      prev[v] ← UNDEFINED
      add v to Q
  dist[source] ← 0

  while Q is not empty:
      u ← vertex in Q with min dist[u]

      remove u from Q

      for each neighbor v of u still in Q:
          alt ← dist[u] + length(u, v)
          if alt < dist[v]:
              dist[v] ← alt
              prev[v] ← u

  return dist[], prev[]
```

## Pseudocode with Priority
```python
function Dijkstra(Graph, source):
  dist[source] ← 0                           // Initialization

  create vertex priority queue Q

  for each vertex v in Graph:
      if v ≠ source
          dist[v] ← INFINITY                 // Unknown distance from source to v
          prev[v] ← UNDEFINED                // Predecessor of v

      Q.add_with_priority(v, dist[v])


  while Q is not empty:                      // The main loop
      u ← Q.extract_min()                    // Remove and return best vertex
      for each neighbor v of u:              // only v that are still in Q
          alt ← dist[u] + length(u, v)
          if alt < dist[v]
              dist[v] ← alt
              prev[v] ← u
              Q.decrease_priority(v, alt)

  return dist, prev
```
