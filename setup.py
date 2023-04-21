import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="springpy",
    version="0.1.0",
    author="kiwirafe",
    author_email="kiwirafe@gmail.com",
    description="Distance Matrix Visualizer in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kiwirafe/springpy",
    project_urls={"Github": "https://github.com/kiwirafe/springpy"},
    packages=["springpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "matplotlib",
    ],
    package_data = {
        # If any package contains *.txt files, include them:
        "springpy": ["*.txt", "*.md", "springpy/*",],
    },
    python_requires=">=3.4",
)
