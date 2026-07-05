import struct

def packFloat(what):
    return struct.pack(">f", what)

def packUInt(what):
    return struct.pack(">I", what)

def writeVector2(stream, what):
    stream.write(
        packFloat(what[0])
    )
    
    stream.write(
        packFloat(what[1])
    )

def writeVector3(stream, what):
    stream.write(
        packFloat(what[0])
    )
    
    stream.write(
        packFloat(what[1])
    )
    
    stream.write(
        packFloat(what[2])
    )
    
class MGObject:

    def __init__(self, obj):
        self.obj = obj
        
    def exportData(self, stream):
        print(f"Exporting object to .mgobj ::: {self.obj.type}")
        if (self.obj.type != "MESH"):
            return
            
        mesh = self.obj.data
        vertices = mesh.vertices
        verticesCount = len(vertices)
        print(f"Vertex count: {verticesCount}")
        
        stream.write(
            packUInt(verticesCount)
        )
        
        print("Writing vertices")
        layerLight = mesh.uv_layers.get("lightmap").data
        for i in range(verticesCount):
            vertex = vertices[i]
            # position
            writeVector3(stream, vertex.co)
            
            # uv
            writeVector2(stream, layerLight[i].uv)
            
            # normals
            writeVector3(stream, vertex.normal)
            
        print("Writing triangle indices")
        
        mesh.calc_loop_triangles()
        print(f"Triangles count: {len(mesh.loop_triangles)}")
        
        for tri in mesh.loop_triangles:
            stream.write(
                packUInt(tri.vertices[0])
            )
            
            stream.write(
                packUInt(tri.vertices[1])
            )
            
            stream.write(
                packUInt(tri.vertices[2])
            )
