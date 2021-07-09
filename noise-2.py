import bpy
from mathutils.noise import hetero_terrain as ht
context = bpy.context

# Select all objects from previous run
bpy.ops.object.select_all(action='SELECT')

# Deselect Camera and Light
bpy.data.objects['Camera'].select_set(False)
bpy.data.objects['Light'].select_set(False)

# Delete all selected objects (i.e. all objects except Camera and Light
bpy.ops.object.delete()

H = 0.4
lacunarity = 1
octaves = 1
offset = 0.3
noise_basii =  (
    'BLENDER', 
    'PERLIN_ORIGINAL', 
    'PERLIN_NEW', 
    'VORONOI_F1', 
    'VORONOI_F2', 
    'VORONOI_F3', 
    'VORONOI_F4', 
    'VORONOI_F2F1', 
    'VORONOI_CRACKLE', 
    'CELLNOISE')
    
bpy.ops.mesh.primitive_grid_add(
        size=10,
        x_subdivisions=100,
        y_subdivisions=100
        )
        
ob = context.object
me = ob.data

for v in me.vertices:
    noise_val = ht( v.co,
                                    H,
                                    lacunarity,
                                    octaves,
                                    offset,
                                    noise_basis='BLENDER'
                                    )
    v.co.z = noise_val

'''
sk = ob.shape_key_add(name="Basis")

for nb in noise_basii:
    sk = ob.shape_key_add(name=nb)

    for v in me.vertices:
        sk.data[v.index].co.z = ht( v.co,
                                    H,
                                    lacunarity,
                                    octaves,
                                    offset,
                                    noise_basis=nb
                                    )
'''                     

