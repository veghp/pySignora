import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = {}
with open("pysignora/version.py") as fp:
    exec(fp.read(), version)

setuptools.setup(
    name="pysignora",
    version=version["__version__"],
    author="Peter Vegh",
    description="Pathway gene-pair signature overrepresentation analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3+",
    url="https://github.com/veghp/pySignora",
    keywords="biology",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)
