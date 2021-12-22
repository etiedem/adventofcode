# Flood Fill
Two functions required for algorithm
1. Inside
    - returns ```True``` for unfilled points that would be inside the filled area
2. Set
    - fills a node. Any node that has Set called on it must then no longer be Inside

## Algorithm
```
Flood-fill (node):
1. If node is not Inside return.
2. Set the node
3. Perform Flood-fill south
4. Perform Flood-fill north
5. Perform Flood-fill west
6. Perform Flood-fill east
7. Return
```

### Optimized
```
fn fill(x, y):
  if not Inside(x, y) then return
  let s = new empty queue or stack
  Add (x, x, y, 1) to s
  Add (x, x, y - 1, -1) to s
  while s is not empty:
    Remove an (x1, x2, y, dy) from s
    let x = x1
    if Inside(x, y):
      while Inside(x - 1, y):
        Set(x - 1, y)
        x = x - 1
    if x < x1:
      Add (x, x1-1, y-dy, -dy) to s
    while x1 < x2:
      while Inside(x1, y):
        Set(x1, y)
        x1 = x1 + 1
      Add (x, x1 - 1, y+dy, dy) to s
      if x1 - 1 > x2:
        Add (x2 + 1, x1 - 1, y-dy, -dy)
      while x1 < x2 and not Inside(x1, y):
        x1 = x1 + 1
      x = x1
```
