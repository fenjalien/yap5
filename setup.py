import setuptools
with open('README.md', 'r') as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="UTF-8") as f:
    requires = f.read().split("\n")

setuptools.setup(
    name='yap5',
    version='0.6.2',
    author='fenjalien',
    description="Gives simplified drawing bindings to the pyglet library. The main window class is still accessible.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),

    install_requires=requires,

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent"
    ]
)
