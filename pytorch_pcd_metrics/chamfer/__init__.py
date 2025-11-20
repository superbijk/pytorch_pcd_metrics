"""
ChamferDistance Wrapper

Source: https://github.com/ThibaultGROUEIX/ChamferDistancePytorch

Fast CUDA implementation of Chamfer Distance for 3D point clouds.

Functions:
    - chamfer_3DDist: Chamfer Distance module (nn.Module)
    - chamfer_3DFunction: Chamfer Distance autograd function
"""

try:
    from dist_chamfer_3D import chamfer_3DDist, chamfer_3DFunction

    __all__ = ['chamfer_3DDist', 'chamfer_3DFunction']

except ImportError as e:
    raise ImportError(
        "ChamferDistance (chamfer_3D) not installed. Please install with:\n"
        "  cd sources/modified/ThibaultGROUEIX__ChamferDistancePytorch/chamfer3D && pip install .\n"
        "Or run: bash run.sh"
    ) from e
