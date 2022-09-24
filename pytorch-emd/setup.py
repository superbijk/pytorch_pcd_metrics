from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='emd',
    packages=['emd_wrapper'],
    package_dir={'emd_wrapper': './src/emd_wrapper'},
    ext_modules=[
        CUDAExtension('emd_cuda', [
            'src/emd/emd.cpp',
            'src/emd/emd_cuda.cu',
        ]),
    ],
    cmdclass={
        'build_ext': BuildExtension
    })