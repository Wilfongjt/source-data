# source-data
A repository of CSV files

# Best Practice
* Name staged files the same as the data.world destination dataset. world-data/Seed.csv goes to data.world/../Seed dataset. Cuts down on the confusion of what goes where.

# Prerequisites
* install jupyter notebook

# Handling New Data
Goal: Keep data fresh
Strategy: total replacement of a data.world dataset

# Process
* Assemble New Data
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


| Originator              | -> | Developer                  | Maintainer                  |
| :---------------------- | :- | :------------------------- | --------------------------- |
| Download refresh-data branch |    |                       |    |                              |
| Add New Dataset         |    |                            |    |                              | 
| Upload Data to Repo     |    |                            |    |                              |
| Notify Developer        | -> | Download Data from Repo    |    |                              |
|                         |    | Setup Dev Data Environment |    |                              |
|                         |    | Write/Update Script        |    |                              |
|                         |    | Test Script in Dev         |    |                              |
|                         |    | Test Data Load in Dev      |    |                              |
|                         |    | Test Application           |    |                              |
|                         |    | Upload Script              |    |                              |
|                         |    | Notify Maintainer ->       |    | Download refresh-data Branch | 
|                         |    |                            |    | Setup Prod Data Environment  | 
|                         |    |                            |    | Deploy to Production         |
|                         |    |                            |    | Deployment Check             |
| Deployment Check        |    |                            | <- | Notify Originator            |
| Approve Deployment      |    |                            |    |                              |
| Notify Maintainer       | -> |                            |    | Update Master Branch         |



