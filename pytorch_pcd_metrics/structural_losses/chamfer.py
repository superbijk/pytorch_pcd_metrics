"""
Custom Chamfer Distance implementations

These are convenience functions that extend the original StructuralLosses package.
They are NOT part of the original author's implementation.
"""

import torch


def chamfer_distance_l2(x, y):
    """
    Squared L2 Chamfer Distance.

    This is an alias for distChamfer from StructuralLosses,
    which computes squared Euclidean distance.

    Args:
        x: Point cloud tensor [B, N, D]
        y: Point cloud tensor [B, M, D]

    Returns:
        min_dist_x: Minimum distances from x to y [B, N]
        min_dist_y: Minimum distances from y to x [B, M]

    Note:
        This is a convenience wrapper around the original distChamfer function.
    """
    from StructuralLosses import distChamfer
    return distChamfer(x, y)


def chamfer_distance_l1(x, y):
    """
    L1 Chamfer Distance.

    Computes Chamfer distance using L1 norm (Manhattan distance).
    This is our custom implementation, not from the original authors.

    Args:
        x: Point cloud tensor [B, N, D]
        y: Point cloud tensor [B, M, D]

    Returns:
        min_dist_x: Minimum L1 distances from x to y [B, N]
        min_dist_y: Minimum L1 distances from y to x [B, M]

    Example:
        >>> import torch
        >>> x = torch.rand(2, 100, 3)  # 2 batches, 100 points, 3D
        >>> y = torch.rand(2, 50, 3)   # 2 batches, 50 points, 3D
        >>> min_x, min_y = chamfer_distance_l1(x, y)
        >>> min_x.shape  # torch.Size([2, 100])
        >>> min_y.shape  # torch.Size([2, 50])
    """
    # Use torch.cdist with p=1 for L1 norm
    # cdist expects [B, N, D] and [B, M, D]
    # Returns [B, N, M] distance matrix
    dist = torch.cdist(x, y, p=1)

    min_dist_x, _ = torch.min(dist, dim=2)  # [B, N]
    min_dist_y, _ = torch.min(dist, dim=1)  # [B, M]

    return min_dist_x, min_dist_y


def permutation_invariance_metrics(x, y):
    """
    Compute metrics that should be invariant to permutation of points.

    This is our custom implementation, not from the original authors.
    Useful for sanity checking that point cloud metrics are working correctly.

    Args:
        x: Point cloud tensor [B, N, D]
        y: Point cloud tensor [B, N, D] (should have same N as x)

    Returns:
        dict with keys:
            - diff_mean: Difference in center of mass (mean)
            - diff_var: Difference in variance (spread)

    Example:
        >>> import torch
        >>> x = torch.rand(2, 1000, 3)
        >>> y = torch.rand(2, 1000, 3)
        >>> metrics = permutation_invariance_metrics(x, y)
        >>> print(metrics['diff_mean'], metrics['diff_var'])
    """
    # 1. Center of Mass (Mean)
    mean_x = x.mean(dim=1)  # [B, D]
    mean_y = y.mean(dim=1)  # [B, D]
    diff_mean = (mean_x - mean_y).norm(dim=1).mean()

    # 2. Variance / Spread
    var_x = x.var(dim=1, unbiased=False).sum(dim=1)  # [B]
    var_y = y.var(dim=1, unbiased=False).sum(dim=1)  # [B]
    diff_var = (var_x - var_y).abs().mean()

    return {
        "diff_mean": diff_mean.item() if diff_mean.numel() == 1 else diff_mean,
        "diff_var": diff_var.item() if diff_var.numel() == 1 else diff_var,
    }
