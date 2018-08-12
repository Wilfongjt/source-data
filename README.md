Title: TBD

# SLACK CHANNEL TBD

# Project Description:
The idea is a sharable staging area for wrangling data before transfer to an open data portal (e.g., https://data.world).  The repo stores raw data and wrangling scripts.  Citizen Lab members can push raw data into the repo and authorized members can write scripts to prepare data for transfer to an open data portal.  

With some effort, we can create a repository of data and scripts to facilitate future data wrangling and help keep our open data manageable. 

# Table of Contents
TBD
## Maintainers (people with write access):
* TBD -  need at least two maintainers 

# Process
## Roles
| Originator              | Developer                | Maintainer                |
| :------------------     | :---------------------   | :-----------------------  |
| Curates dataset         | Writes scripts           | Puts data into production |
| Initiates data transfer | Tests data transfer      | Removes data from production |
| Maintains GIT raw-data  | Maintains GIT scripts    | Maintains Versions | 
|                         | Maintains GIT tmp-data   | Maintains the GIT master branch |
|                         | Maintains GIT clean-data | Keeps Production API Keys
|                         | Keeps Dev/Test API Keys |  |

## Process Overview
This is a best case scenario with no failures. Use as a guide to a successful completion of the process.   

| Originator          |    | Developer              |    | Maintainer               |
| :---------------------- | :- | :------------------------- | :- | :--------------------------- |
| Download refresh-data Branch |    |                       |    |                              |
| Add New Dataset         |    |                            |    |                              | 
| Upload refresh-data Branch |    |                         |    |                              |
| Notify Developer        | > | Download refresh-data Branch |    |                            |
|                         |    | Setup Dev Data Environment |    |                              |
|                         |    | Write/Update Script        |    |                              |
|                         |    | Test Script in Dev         |    |                              |
|                         |    | Test Data Load in Dev      |    |                              |
|                         |    | Test Application           |    |                              |
|                         |    | Upload refresh-data Branch |    |                              |
|                         |    | Notify Maintainer          | > | Download refresh-data Branch | 
|                         |    |                            |    | Setup Prod Data Environment  | 
|                         |    |                            |    | Deploy to Production         |
|                         |    |                            |    | Deployment Check             |
| Deployment Check        |    |                            | < | Notify Originator            |
| Approve Deployment      |    |                            |    |                              |
| Notify Maintainer       | > |                            |    | Update master Branch         |

## Open Data Portal
* https://data.world

## Conventions and Expectations
### Open Data Portals
* Using third party Open Data Portals via an API is preferred to copying a dataset to the Citizen Labs' open data portal
* Documentation on how to interface with a specific open data portal should be included in an application's repo
### API
* An API is preferred to a direct connection to a database. Direct connections are discouraged. 
* Maintainers should keep Citizen Labs’ API keys in a secure place
* Developers should keep personal/development API keys in a secure place
* Originators should not need API keys 
### Versioning
Versioning is a way to allow structural changes to a table without breaking consuming applications.  Well at least not breaking them right away.   
* Be nice to other applications sharing a dataset by versioning 
* A new version is required when a column name changes
* A new version is required when adding a column to an existing version
* Versions should be few, no more than 3 version are in the open data portal at a time
* When a fourth version is required, the first version is removed
### Clean File Names
Clean files are final version of a dataset before it is transferred to the open data portal
*    data.world use the clean file name as its default when naming a table
### Table Names
* A noun is preferred to a verb when naming tables
* Plurals are preferred to singular nouns when naming tables
* Underscores are the preferred separator.  Spaces and hyphens are not recommended.
* Lowercase is preferred to everything else
* Don't change the name of the original source file. You may not be the originator of the file so keep the file as recognizable to the originator as possible for ease of communications.
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
* Rename source-data file name
* Script table name changes to a copy in the temp-data folder
* Rename columns
* Script column name changes
### Missing and Malformed Data
* drop entire record when Identity value is empty
* drop 
### Duplicate Data
* UUID should not duplicate   
* Open Data is about things     
### Outliers
* establish and document boundaries for column values in scripts
*         
