import trimesh
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Function to load the 3D file and process vertices and edges
def process_file(input_file, scale, focal_length):
    try:
        # Load an OBJ or STL file
        mesh = trimesh.load(input_file)

        # Get the list of vertices (points)
        vertices = mesh.vertices

        # Get the edge table
        edges = mesh.edges

        projected_vertices = []

        # Project the vertices onto a 2D plane using perspective projection
        for vertex in vertices:
            x = vertex[0]
            y = vertex[1]
            z = vertex[2]

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
  [{projected_vertices[edge[0]][0] * scale}, {projected_vertices[edge[0]][1] * scale}],
  [{projected_vertices[edge[1]][0] * scale}, {projected_vertices[edge[1]][1] * scale}]
          ];\n"""
            line += f"finalLines.push(polyline{i});\n"
            output.append(line)

        # Return the generated output
        return ''.join(output)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to process file: {e}")
        return ""

# Function to open file dialog
def select_file():
    file_path = filedialog.askopenfilename()
    file_input.delete(0, tk.END)
    file_input.insert(0, file_path)

# Function to generate the output code
def generate_output():
    input_file = file_input.get()
    scale = float(scale_input.get())
    focal_length = float(focal_length_input.get())

    if input_file:
        output_code = process_file(input_file, scale, focal_length)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, output_code)
    else:
        messagebox.showwarning("Input Required", "Please select a 3D file.")

# Function to copy the output to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_text.get(1.0, tk.END))
    messagebox.showinfo("Copied", "Output copied to clipboard.")

# Create the UI window
root = tk.Tk()
root.title("Blot 3D Projection Tool")

# File selection
tk.Label(root, text="Select 3D File:").grid(row=0, column=0, padx=10, pady=5)
file_input = tk.Entry(root, width=50)
file_input.grid(row=0, column=1, padx=10, pady=5)
file_button = tk.Button(root, text="Browse", command=select_file)
file_button.grid(row=0, column=2, padx=10, pady=5)

# Scale input
tk.Label(root, text="Scale:").grid(row=1, column=0, padx=10, pady=5)
scale_input = tk.Entry(root, width=10)
scale_input.insert(0, "1000")
scale_input.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Focal length input
tk.Label(root, text="Focal Length:").grid(row=2, column=0, padx=10, pady=5)
focal_length_input = tk.Entry(root, width=10)
focal_length_input.insert(0, str(0.015))
focal_length_input.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Output text area
tk.Label(root, text="Output:").grid(row=3, column=0, padx=10, pady=5)
output_text = tk.Text(root, width=70, height=20)
output_text.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

# Buttons for generating and copying output
generate_button = tk.Button(root, text="Generate", command=generate_output)
generate_button.grid(row=5, column=0, padx=10, pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=5, column=1, padx=10, pady=10)

# Start the Tkinter main loop
root.mainloop()
