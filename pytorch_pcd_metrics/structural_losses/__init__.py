"""
PointFlow Structural Losses Wrapper

Source: https://github.com/stevenygd/PointFlow/tree/master/metrics/pytorch_structural_losses

This module provides evaluation metrics for point clouds including:
    - L-GAN metrics: MMD, COV, 1-NN (using CD or EMD)
    - JSD: Jensen-Shannon Divergence
    - Chamfer Distance: L1 and L2 variants (our extensions)

Make sure to install the source package first:
    pip install sources/modified/PointFlow__pytorch_structural_losses
"""

try:
    # Import from original StructuralLosses package
    from StructuralLosses import (
        # Main API (original)
        compute_all_metrics,
        jsd_between_point_cloud_sets,

        # Chamfer Distance (original)
        distChamfer,

        # EMD approximation (original)
        emd_approx,
        EMD_CD,

        # Utility functions (original)
        entropy_of_occupancy_grid,
        jensen_shannon_divergence,
        unit_cube_grid_point_cloud,
    )

    # Import our custom extensions
    from .chamfer import (
        chamfer_distance_l1,
        chamfer_distance_l2,
        permutation_invariance_metrics,
    )

    __all__ = [
        # Original StructuralLosses
        'compute_all_metrics',
        'jsd_between_point_cloud_sets',
        'distChamfer',
        'emd_approx',
        'EMD_CD',
        'entropy_of_occupancy_grid',
        'jensen_shannon_divergence',
        'unit_cube_grid_point_cloud',
        # Our extensions
        'chamfer_distance_l1',
        'chamfer_distance_l2',
        'permutation_invariance_metrics',
    ]

except ImportError as e:
    raise ImportError(
        "StructuralLosses not installed. Please install with:\n"
        "  cd sources/modified/PointFlow__pytorch_structural_losses && pip install .\n"
        "Or run: bash run.sh"
    ) from e
