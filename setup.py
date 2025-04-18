from setuptools import setup, find_packages

setup(
    name="tasktagger-cli",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tasktagger=tasktagger.cli:main',
        ],
    },
    author="delibero",
    description="Scan source code for TODO, FIXME, and HACK-style task tags.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
