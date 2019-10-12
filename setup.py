import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='benefactor',
    version='0.1',
    scripts=[],
    author="Viktor Chukhantsev",
    author_email="email@viktor.dev",
    description="Useful Python snippets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/viktorchukhantsev/benefactor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
