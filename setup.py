import setuptools
with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='octo-fenjalien',
    version='0.2',
    author='fenjalien',
    description="A 2D graphics library.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent"
    ]
)
