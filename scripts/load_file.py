# This script loads the account data file placed in the data folder to the account_table 
# it logs the load stats to the job_run_status table in metadata schema
# Assumptions: The files placed is in CSV format with , as a seperator and .csv as extension

#import libraries
import yaml;
import mysql.connector;
import pandas as pd;
from datetime import datetime;
import glob;

# Load config
stream = open('config\load_file_config.yaml', 'r')
configs=yaml.safe_load(stream)

# Add currenttime
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
now_t=(now,) 

rec_cnt=0

#Create connection. (Parameterize pending)
cnx = mysql.connector.connect(user='proc_mon', password='checkwork',
                              host='metastore.cpogzsn5ewwn.ap-southeast-2.rds.amazonaws.com',
                              database=configs['auditdb'])
cursor = cnx.cursor()

#Reading Datafile
path = r'data'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df1 = pd.read_csv(filename, index_col=None, header=0)
    li.append(df1)
frame = pd.concat(li, axis=0, ignore_index=True)

#data = pd.read_csv (r'data\datafile_20210827.csv')   
df = pd.DataFrame(frame, columns= ['account_id','account_name','account_revenue','account_manager','revenue_year'])

#Insert to table
query = "INSERT INTO data.account_table(account_id,account_name,account_revenue,account_manager,revenue_year,updated_date) VALUES (%s, %s, %s, %s, %s, %s)"

for row in list(df.itertuples(index=False, name=None)):
    row += now_t
    cursor.execute(query,row)
    rec_cnt += 1
cnx.commit()

print(rec_cnt)

cursor.close()
cnx.close()