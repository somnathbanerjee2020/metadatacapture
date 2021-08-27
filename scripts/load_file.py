# This script loads the account data file placed in the data folder to the account_table 
# it logs the load stats to the job_run_status table in metadata schema
# Assumptions: The file placed is in CSV format with ~ as a seperator



import yaml;
import mysql.connector;


stream = open('config\load_file_config.yaml', 'r')
configs=yaml.safe_load(stream)

print(configs)