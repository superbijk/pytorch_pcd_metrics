# Collection of Point Cloud Evaluation Metrics

- All rights reserved to the original owners.
- Tested with Python 3.9.25, PyTorch 2.8.0+cu128, CUDA 12.8 on Ubuntu 24.04 (WSL)
- Original packages were modified (`setup.py`, CUDA files: `*.cu`, `*.cpp`) to accommodate builds for code that was originally written against mostly PyTorch 1.x. The build scripts in this repository adapt earlier torch 1.x CUDA build flags so the extension can be built with newer PyTorch/CUDA toolchains.

## Installation

```bash
cd sources/modified/MSN__emd && pip install .              # Install individual package
pip install .                                              # Install wrapper
bash run.sh                                                # Interactive menu
```

## Included Metrics

| Source | Import | Metrics | Usage |
|--------|--------|---------|-------|
| [PointFlow](https://github.com/stevenygd/PointFlow/tree/master/metrics/pytorch_structural_losses) | `from StructuralLosses import *` | COV(CD/EMD), MMD(CD/EMD), 1-NN(CD/EMD), JSD | `compute_all_metrics(a, b, batch_size)` → dict<br>`jsd_between_point_cloud_sets(a, b)` → float |
| [MSN](https://github.com/Colin97/MSN-Point-Cloud-Completion) | `from emd_wrapper import emdModule` | EMD (auction) | `emdModule()(a, b, eps, iters)` → (dist, assignment) |
| [PyTorchEMD](https://github.com/daerduoCarey/PyTorchEMD) | `from emd import earth_mover_distance` | EMD (approx) | `earth_mover_distance(a, b, transpose)` → cost |
| [ChamferDistance](https://github.com/ThibaultGROUEIX/ChamferDistancePytorch) | `from dist_chamfer_3D import chamfer_3DDist` | Chamfer Distance | `chamfer_3DDist()(a, b)` → (dist1, dist2, idx1, idx2) |

## Usage

- **Examples**: See `notebooks/01_test_packages.ipynb` for complete usage examples