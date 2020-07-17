from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name="augaudio",
    version="1.0.0",
    author="Bastian Schwickert",
    author_email="Bastian.Schwickert@gmail.com",
    description="A simple audio data augmentation package",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://basti564.github.io",
    project_urls={
        "Bug Tracker": "https://github.com/Basti564/augaudio/issues",
        "Source Code": "https://github.com/Basti564/augaudio",
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
          'numpy >= 1.16.2',
          'librosa >= 0.7.2',
          ],
    license="Apache",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
		"Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
		"Topic :: Scientific/Engineering",
    ],
)
