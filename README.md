Note: `setup.py` was modified to accommodate CUDA builds for code that was originally written against PyTorch 1.x. The build scripts in this repository adapt earlier torch 1.x CUDA build flags so the extension can be built with newer PyTorch/CUDA toolchains.

## Collection of Point cloud evaluation metrics
- All rights reserved to the original owners.
- Tested with Python 3.9.24, PyTorch 2.8.0+cu128, CUDA 12.8 (nvcc: /usr/local/cuda-12.8/bin/nvcc) on Ubuntu 24.04 (WSL)
- Tested with Python 3.9.13, PyTorch 1.12.1, CUDA 11.6 on Windows 11 and Ubuntu 22.04 (WSL)

### Included
- l-gan MMD COV 1-NN (CD/EMD) and JSD
- Original Author: https://github.com/stevenygd/PointFlow/tree/master/metrics/pytorch_structural_losses
- EMD (distance and assignment)
- Original Author: https://github.com/Colin97/MSN-Point-Cloud-Completion

### Compile
- Navigate inside directory and run `pip install .` to compile.

### Example
- See `test evaluation metrics.ipynb` for examples and installation.
