| [Overview](/README.md) 
|----|

# Summary
Code for Data Ingestion and Metadata Capture

# Solution Approach
The solution ingests a data file and captures the following metadata:
- Load ID (Unique Sequence ID for the load)
- Execution Start and End time
- Excution Status
- Number of records loaded

# Technologies used
- Database: MySQL running on AWS RDS
- Execution Language: Python

# Setup
The solution ingests all .csv files placed in the /data folder. The file name needs to start with datafile_ and needs to have an extension of.csv. A template file has been provided in the folder for reference on the column structure.


# Manual Installation Needed

The application needs a manual setup to be executed. The instructions below are for Windows machines.

- Install Python 3.x ( developed on Python 3.8.3)
- Install / Update the following packages if not available

```
pip install pyyaml
pip install mysql.connector
pip install pandas
pip install datetime
```
- Install a database client. Suggested: [MySQL Workbench](https://dev.mysql.com/downloads/workbench/)

