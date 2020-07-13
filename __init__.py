import bpy

bl_info = {
    'name': 'Project markers to other scenes',
    'author': 'gabriel montagné, gabriel@tibas.london',
    'version': (0, 0, 1),
    'blender': (2, 80, 0),
    'description': 'Replace makers in other scenes with the markers in this scene',
    'tracker_url': 'https://github.com/gabrielmontagne/blender-addon-project-markers/issues?status=new&status=open',
    'category': 'Object'
}

class PROJECT_MAKER_OT_tibasenno(bpy.types.Operator):
    """Replace all makers in other scenes with the markers in this scene"""
    bl_idname = "marker.project_markers_to_scenes"
    bl_label = "Project markers to other scenes"

    def execute(self, context):
        print('Project markers to other scenes')
        scene = context.scene
        markers = scene.timeline_markers

        for s in bpy.data.scenes:
            if s is scene:
                continue

            for xm in s.timeline_markers:
                s.timeline_markers.remove(xm)

            for m in markers:
                s.timeline_markers.new(m.name, frame=m.frame)

        return {'FINISHED'}

class PROJECT_START_END_OT_tibasenno(bpy.types.Operator):
    """Replace all makers in other scenes with the markers in this scene"""
    bl_idname = "marker.project_start_end_to_scenes"
    bl_label = "Project start / current / end frames to other scenes"

    def execute(self, context):
        print('Project start-end to other scenes')
        scene = context.scene
        markers = scene.timeline_markers

        for s in bpy.data.scenes:
            if s is scene:
                continue

            s.frame_start = scene.frame_start
            s.frame_current = scene.frame_current
            s.frame_end = scene.frame_end
            s.frame_preview_end = scene.frame_preview_end
            s.frame_preview_start = scene.frame_preview_start

        return {'FINISHED'}

def register():
    bpy.utils.register_class(PROJECT_MAKER_OT_tibasenno)
    bpy.utils.register_class(PROJECT_START_END_OT_tibasenno)

def unregister():
    bpy.utils.unregister_class(PROJECT_START_END_OT_tibasenno)
    bpy.utils.unregister_class(PROJECT_MAKER_OT_tibasenno)

if __name__ == "__main__":
    register()
