import bpy
from math import radians

#create cube
bpy.ops.mesh.primitive_cube_add()
so = bpy.context.active_object

# rotate object
so.rotation_euler[0] += radians(45)


# create modifier
mod_subsurf = so.modifiers.new("My Modifier", 'SUBSURF')

# change modifier value
mod_subsurf.levels = 3

#bpy.ops.object.shade_smooth()

mesh = so.data

for face in mesh.polygons:
    face.use_smooth = True

# create displacement modifier
mod_displace = so.modifiers.new("My Displacement", 'DISPLACE')

# create the texture
#https://docs.blender.org/api/current/bpy.types.Texture.html
new_tex = bpy.data.textures.new("My Texture", 'DISTORTED_NOISE')

# change the texture settings
new_tex.noise_scale = 2.0

# assign the texture to displacement modifier
mod_displace.texture = new_tex

# create the material
new_mat = bpy.data.materials.new(name = "My Material")
so.data.materials.append(new_mat)

new_mat.use_nodes = True
nodes = new_mat.node_tree.nodes

