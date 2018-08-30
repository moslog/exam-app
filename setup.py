import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="examapp",
    version="0.0.5",
    author="Muhammad Muizzsuddin",
    author_email="m.muizzsuddin@windowslive.com",
    description="Generator for exam at Logic Pondok Programmer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moslog/exam-app",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),package_data={
        '': ['*']
   },
    include_package_data=True
)