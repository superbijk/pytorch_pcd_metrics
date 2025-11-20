"""Setup extension

Notes:
    If extra_compile_args is provided, you need to provide different instances for different extensions.
    Refer to https://github.com/pytorch/pytorch/issues/20169

"""

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension


setup(
    name='emd_ext',
    version='0.0.0',
    py_modules=['emd'],
    ext_modules=[
        CUDAExtension(
            name='emd_cuda',
            sources=[
                'cuda/emd.cpp',
                'cuda/emd_kernel.cu',
            ],
            extra_compile_args={'cxx': ['-g'], 'nvcc': ['-O2']}
        ),
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
