n = int(input())
total = 0
faces = {"Tetrahedron":4,"Cube":6,"Octahedron":8,"Dodecahedron":12,"Icosahedron":20}
for i in range(n):
    total += faces[input()]

print(total)
