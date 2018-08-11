# Project Description:
The idea is a sharable staging area for wrangling data before transfer to an open data portal (e.g., https://data.world).  The repo stores raw data and wrangling scripts.  Citizen Lab members can push raw data into the repo and authorized members can write scripts to prepare data for transfer to an open data portal.  

## Maintainers (people with write access):
* James Wilfong

## Tools
Use your favorite data processing tool of choice.
* Jupyter Notebook
* Python
* ...
## Conventions
### Table Names
 * A noun is preferred to a verb, Plurals are preferred to singular
 * Provide a table abbreviation: A 3 letter abbreviation is preferred to a 4 letter abbreviation, a 4 letter abreviation is preferred to a longer abbrevation.
### Column Names
 * column names prefixed with a table abbreviation preferred to to column names with no prefix.
 * column names with underscores are preferred to column names with hyphens, column names with hyphens are preferred to column names with spaces, column names with spaces are just not right.
 * column names in lower case are preferred to everything else
### Identity Names
 * Alpha-numeric identity column names should end with the suffix "_id"
   * Numeric identity column names should end with the suffix "_no"
### Identity Values
* a universally unique identifyer (UUID) value is preferred to a locally unique identity value, a locally unique identity is preferred to no identity, things with no identity are not things at all. 

## Wrangling
* Tables
  * Name
 
  
* Table Columns
  * Column names 
   
   
   
  * Identity columns:
   
  
     
 
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
