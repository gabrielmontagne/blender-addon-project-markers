import bpy

{
    'name': 'Project markers to other scenes',
    'author': 'gabriel montagné, gabriel@tibas.london',
    'version': (0, 0, 1),
    'blender': (2, 80, 0),
    'description': 'Replace makers in other scenes with the markers in this scene',
    'tracker_url': 'https://bitbucket.org/gabriel.montagne/blender-addon-project-markers/issues?status=new&status=open',
    'category': 'Object'
}

class PROJECT_MAKER_OT_tibasenno(bpy.types.Operator):
    """Replace all makers in other scenes with the markers in this scene"""
    bl_idname = "marker.project_to_scenes"
    bl_label = "Project markers to other scenes"

    def execute(self, context):
        print('Project markers to other scene')
        scene = context.scene
        markers = scene.timeline_markers

        for m in markers:
            print('m', m)

        for s in bpy.data.scenes:
            if s is scene:
                continue

            for xm in s.timeline_markers:
                s.timeline_markers.remove(xm)

            for m in markers:
                s.timeline_markers.new(m.name, frame=m.frame)

        return {'FINISHED'}

def register():
    bpy.utils.register_class(PROJECT_MAKER_OT_tibasenno)

def unregister():
    bpy.utils.unregister_class(PROJECT_MAKER_OT_tibasenno)

if __name__ == "__main__":
    register()
    bpy.ops.marker.project_to_scenes()
