# Drawn Shapes Dataset

[![Buy me a coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/tonyb)

Dataset of paths coordinates of drawn shapes.

Also script for processing data to images and binary CSV matrices is included.

## Shapes in dataset

All shapes was drawn by by hand on canvas 256x256px with apple pencil and iPad Pro.
Most of them was drawn in one stroke, but few of them with more strokes.

__Total count:__ 3045

- circle (511x)
- diamond (465x)
- oval (557x)
- rectangle (463x)
- square (574x)
- triangle (475x)

### Data structure

In directory `paths` are JSON files of shape paths separated to directories by shape type.

Each shape is array of drawn paths and each path is array of point coordinates:

__Example:__

```
[
  [
    ["125","91.1875"],
    ["125","91.1875"],
    ["122","89.1875"],
    ["122","89.1875"],
    ...
  ],
  [
    ["125","91.1875"],
    ["125","91.1875"],
    ["122","89.1875"],
    ["122","89.1875"].
    ...
  ],
  ...
]
```

## Path processor

Python script `process.py` suppose to convert paths to images and binary CSV matrices.

When you run script if will fill directories `output/images` and `output/binary` with data separated
to subdirectories by types.

For modify output you can change config on beginning of the script 

```python
OUTPUT_SIZE = 28
OUTPUT_DRAWN_PATH_THICKNESS = 1
OUTPUT_SHAPE_PADDING = 2
```

### Output image examples:

![circle](https://github.com/antoninbouchal/drawn-shapes-dataset/raw/master/examples/0.00089200%201567776990.png)
![diamond](https://github.com/antoninbouchal/drawn-shapes-dataset/raw/master/examples/0.00292400%201567777236.png)
![oval](https://github.com/antoninbouchal/drawn-shapes-dataset/raw/master/examples/0.00080600%201567776567.png)
![rectangle](https://github.com/antoninbouchal/drawn-shapes-dataset/raw/master/examples/0.00178700%201567787745.png)
![square](https://github.com/antoninbouchal/drawn-shapes-dataset/raw/master/examples/0.00035800%201567776476.png)
![triangle](https://github.com/antoninbouchal/drawn-shapes-dataset/raw/master/examples/0.00177900%201567778143.png)
