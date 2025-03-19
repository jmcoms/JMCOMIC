from setuptools import setup, find_packages

setup(
    name='product_intro_blog',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'sphinx',
        'sphinx-rtd-theme',
    ],
)