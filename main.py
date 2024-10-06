import trimesh

# Load an OBJ or STL file
mesh = trimesh.load('example.stl')  # Replace with your file path

# Get the list of vertices (points)
vertices = mesh.vertices

# Get the edge table
edges = mesh.edges

scale = 1000

focal_length = 1/70

projected_vertices = []

# Project the vertices onto 2D plane using perspective projection
for vertex in vertices:
    x = vertex[0]
    y = vertex[1]
    z = vertex[2]
    print(f"x:{x} y:{y} z:{z}")
    if z != 0:  # Ensure we don't divide by zero
        x_projected = -(focal_length * x) / z
        y_projected = -(focal_length * y) / z
    else:
        x_projected = x  # Handle z=0 case (might not occur in normal meshes)
        y_projected = y
    
    # Append the 2D projected point to the list
    projected_vertices.append([x_projected, y_projected])

# Prepare output string for the code
output = []
output.append("//copy/pastable code for blot drawing:\n")

for i, edge in enumerate(edges):
    line = f"""const polyline{i} = [
  [{projected_vertices[edge[0]][0]*scale}, {projected_vertices[edge[0]][1]*scale}],
  [{projected_vertices[edge[1]][0]*scale}, {projected_vertices[edge[1]][1]*scale}]
          ];\n"""
    line += f"finalLines.push(polyline{i});\n"
    output.append(line)

# Write the output to a file for easier copying
with open('output.txt', 'w') as f:
    f.writelines(output)
