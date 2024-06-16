# BootImageExtractor Setup File
# -----------------------------
# 
# Install with: pip install .
#
# Usage: sudo boot_image_extractor.py

from setuptools import setup

setup(
    name='Boot-Image-Extractor',
    description='A tool to extract boot images from Android devices with root access.',
    author='Abhijeet',
    url='https://github.com/gitclone-url/Boot-image-Extractor',
    scripts=['scripts/boot_image_extractor.py'],
    install_requires=[
        'pyfiglet',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Android', 
    ],
)
