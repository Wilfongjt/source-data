# Project Description:
The idea is a sharable staging area for wrangling data before transfer to an open data portal (e.g., https://data.world).  The repo stores raw data and wrangling scripts.  Citizen Lab members can push raw data into the repo and authorized members can write scripts to prepare data for transfer to an open data portal.  

## Maintainers (people with write access):
* James Wilfong

## Actors
* Originator: an originator is usually a third party that has curated the data.  
## Open Data Portal
* https://data.world

## Scripting Tools
Use your favorite data processing tool.
* Jupyter Notebook
* Python
* ...
## Conventions
### Open Data Portals
* Using third party Open Data Portals via an API is preferred to coping a dataset to the Citizen Labs' open data portal
* Documentation on how to interface with a specific open data portal should be incuded in a applications repo
*
### API
* 
### Table Names
 * A noun is preferred to a verb, plurals are preferred to singular
 * Underscores are the preferred separator.  Spaces and hyphens are not recommended.
 * Lowercase is preferred to everything else
### Column Names
 * Underscores are the preferred separator.  Spaces and hyphens are not recommended.
 * Column names prefixed with a table abbreviation are preferred to column names with no prefix.
 * Lowercase is preferred to everything else
### Identity Names
 * Alpha-numeric identity values should have column names with the suffix "_id"
 * Numeric identity column names should have column names with the suffix "_no"
### Identity Values
* A universally unique identifyer (UUID) value is preferred to a locally unique identity value, a locally unique identity is preferred to no identity, things with no identity are not things at all. 

## Wrangling
Preparing data for uploading to the open data portal.
## Naming
* Don't change the name of the original source file. You may not be the originator of the file so keep the file as recognizeable to the originator as possible for ease of communications.
 
## Missing and Malformed Data

## Duplicate Data

## Outliers


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
