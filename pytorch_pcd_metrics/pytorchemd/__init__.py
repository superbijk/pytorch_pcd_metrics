"""daerduoCarey PyTorchEMD Wrapper

Provides Earth Mover's Distance (EMD) for point clouds using optimal transport.

Functions:
    - earth_mover_distance: Compute EMD between two point clouds
    - EarthMoverDistanceFunction: PyTorch autograd function for EMD
"""

try:
    from emd import earth_mover_distance, EarthMoverDistanceFunction

    __all__ = [
        'earth_mover_distance',
        'EarthMoverDistanceFunction',
    ]

except ImportError as e:
    raise ImportError(
        "PyTorchEMD (emd_ext) not installed. Please install with:\n"
        "  cd sources/modified/daerduoCarey__PyTorchEMD && pip install .\n"
        "Or run: bash run.sh"
    ) from e
