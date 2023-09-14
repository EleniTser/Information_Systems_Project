import os
import time
import subprocess

# Set the paths and options
dsbulk_path = "/home/user/info_sys/cassandra/dsbulk-1.11.0/bin/dsbulk"  # Path to the DSBulk executable
keyspace = "mykeyspace"

tables = ["query_{}_table".format(i) for i in range(1, 11)] 

csv_file_1 = "/home/user/info_sys/cassandra/csv_file_1"
csv_file_2 = "/home/user/info_sys/cassandra/csv_file_2"
csv_file_3 = "/home/user/info_sys/cassandra/csv_file_3"
csv_file_4 = "/home/user/info_sys/cassandra/csv_file_4"

time_list = {}
for table in ["query_1_table", "query_2_table", "query_3_table", "query_4_table", "query_5_table", "query_6_table"]: 
    start_time = time.time()
    dsbulk_cmd = [
        dsbulk_path,
        "load",
        "-h", "192.168.0.2",
        "-k", keyspace,
        "-t", table,
        "-url", csv_file_1,
        "-header", "false",
        "-delim", ",",  
        "-m", "0=hostname, 1=usage_type, 2=timestamp, 3=value"
        ]

    try:
        subprocess.run(dsbulk_cmd, check=True)
        print("CSV data loaded successfully using DSBulk.")
    except subprocess.CalledProcessError as e:
        print("Error:", e)
    end_time = time.time()
    time_list[table] = end_time - start_time
 
for table in ["query_7_table", "query_9_table"]:
    start_time = time.time()
    dsbulk_cmd = [
        dsbulk_path,
        "load",
        "-h", "192.168.0.2",
        "-k", keyspace,
        "-t", table,
        "-url", csv_file_2,
        "-header", "false",
        "-delim", ",",  
        "-m", "0=datacenter, 1=usage_type, 2=timestamp, 3=value"
        ]

    try:
        subprocess.run(dsbulk_cmd, check=True)
        print("CSV data loaded successfully using DSBulk.")
    except subprocess.CalledProcessError as e:
        print("Error:", e)
    end_time = time.time()
    time_list[table] = end_time - start_time

table = "query_8_table"
start_time = time.time()
dsbulk_cmd = [
    dsbulk_path,
    "load",
    "-h", "192.168.0.2",
    "-k", keyspace,
    "-t", table,
    "-url", csv_file_3,
    "-header", "false",
    "-delim", ",",  
    "-m", "0=hostname, 1=datacenter, 2=usage_type, 3=timestamp, 4=value"
    ]

try:
    subprocess.run(dsbulk_cmd, check=True)
    print("CSV data loaded successfully using DSBulk.")
except subprocess.CalledProcessError as e:
    print("Error:", e)
end_time = time.time()
time_list[table] = end_time - start_time


table = "query_10_table"
start_time = time.time()
dsbulk_cmd = [
    dsbulk_path,
    "load",
    "-h", "192.168.0.2",
    "-k", keyspace,
    "-t", table,
    "-url", csv_file_4,
    "-header", "false",
    "-delim", ",", 
    "-m", "0=hostname, 1=datacenter, 2=service, 3=usage_type, 4=timestamp, 5=value"
    ]

try:
    subprocess.run(dsbulk_cmd, check=True)
    print("CSV data loaded successfully using DSBulk.")
except subprocess.CalledProcessError as e:
    print("Error:", e)
end_time = time.time()
time_list[table] = end_time - start_time

print(time_list)
