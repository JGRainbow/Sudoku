import setuptools

setuptools.setup(
    name="Sudoku", 
    version="0.0.1",
    author="Jacob Rainbow",
    author_email="jacob.rainbow@gmail.com",
    description="Sudoku Solver using Backtracking",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)