"""
PyTorch Point Cloud Metrics

Collection of point cloud evaluation metrics for PyTorch.
All rights reserved to the original authors.

Submodules:
    - emd: MSN Earth Mover's Distance
    - pytorchemd: daerduoCarey PyTorchEMD (optimal transport EMD)
    - structural_losses: PointFlow evaluation metrics (MMD, COV, 1-NN, JSD)
    - chamfer: ThibaultGROUEIX ChamferDistance (fast CUDA)

Usage:
    # Direct imports
    from pytorch_pcd_metrics import compute_all_metrics, jsd_between_point_cloud_sets
    from pytorch_pcd_metrics.emd import emdModule as MSN_EMD
    from pytorch_pcd_metrics.pytorchemd import earth_mover_distance
    from pytorch_pcd_metrics.chamfer import chamfer_3DDist
"""

__version__ = "0.1.0"
__author__ = "Chawalit Chanintonsongkhla"

# Re-export commonly used functions from structural_losses
try:
    from .structural_losses import compute_all_metrics, jsd_between_point_cloud_sets
    _has_structural_losses = True
except ImportError:
    _has_structural_losses = False

__all__ = ["emd", "pytorchemd", "structural_losses", "chamfer"]

if _has_structural_losses:
    __all__.extend(["compute_all_metrics", "jsd_between_point_cloud_sets"])
