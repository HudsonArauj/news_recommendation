from setuptools import setup, find_packages
import os

def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read()

here = os.path.abspath(os.path.dirname(__file__))
long_description = read_file(os.path.join(here, "README.md"))

with open(os.path.join(here, "requirements.txt"), "r") as f:
    install_requires = f.read().splitlines()

setup(
    name="fastapi_template",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "fastapi_template_app=fastapi_template.main:run"
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
)
