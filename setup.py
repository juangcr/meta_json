from os import path
from setuptools import setup, find_packages


def get_long_description():
  here = path.abspath(path.dirname(__file__))
  with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="meta-json",
    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    # https://packaging.python.org/guides/single-sourcing-package-version/
    version="0.0.1.dev1",
    description="Extract metadata from a deserialized JSON.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/juangcr/metadata_json",
    author="Juan Cortés",
    author_email="juang.cortes@outlook.com",
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    keywords='metadata json',
    include_package_data=True,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    # install_requires=[""],
    extras_require={
        "test": [
            "pytest",
            "black",
            "flake8",
            "mypy"
            ]
    },
    project_urls={
        "Source": "https://github.com/juangcr/meta_json/",
    },
)

