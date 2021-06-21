from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'card_deck',
    packages = ['card_deck'],
    version = '1.0.1',
    license='MIT',
    description = 'An object model of a pack of cards',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Edmund Goodman',
    url = 'https://github.com/EdmundGoodman/card_deck',
    download_url = 'https://github.com/EdmundGoodman/card_deck/archive/refs/tags/v1.0.1.tar.gz',        # I explain this later on
    keywords = ['game', 'card', 'model'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
