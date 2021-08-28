| [Overview](/README.md) 
|----|

# Summary
Code for Data Ingestion and Metadata Capture

# Solution Approach
The solution ingests a data file and captures the following metadata:
- Load ID (Unique Sequence ID for the load)
- Name of the file loaded
- Execution Start and End time
- Excution Status
- Target Table
- Number of records loaded

# Configuration
Database: MySQL running on AWS RDS
Execution Script: Python

# Installation Needed
Install the following packages if not available
```
pip install pyyaml
pip install mysql
pip install mysql.connector

```