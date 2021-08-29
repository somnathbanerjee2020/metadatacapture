#######################################################################################
#  Name    : load_file.py
#  Version     Author                  Date             Comments
#  1.0         Somnath Banerjee        28/08/2021       Initial Version
#######################################################################################
# This script loads the account data file placed in the data folder to the account_table 
# it logs the load stats to the job_run_status table in metadata schema


#import libraries
import yaml;
import mysql.connector;
import pandas as pd;
from datetime import datetime;
import glob;

rec_cnt=0

# Load config
stream = open('C:/metadatacapture/config/load_file_config.yaml', 'r')
configs=yaml.safe_load(stream)

# Start / Load time
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
now_t=(now,)
load_st=('load_datafile',now,'Started')

################## Processing Start entered to metadata ###########################

cnxmet = mysql.connector.connect(user=configs['dbuser'], password=configs['dbpwd'],
                              host=configs['dbhost'],
                              database=configs['auditdb'])
cursor_st = cnxmet.cursor()

query_st = "INSERT INTO metadata.job_run_status(job_name,start_time,status) VALUES (%s, %s, %s)"

cursor_st.execute(query_st,load_st)

cnxmet.commit()

#fetch latest run_id
fetch_sql="select max(run_id) from metadata.job_run_status where status = 'Started'"

cursor_rd = cnxmet.cursor()

cursor_rd.execute(fetch_sql)

w=cursor_rd.fetchall()

for row in w:
    run_id_curr=row

cursor_st.close()
cursor_rd.close()

################## Loading Datafile Start ###########################

#Create connection to load data. (Parameterize pending)
cnx = mysql.connector.connect(user=configs['dbuser'], password=configs['dbpwd'],
                              host=configs['dbhost'],
                              database=configs['datadb'])
cursor = cnx.cursor()

#Reading Datafiles
path = r'C:/metadatacapture/data'
all_files = glob.glob(path + "/datafile_*.csv")

li = []

for filename in all_files:
    df1 = pd.read_csv(filename, index_col=None, header=0)
    li.append(df1)
frame = pd.concat(li, axis=0, ignore_index=True)

df = pd.DataFrame(frame, columns= ['account_id','account_name','account_revenue','account_manager','revenue_year'])

#Insert to table
query = "INSERT INTO data.account_table(account_id,account_name,account_revenue,account_manager,revenue_year,updated_date, run_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"

for row in list(df.itertuples(index=False, name=None)):
    row += now_t
    row += run_id_curr
    cursor.execute(query,row)
    rec_cnt += 1
cnx.commit()

cursor.close()
cnx.close()

################## Loading Datafile Done ###########################

# End time
nowe = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
nowe_t=(nowe,rec_cnt) 

cursor_end = cnxmet.cursor()

updsql = "UPDATE metadata.job_run_status SET end_time = %s, status = 'Completed', records_inserted = %s WHERE status = 'Started'"

cursor_end.execute(updsql,nowe_t)

cnxmet.commit()

print(cursor_end.rowcount, "record(s) affected")

cursor_end.close()
cnxmet.close()