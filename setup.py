"""
PyTorch Point Cloud Metrics - Setup
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pytorch-pcd-metrics",
    version="0.1.0",
    author="Chawalit Chanintonsongkhla",
    description="Collection of Point Cloud Evaluation Metrics for PyTorch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pytorch-pcd-metrics",
    packages=find_packages(include=["pytorch_pcd_metrics*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.9",
    install_requires=[],
    keywords="point-cloud metrics evaluation 3d pytorch chamfer-distance emd",
)
