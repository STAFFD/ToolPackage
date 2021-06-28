from pywavefront import Wavefront
import numpy as np

def loadObjModel():    
    obj_file = Wavefront('dolphin/dolphin.obj', collect_faces=True)
    obj_vertices = np.array(obj_file.vertices, dtype='f')
    faces_list = []
    for mesh in obj_file.mesh_list:
        for face in mesh.faces:
            faces_list.append(face)
    obj_ind = np.array(faces_list,  dtype=np.int32)
    return obj_vertices, obj_ind