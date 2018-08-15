# Data.World
**SLACK CHANNEL: TBD**
# Project Description:

The idea is a sharable staging area for wrangling data before transfer to an open data portal (e.g., https://data.world).  The repo stores raw data and wrangling scripts.  Citizen Lab members can push raw data into the repo and authorized members can write scripts to prepare data for transfer to an open data portal.  

With some effort, we can create a repository of data and scripts to facilitate future data wrangling and help keep our open data manageable. 

### Table of Contents
* [Definitions](#definitions)        
* Roles
* Process Roles
* Data Flow
* Process Overview
* Data Processing

### <a id="definitions">Definitions</a> 
* [Comma Separated Values](https://en.wikipedia.org/wiki/Comma-separated_values) (CSV).  CSV is a method of formatting values in a text file. 
* [GitHub](https://en.wikipedia.org/wiki/GitHub) is a technology for versioning files.

## Roles
### Curators
* Cara D
* Eileen B
### Developers
* James Wilfong   
### Maintainers (people with write access):
* Jace B
* TBD  

## Process Roles
| Curator                  | Developer                     | Maintainer                |
| :------------------      | :---------------------        | :-----------------------  |
| Curates dataset(s)       | Writes/Updates scripts        | Puts data into production |
| Loads raw dataset to GIT | Tests dataset load            | Removes data from production |
| Creates GIT pull request | Maintains GIT scripts folder  |  | 
| Signoff on Prod dataset load  | Maintains GIT tmp-data folder | Maintains the GIT master branch |
|                          | Maintains clean-data folder   | Maintains the Prod Environment |
|                          | Creates clean-data set        |  |
|                          | Maintains Dev Environment     |  |
|                          | Creates GIT pull request      |  |
|                          | Adds raw-data  sub-folders    |  |

## Data Flow

| Local      |    | GitHub     |    | Data.World.Test |    | Data.World.Prod |
| :-         | :- | :-         | :- | :-              | :- | :- |
| Curator    | >  | raw-data   |    |                 |    |  |
| Developer  | <  | raw-data   |    |                 |    |  |
|            | >  | clean-data | >  | test-data       |    |  | 
| Maintainer | <  | clean-data |    |                 |    |  |
|            | >  |            |    |                 | >  | open-data |
| App(s)     | <  |            |    |                 | <  | open-data |

## Process Overview
This is a best case scenario with no failures. Use as a guide to a successful completion of the process.   

| Curator                 |    | Developer                  |    | Maintainer                   |
| :---------------------- | :- | :------------------------- | :- | :--------------------------- |
| Prepare Dataset CSV |     |    |                            |    |                              |
| Upload Dataset          |    |                            |    |                              | 
| Create GIT pull request |    |                            |    |                              | 
| Notify Developer        | >  | Download Repo              |    |                              |
|                         |    | Setup Environment Variables |    |                             |
|                         |    | Write/Update Script        |    |                              |
|                         |    | Test Script                |    |                              |
|                         |    | Test Data Load             |    |                              |
|                         |    | Test Application           |    |                              |
|                         |    | Upload Branch              |    |                              |
|                         |    | Notify Maintainer          | >  | Download refresh-data Branch | 
|                         |    |                            |    | Setup Prod Data Environment  | 
|                         |    |                            |    | Deploy to Production         |
|                         |    |                            |    | Deployment Check             |
| Deployment Check        |    |                            | <  | Notify Curator               |
| Approve Deployment      |    |                            |    |                              |
| Notify Maintainer       | >  |                            |    | Update master Branch         |








    


