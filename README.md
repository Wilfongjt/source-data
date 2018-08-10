# Project Description:
The idea is a sharable staging area for wrangling data before transfer to an open data portal (e.g., https://data.world).  The repo stores raw data and wrangling scripts.  Citizen Lab members can push raw data into the repo and authorized members can write scripts to prepare data for transfer to an open data portal.  

# Maintainers (people with write access):
* James Wilfong

# Tools
Use your favorite data processing tool of choice.
* Jupyter Notebook
* Python

# Wrangling
* Table Naming
* Column Naming
* Missing and Malformed Data
* Duplicate Data
* Outliers


# Process
* 
* Get source-data Repository
* Process raw-data to clean-data
* Update source-data Repository
* Move clean-data to Data.World Dataset

# Assemble New Data
*  
# Get source-data Repository
* mkdir ~/github
* cd ~/github
* git clone -b refresh-data https://github.com/Wilfongjt/source-data.git

# Process raw-dataset
* put new or updated data-file in /github/source-data/raw-data/ folder
* open command window
* cd ~/github/source-data/notebook
* jupyter-notebook
* using jupyter, open Process.ipynb
* from jupyter, run all the cells
