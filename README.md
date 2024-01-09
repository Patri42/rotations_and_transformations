# 3D Vector Rotation and Transformation Demonstrations

This repository contains a collection of Python scripts that demonstrate the process of rotating 3D vectors using rotation matrices and Euler angles. The scripts utilize the `numpy` library to perform matrix operations and showcase how vectors transform in three-dimensional space.

## What's Inside

- `changing_multiple_rotations.py`: Demonstrates sequential rotations around the x-axis using rotation matrices. It shows how multiple rotations transform a vector step-by-step and how combining these rotations yields the same result as a single, equivalent rotation.
- `single_axis_dcm.py`: Showcases the application of a rotation matrix to rotate a vector around the x-axis by a specific angle, demonstrating the transformation of vector components in 3D space.
- `rotation_interpolation.py`:This script illustrates linear interpolation between two rotation matrices around the X-axis, showcasing a method for smooth transitions between different 3D rotations.
- `euler_angles_to_dcm.py`: Provides an implementation for converting Euler angles to a direction cosine matrix (DCM) and back. It demonstrates how to apply Euler angles for rotations in 3D space and how to extract these angles back from the rotation matrix.

## Future Updates

As time progresses, I will be adding more scripts and examples that cover:
- Rotations around the y-axis and z-axis.
- Combinations of rotations around multiple axes.
- More complex transformations and their applications.

Stay tuned for updates, and feel free to contribute or use these demonstrations as a learning resource or a starting point for your own projects!
