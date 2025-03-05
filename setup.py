from setuptools import setup, find_packages

setup(
    name='DiffTSR',
    version='0.0.1',
    description='A tool for super-resolution tasks',
    packages=find_packages(),
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
    python_requires='>=3.8',  # 明确指定 Python 版本
)
