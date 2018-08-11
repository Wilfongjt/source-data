Title: TBD

# SLACK CHANNEL TBD

# Project Description:
The idea is a sharable staging area for wrangling data before transfer to an open data portal (e.g., https://data.world).  The repo stores raw data and wrangling scripts.  Citizen Lab members can push raw data into the repo and authorized members can write scripts to prepare data for transfer to an open data portal.  

# Table of Contents
* TBD

# Change Management
* Initiate a change request by adding a repo "Issue"
* Process changes require discussion to validate the correctness of the change

## Maintainers (people with write access):
* James Wilfong
* TBD -  need at least two maintainers 

## Roles
* **Originator**: an originator is usually, but not always, a third party that curates a dataset. Has github privileges to create, clone, and push github branches
* **Developer**: a developer writes and runs scripts in development environment, keeps development API key(s). Has github privileges to create, clone, push, and make pull requests on a branch
* **Maintainer**: an admin that runs scripts in production environment, keeper of the Citizen Labs API keys(s), Has github privileges to  clone, resolve pull requests
## Open Data Portal
* https://data.world

## Scripting Tools
Use your favorite data processing tool.
* Jupyter Notebook
* Python
* ...
## Conventions and Expectations
### Open Data Portals
* Using third party Open Data Portals via an API is preferred to copying a dataset to the Citizen Labs' open data portal
* Documentation on how to interface with a specific open data portal should be incuded in a application's repo
* 
### API
* An API is preferred to a direct connection to a database. Direct connections are discouraged. 
### Versioning
* Be nice to other applications sharing a dataset by versioning 
* A new version is required when a column name changes
* A new version is required when adding a column to an existing version
* Versions should be few, no more than 3 copies of a dataset should appear in the data portal
* When a fourth version is required
### Table Names
 * A noun is preferred to a verb, plurals are preferred to singular
 * Underscores are the preferred separator.  Spaces and hyphens are not recommended.
 * Lowercase is preferred to everything else
### Column Names
 * Underscores are the preferred separator.  Spaces and hyphens are not recommended.
 * Column names prefixed with a table abbreviation are preferred to column names with no prefix.
 * Lowercase is preferred to everything else
### Identity Names
 * Alphanumeric identity values should have column names with the suffix "_id"
 * Numeric identity column names should have column names with the suffix "_no"
### Identity Values
* A universally unique identifier (UUID) value is preferred to a locally unique identity value, a locally unique identity is preferred to no identity, things with no identity are not things at all. 

## Wrangling
Preparing data for uploading to the open data portal.
Environment Variables (.env)
### Naming
* Don't change the name of the original source file. You may not be the originator of the file so keep the file as recognizable to the originator as possible for ease of communications.
* Use a script to copy original files to an 
* Script column name changes

### Missing and Malformed Data

### Duplicate Data

### Outliers

## GitHub Process

### Originator
* Create a branch to hold new or updated datasets
* Clone the branch on your local machine
* Add a new data set
 * put original data in the repo's raw-data/ folder
* Create a new or modify an existing data load script 
### Developer

## Process
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
* cd ~/github/source-data/notebook
* jupyter-notebook
* using jupyter, open Process.ipynb
* from jupyter, run all the cells


