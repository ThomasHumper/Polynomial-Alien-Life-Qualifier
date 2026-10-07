pytest>=8.0

[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "polynomial-alien-life-qualifier"
version = "0.1.0"
description = "A polynomial constraint framework for qualifying hypothetical alien life."
readme = "README.md"
requires-python = ">=3.9"
license = { text = "Apache-2.0" }
authors = [
    { name = "YOUR NAME" }
]
dependencies = []

[project.optional-dependencies]
dev = [
    "pytest>=8.0"
]

[tool.pytest.ini_options]
pythonpath = [
    "src"
]
testpaths = [
    "tests"
]
