import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="card_deck",
    version="1.0.0",
    author="Edmund Goodman",
    description="An object model of a pack of cards",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EdmundGoodman/cards",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
