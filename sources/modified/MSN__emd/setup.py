from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='msn_emd',
    version='0.0.0',
    packages=['emd_wrapper'],
    package_dir={'emd_wrapper': './src/emd_wrapper'},
    ext_modules=[
        CUDAExtension('msn_emd_cuda', [
            'src/emd/emd.cpp',
            'src/emd/emd_cuda.cu',
        ]),
    ],
    cmdclass={
        'build_ext': BuildExtension
    })