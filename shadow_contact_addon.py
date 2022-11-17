import bpy



bl_info = {
    "name": "Contact shadow ",
    "blender": (3, 3, 1),
    "category": "Object",
}

#operator

class LIGHT_OT_CONTACT(bpy.types.Operator):
    bl_idname="object.contactshadow"
    bl_label="shadow contact"
    
    my_bool:bpy.props.BoolProperty(name="ToggleOption")
    @classmethod
    def poll(self,context):
        return context.object is not None
        
    
    def execute(self,context):
        
        for light in bpy.data.lights:
            
            light.use_contact_shadow=self.my_bool
                
        
        return {"FINISHED"}






#panel

class SHADOW_CONTACT_PANEL(bpy.types.Panel):
    bl_idname="LIGHT_PT_SHADOW"
    bl_label="contact shadow"
    bl_space_type="VIEW_3D"
    bl_region_type="UI"
    
    
    
    def draw(self,context):
        layout=self.layout
        
        turn_on_operator=layout.operator("object.contactshadow",text="contact shadow True")
        turn_on_operator.my_bool = True
        
        turn_of_operator=layout.operator("object.contactshadow",text="contact shadow False")
        turn_of_operator.my_bool = False
        
    

allClass=(
LIGHT_OT_CONTACT,
SHADOW_CONTACT_PANEL

)

def register():
    for cls in allClass:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in allClass:
        bpy.utils.unregister_class(cls)
        
       
