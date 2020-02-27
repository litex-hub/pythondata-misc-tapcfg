import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

from litex.data.misc.tapcfg import version_str

setuptools.setup(
    name="litex-data-misc-tapcfg",
    version=version_str,
    author="LiteX Authors",
    author_email="litex@googlegroups.com",
    description="Python module containing data files for using the Ethernet TAP Config misc with LiteX.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/litex-hub/litex-data-misc-tapcfg",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    zip_safe=False,
    packages=setuptools.find_packages(),
    package_data={'litex.data.misc.tapcfg': ['litex/data/misc/tapcfg/data/**']},
    include_package_data=True,
)
