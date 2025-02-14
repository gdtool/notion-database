import setuptools

from src.notion_database import NOTION_VERSION

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="notion-database",
    version=NOTION_VERSION.replace("-", "") + ".2",
    author="minwook-shin",
    author_email="isme@gmail.com",
    description=" Notion API Database Python Implementation+",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gdtool/notion-database",
    project_urls={
        "Bug Tracker": "https://github.com/gdtool/notion-database/issues",
    },
    install_requires=[
        "requests==2.27.1",
        "typing-extensions==4.1.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
