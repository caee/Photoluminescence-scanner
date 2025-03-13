import ctypes
import os

_DIRNAME = os.getenv('FLISDK_DIR')

if os.name == 'nt':
    lib = ctypes.cdll.LoadLibrary(_DIRNAME + "\\lib\\release\\FliSdk.dll")
elif os.name == 'posix':
    if "aarch64" in str(os.uname()):
        lib = ctypes.cdll.LoadLibrary(_DIRNAME + "/lib/libFliSdk.so")
    else:
        lib = ctypes.cdll.LoadLibrary(_DIRNAME + "/lib/release/libFliSdk.so")

CWRAPPER = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)