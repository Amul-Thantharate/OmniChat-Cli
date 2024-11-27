from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

try:
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        requirements = [line.strip() for line in fh if line.strip() and not line.startswith('#')]
except FileNotFoundError:
    requirements = []

setup(
    name='omenicli',
    version='0.2.3',
    author='Amul Thantharate',
    author_email='amulthantharate@gmail.com',
    license='MIT',
    description='A powerful command-line interface for interacting with AI models and generating images. Features multiple AI providers, streaming responses, and a colorful interface.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Amul-Thantharate/OmniChat-Cli.git',
    packages=['app'],
    install_requires=requirements,
    python_requires='>=3.10',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    entry_points={
        'console_scripts': [
            'omenicli=app.main:app',
        ],
    }
)