Author: Raul Zaldana-Calles
Date: July 6, 2021

Hello,

This repository keeps track of my experiments with Blender's Python API.

I'm particularly interested in generating meshes that look interesting.

Eventually, I want to experiment with the generative placement of meta balls to create organic-looking 3D shapes.

I then want to combine those shapes with noise-based displacement shaders to create coloring schemes that look life-like.

We'll see how it goes :)

Next steps:
- Reorganize files (create a folder for scripts and a folder for images)
- Experiment with size and placement of metaballs to create different structures
- Experiment with deforming metaballs structure
- Render current metaballs structure (Done)
- Figure out how metaballs objects work (is there a mesh associated to the object? A mesh substitute?)
- Create a row of meta-balls that connect (all same size and then different size) (DONE. result: metaballs.py)
- Make a cube with bmesh
- Complete this tutorial: https://www.youtube.com/watch?v=mljWBuj0Gho&list=RDCMUCzghqpGuEmk4YdVewxA79GA&index=2 (DONE - result: createMeshFromScratch.py)


List of Scripts:

- addObjectScript.py : 
    Basic script to get acquainted with Python scripting environment
- addObjectwithModifiers.py : 
    script made by following youtube tutorial (https://www.youtube.com/watch?v=XqX5wh4YeRw&t=8s) to create an object with modifiers from the Python console
- createMeshFromScratch.py :
	script to create and display an object by creating the mesh
- EasyBPYtest.py : 
	A script to test that the EasyBPY module is imported correctly

Organization:
- Only create new branch when you render something

Modules:
- EasyBPY: provides plain English wrappers for data-block references and functions (To install, copy the EasyBPY.py file to C:/Users/[User]/AppData/Roaming/BlenderFoundation/Blender/[Blender Version]/scripts/modules. If any of the directories doesn't exist, create it)

Sources:
- 3 point lighting: https://www.youtube.com/watch?v=RDbrOpnIY7Q

Noise:
- Noise functions in Blender are in the mathutils.noise module
	- e.g. mathutils.noise.noise(), mathutils.noise.hetero_terrain()
- Noise functions return the same value for all integer co-ordinates
	- e.g. (1, 0, 0) returns the same noise value as (2, 0, 0) and (3, 0, 0)
- But they return different values for (1.1, 0, 0) and (2.1, 0, 0)
- Overall, it's best to keep the step in between the different values < 1


