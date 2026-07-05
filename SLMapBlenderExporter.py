from io import BytesIO
import struct

def packFloat(what):
    return struct.pack(">f", what)

def packUInt(what):
    return struct.pack(">I", what)

class SLMapBlenderExporter:
    def __init__(self, objects):
        self.objects = objects

    def exportData(self, stream):
        print("Exporting blender data to .slmap")
        print(f"Count objects to export: {len(self.objects)}")
        stream.write(
            packUInt(len(self.objects))
        )
        
        for obj in self.objects:
            posX, posY, posZ = obj.location
            rotationW, rotationX, rotationY, rotationZ = obj.rotation_quaternion
            scaleX, scaleY, scaleZ = obj.scale
            name = obj.name
            
            print(f"Obj: {name}, Location: {posX}, {posY}, {posZ}; Scale: {scaleX}, {scaleY}, {scaleZ};")
            
            encodedName = name.encode("utf-8")
            stream.write(
                packUInt(len(encodedName))
            )
            
            stream.write(
                encodedName
            )
            
            stream.write(
                packFloat(posX)
            )
            
            stream.write(
                packFloat(posY)
            )
            
            stream.write(
                packFloat(posZ)
            )
            
        
        #materials = data.materials
        #material = materials[0]
        #materialName = material.name
        #colorR, colorG, colorB, _ = material.diffuse_color
        
        #vertices = data.vertices
        #vertex = vertices[0]
        #vertexCoord = vertex.co
        #vertexNormal = vertex.normal
        
        #polygons = data.polygons
        #polygon = polygons[0]
        #polygonVertices = polygon.vertices
        #polygonMaterialIndex = polygon.material_index
        
        #boundBox = ob.bound_box
        #x, y, z = boundBox
