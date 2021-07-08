import bpy
import random

# Select all objects from previous run
bpy.ops.object.select_all(action='SELECT')

# Deselect Camera and Light
bpy.data.objects['Camera'].select_set(False)
bpy.data.objects['Light'].select_set(False)

# Delete all selected objects (i.e. all objects except Camera and Light
bpy.ops.object.delete()
 

for x in range(-5,6):
    z = 0
    if (x%2)==0:
        z = 1
    bpy.ops.object.metaball_add(type='BALL', radius=random.randint(1, 2), enter_editmode=False, align='WORLD', location=(x, 0, z), scale=(1, 1, 1))
    so = bpy.context.active_object




