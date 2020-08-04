import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygments-promql",
    version="0.0.3",
    author="Pablo Seminario",
    author_email="pablo@seminar.io",
    description="A PromQL lexer for Pygments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pabluk/pygments-promql",
    keywords="pygments-lexer promql highlighting",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    install_requires=['Pygments>=2'],
    entry_points={
        'pygments.lexers': [
            'PromQLLexer = pygments_promql:PromQLLexer'
        ],
    },
)
