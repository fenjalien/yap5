import setuptools
with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='yap5',
    version='0.6.1',
    author='fenjalien',
    description="Gives simplified drawing bindings to the pyglet library. The main window class is still accessible.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent"
    ]
)
