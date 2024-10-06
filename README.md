# Blot3DRenderer

## Overview
Blot3DRenderer is a simple 3D renderer designed for [Hack Club Blot](https://blot.hackclub.com). It takes in 3D files using [Trimesh](https://trimsh.org) (such as STL, OBJ, etc.) and generates polylines that can be used for rendering purposes in your projects.

## Features
- Supports various 3D file formats, including:
  - **STL** (Stereolithography)
  - **OBJ** (Wavefront Object)
  - **PLY** (Polygon File Format)
  - **GLTF/GLB** (GL Transmission Format)
  - **3MF** (3D Manufacturing Format)
- Simple user interface for loading files, setting scale and focal length, and generating output.
- Outputs a copy/pastable format for rendering in Hack Club Blot.

## Installation
To use Blot3DRenderer, ensure you have Python 3.x installed on your system and clone into this directory. You can install the required libraries using pip:

```bash
pip install trimesh
```


## Usage
1. **Run the Script**: Open a terminal and execute the script:
```python mainui.py```

2. **Load a 3D File**: Enter the path to your 3D file in the provided input field.

3. **Set Parameters**:
- **Scale**: Specify a scale factor for the output (default: 1000).
- **Focal Length**: Specify the focal length for the perspective projection (default: 0.015 for a "70(ish)mm lens").

4. **Generate Output**: Click the "Load and Project" button to process the file and generate the output code.

5. **Copy Output**: Use the "Copy Output" button to copy the generated code for use in your rendering projects.

## Example
Given a 3D model file `example.obj`, set the desired scale and focal length, and run the renderer to get the corresponding polylines for rendering.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the functionality or usability of the renderer.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
