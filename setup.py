import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="transformersum",  # Replace with your own username
    version="0.0.1",
    author="",
    author_email="",
    description="TransformerSum as a package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "torch==1.13.1",
        "scikit-learn==1.2.*",
        "tensorboard",
        "spacy",
        "sphinx",
        "pyarrow",
        "pytorch_lightning==1.6.5",
        "transformers==4.*",
        "torch_optimizer==0.3.*",
        "wandb==0.14.*",
        "rouge-score==0.1.*",
        "packaging",
        "datasets==2.*",
        "gradio==3.*"
    ],
    dependency_links=[
        "https://download.pytorch.org/whl/cu117",
    ]
)
