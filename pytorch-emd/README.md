## Earth Mover's Distance of point clouds

- Original Author: https://github.com/Colin97/MSN-Point-Cloud-Completion
- Tested with Python 3.9.13, PyTorch 1.12.1, CUDA 11.6 on Windows 11 and WSL Ubuntu 22.04

### Compile
- Navigate inside directory and run `pip install .` to compile.

### Input

- **xyz1, xyz2**: float tensors with shape `[#batch, #points, 3]`. xyz1 is the predicted point cloud and xyz2 is the ground truth point cloud. Two point clouds should have same size and be normalized to [0, 1]. The number of points should be a multiple of 1024. The batch size should be no greater than 512. Since we only calculate gradients for xyz1, please do not swap xyz1 and xyz2.
- **eps**: a float tensor, the parameter balances the error rate and the speed of convergence.
- **iters**: a int tensor, the number of iterations.

### Output

- **dist**: a float tensor with shape `[#batch, #points]`. sqrt(dist) are the L2 distances between the pairs of points.
- **assignment**: a int tensor with shape `[#batch, #points]`. The index of the matched point in the ground truth point cloud.

### Example
See `emd_module.py/test_emd()` for examples.

```
import torch
import emd_wrapper
emd_module = emd_wrapper.emdModule()

a = torch.rand((64, 2048, 3)).cuda()
b = torch.rand((64, 2048, 3)).cuda()

%time emd_dist, assignment = emd_module(a, b, 0.002, 10000)
print(emd_dist.mean(dim=1))
```