import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

from pythondata_misc_tapcfg import version_str

setuptools.setup(
    name="pythondata-misc-tapcfg",
    version=version_str,
    author="LiteX Authors",
    author_email="litex@googlegroups.com",
    description="""\
Python module containing data files for Ethernet TAP Config misc.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/litex-hub/pythondata-misc-tapcfg",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    zip_safe=False,
    packages=setuptools.find_packages(),
    package_data={
    	'misc_tapcfg': ['misc_tapcfg/data/**'],
    },
    include_package_data=True,
    project_urls={
        "Bug Tracker": "https://github.com/litex-hub/pythondata-misc-tapcfg/issues",
        "Source Code": "https://github.com/litex-hub/pythondata-misc-tapcfg",
    },
)
