'''OpenGL extension ANGLE.instanced_arrays

This module customises the behaviour of the 
OpenGL.raw.GLES2.ANGLE.instanced_arrays to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ANGLE/instanced_arrays.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.ANGLE.instanced_arrays import *
from OpenGL.raw.GLES2.ANGLE.instanced_arrays import _EXTENSION_NAME

def glInitInstancedArraysANGLE():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glDrawElementsInstancedANGLE.indices size not checked against 'count,type'
glDrawElementsInstancedANGLE=wrapper.wrapper(glDrawElementsInstancedANGLE).setInputArraySize(
    'indices', None
)
### END AUTOGENERATED SECTION