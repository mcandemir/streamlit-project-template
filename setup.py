import pathlib
import setuptools

setuptools.setup(
    name="streamlit-project-template",
    version="0.1.0",
    description="A solid project structure from basit to advanced streamlit applications.",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Mehmet Can Demir",
    author_email="mhmtcndmr01@gmail.com",
    licance="MIT",
    project_urls={
        "Documentation": \
        "https://github.com/mcandemir/streamlit-project-template/blob/master/README.md",
        "Repository": "https://github.com/mcandemir/streamlit-project-template"
    },
    classifiers={
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12"
    },
    python_requires=">=3.6",
    # install_requires=[
    #     "streamlit"
    # ],
    # extras_require={
    #     "extras": [
    #         "streamlit-extras"
    #     ]
    # },
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "streamlit-project-template = streamlit_project_template:main",
            ]
        }
)