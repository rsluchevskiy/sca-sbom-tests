from setuptools import find_packages, setup

setup(
    name="setup-py-best-practices",
    version="0.0.1",
    author="ORT Contributors",
    author_email="opensource@steenbe.nl",
    description=(
        "An python project that follows provenance metadata best practices."
    ),
    license="Apache-2.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/tsteenbe/sca-sbom-tests",
    project_urls={
        "Documentation": "https://github.com/tsteenbe/sca-sbom-testss",
        "Source": "https://github.com/tsteenbe/sca-sbom-tests",
        "Tracker": "https://github.com/tsteenbe/sca-sbom-tests/issues"
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    python_requires=">=3.9",
    install_requires=[
        "numpy",
        "pandas",
    ],
    extras_require={
        "dev": [
            "black",
            "deprecation",
            "pytest",
            "pytest-cov"
        ],
    },
)
