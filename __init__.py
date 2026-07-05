import bpy
from bpy.types import Operator, OperatorFileListElement, AddonPreferences
from bpy.props import StringProperty, BoolProperty, CollectionProperty, FloatProperty, EnumProperty
from bpy_extras.io_utils import ImportHelper, ExportHelper

from .SLMapBlenderExporter import SLMapBlenderExporter

from os.path import isdir
from time import time

class exportSlmap(Operator, ExportHelper):
    bl_idname = "export_scene.mgengine"
    bl_label = "Export slmap"
    bl_description = "Export an slmap model"
    bl_options = {'PRESET', 'UNDO'}

    filter_glob: StringProperty(default="*.slmap", options={'HIDDEN'})
    filename_ext: StringProperty(default=".slmap", options={'HIDDEN'})

    def invoke(self, context, event):
        return ExportHelper.invoke(self, context, event)
    
    def execute(self, context):
        print(f"Exporting blender data to {self.filepath}")

        exporter = SLMapBlenderExporter(
            bpy.context.selected_objects
        )

        with open(self.filepath, "wb") as file:
            exporter.exportData(
                file
            )

        return {"FINISHED"}


def menuExportSlmap(self, context):
    self.layout.operator(exportSlmap.bl_idname, text="MGEngine map (.slmap)")
    

classes = [
    exportSlmap
]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.TOPBAR_MT_file_export.append(menuExportSlmap)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    bpy.types.TOPBAR_MT_file_export.remove(menuExportSlmap)

if __name__ == "__main__":
    register()
