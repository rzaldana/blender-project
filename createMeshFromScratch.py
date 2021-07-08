import bpy

name = "New Object"

#create verts
verts = []
#              x ,  y , z
verts.append([0.0, 2.0, 0.0]) #index 0
verts.append([1.0, 0.0, 0.0])
verts.append([0.0, 0.0, 1.0])
verts.append([-1.0, 0.0, 0.0])

#create edges (optional)
edges = []
#edges.append([0,1])

#create faces
faces = []
faces.append([0, 1, 2])
faces.append([2, 0, 3])

#create mesh
mesh = bpy.data.meshes.new(name)

#create object
obj = bpy.data.objects.new(name, mesh)

#add skin modifier to object
#mod_skin = obj.modifiers.new('Skin', 'SKIN')

#get collection of Objects that are displayed in the scene
col = bpy.data.collections.get("Collection")
print("Collection: ")
print(col)
col.objects.link(obj)

#make new object the active object
bpy.context.view_layer.objects.active = obj

mesh.from_pydata(verts, edges, faces)