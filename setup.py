from setuptools import setup, find_packages

setup(
    name="bitvis",
    version="0.1.1",
    author="che-41",
    author_email="",
    description="A PyQt6-based bit converter application",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/che-41/bitvis",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "bitvis": ["resources/bitvis.ico"],  # Relativer Pfad im Paket
    },
    install_requires=[
        "PyQt6>=6.0.0",
    ],
    entry_points={
        "console_scripts": [
            "bitvis=bitvis.bitvis:main",  # Anpassung an deinen Einstiegspunkt
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
