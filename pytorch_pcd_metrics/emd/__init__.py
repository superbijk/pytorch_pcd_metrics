"""
MSN Earth Mover's Distance (EMD) Wrapper

Source: https://github.com/Colin97/MSN-Point-Cloud-Completion

This module provides a wrapper around the emd_wrapper package.
Make sure to install the source package first:
    pip install sources/modified/MSN__emd
"""

try:
    from emd_wrapper import emdModule, test_emd
    __all__ = ['emdModule', 'test_emd']
except ImportError as e:
    raise ImportError(
        "emd_wrapper not installed. Please install with:\n"
        "  cd sources/modified/MSN__emd && pip install .\n"
        "Or run: bash run.sh"
    ) from e
