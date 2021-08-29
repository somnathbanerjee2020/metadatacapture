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

# Configuration
Database: MySQL running on AWS RDS
Execution Script: Python

# Manual Installation Needed

The application needs a manual setup to be executed. The instructions below are for Windows machines.

- Install Python 3.x 
- Install / Update the following packages if not available

```
pip install pyyaml
pip install mysql.connector
pip install pandas
pip install datetime
```

