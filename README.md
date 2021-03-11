# Python for Geographic Information System

Welcome to python for GIS training. In this course you will earn how to use python, and its libraries to implement your own GIS features.

During the corse, new materials will appear daily in this repository.

## Scope

The course covers:
* Shapely
* Geopandas
* Map projections
* Geocoding
* Spatial queries
    * Point in Polygon
    * Spatial join
    * Overlay analysis
    * Aggregation
* Data classification
* Retriving Open Street Map data
* Network analysis
* Visualization

**We will NOT cover using ArcGIS (arcpy) + QGIS with Python.** GIS universe is very diverse, and
these subjects would require separate courses. For the interested ones, there are some meterials available.

You will learn how to use libraries like `shapely`, `geopandas`, `mapclassify`, `bokeh`, `osmnx`  and `networkx`. By exercising, you will also strenthen your understandig of `pandas` and `matplotlib`.

To learn more about GIS stack in python, go [here](https://gistbok.ucgis.org/bok-topics/python-gis#Python).

## Before the course

To prepare for the course, make sure all dependencies are installed. You will need `python 3.8.5`, `git` and an IDE. You will also need to install required python packages, and jupyter notebook.
### System requirements
To participate in the course, you will need:
* `python 3.8.5` or newer

    To check your python version, run in the terminal:
    `python --version`
    If you need to install, or upgrade python, follow [these instructions](https://realpython.com/installing-python/)

### Required packages

Now, let's install the required packages. We encourage you to use [virtual environment](https://docs.python.org/3/tutorial/venv.html).

In your terminal run:
* `python3 -m venv venv` to create virtual env
* `. venv/bin/activate` to activate it on Linux or MacOS, or `venv\Scripts\activate.bat` on Windows
* `pip install -r requirements.txt` to install required packages
* `pip freeze` to see what you are using

*Geopandas on Windows*
If you are a Windows user, the package manager may fail installing geopandas. Geopandas require C++ dependencies, and if those are not setup correctly, the installation will fail.

If you encounter issues when installing geopandas, follow [this tutorial](https://geoffboeing.com/2014/09/using-geopandas-windows/).

### Setting up jupyter notebook

Now, let's setup jupyter notebook. This will be very handy when working with map visualizations.
Our recommendation is to install jupyter globally, and its kernel locally (in the venv). It allows you
to have as many kernels (python versions) as projects, but only one jupyter notebook.

To setup jupyter
* `deactivate` to quit the venv
* `pip install notebook` to install jupyter notebook globally
* `. venv/bin/activate` or `venv\Scripts\activate.bat` to activate venv again
* `pip install ipykernel` to install kernel in venv
* `python -m ipykernel install --user --name=gis-training` to attach kernel to your project
* `jupyter notebook` to start a notebook

A good tutorial on configuring jupyter in virtual environment is available [here](https://janakiev.com/blog/jupyter-virtual-envs/)

If you are using VS Code, we highly recommend [this jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter). It will allow you to execute notebooks directly in IDE.

To familiarize yourself with the extension, follow [this tutorial](https://code.visualstudio.com/docs/python/jupyter-support#_setting-up-your-environment).
