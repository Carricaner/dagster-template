from setuptools import find_packages, setup

setup(
    name="demo_code_location",
    packages=find_packages(exclude=["demo_code_location_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
