from cassandra.cluster import Cluster
from prettytable import PrettyTable
import time
import psutil

# Connect to Cassandra
cluster = Cluster(['192.168.0.2'])
session = cluster.connect()

try:
    session.set_keyspace('mykeyspace')
except Exception as e:
    print(e)


exec_times = {}

start_cpu_usage = psutil.cpu_percent(interval=1, percpu=False)
   
## Query 1
# Values of a specific usage_type for each host in the last timestamp
query1 = "SELECT hostname, value FROM query_1_table WHERE usage_type='usage_idle' ORDER BY timestamp DESC LIMIT 100;"

#print("\nQuery 1: Values of usage_idle for each host in the last timestamp.")
try:
    start_time = time.time()
    rows = session.execute(query1)
    end_time = time.time()     
 
    exec_times["query1"]=end_time-start_time;
    
    print(f'Query:{query1}')
    print(f'Latency:{end_time-start_time} seconds\n')
    '''	
    data = PrettyTable()
    data.field_names = ["Hostname", "Value"]
    data.align = "l"
    data.align["Value"] = "r"
    for row in rows:
        data.add_row([row.hostname, row.value])
    print(data)
    '''
except Exception as e:
    print(e)

## Query 2
# Values of all usage_types for a specific host in the last timestamp
query2 = "SELECT usage_type, value FROM query_2_table WHERE hostname='host_2' ORDER BY timestamp DESC LIMIT 10;"

#print("\nQuery 2: Values of all usage types for host_2 in the last timestamp.")
try:
    start_time = time.time()
    rows = session.execute(query2)
    end_time = time.time()

    exec_times["query2"]=end_time-start_time;
    print(f'Query:{query2}')
    print(f'Latency:{end_time-start_time} seconds\n')    
    ''' 
    data = PrettyTable()
    data.field_names = ["Usage", "Value"]
    data.align = "l"
    data.align["Value"] = "r"
    for row in rows:
        data.add_row([row.usage_type, row.value])
    print(data)
    '''
except Exception as e:
    print(e)

## Query 3
# Average value of a specific usage_type over all hosts in the last timestamp
query3 = "SELECT AVG(value) as avg_value FROM query_3_table WHERE usage_type='usage_user'"

#print("\nQuery 3: Average value of usage_user of all hosts in the last timestamp.")
try:
    start_time = time.time()
    rows = session.execute(query3)
    end_time = time.time()

    exec_times["query3"]=end_time-start_time;
    print(f'Query:{query3}')
    print(f'Latency:{end_time-start_time} seconds\n')    
    '''
    data = PrettyTable()
    data.field_names = ["Average Value"]
    data.align = "l"
    data.align["Average Value"] = "r"
    for row in rows:
        data.add_row([row.avg_value])
    print(data)
    '''
except Exception as e:
    print(e)

## Query 4
# Average value of a specific usage_type for a specific host
query4 = "SELECT MAX(value) as avg_value FROM query_4_table WHERE hostname='host_3' AND usage_type='usage_user'"

#print("\nQuery 4: Maximum value of usage_user for host_3.")

try:
    start_time = time.time()
    rows = session.execute(query4)
    end_time = time.time()

    exec_times["query4"]=end_time-start_time;
    print(f'Query:{query4}')
    print(f'Latency:{end_time-start_time} seconds\n')
    '''
    data = PrettyTable()
    data.field_names = ["Maximum Value"]
    data.align = "l"
    data.align["Maximum Value"] = "r"
    for row in rows:
        data.add_row([row.avg_value])
    print(data)
    '''
except Exception as e:
    print(e)

## Query 5
# Max value of a specific usage_type for each host
query5 = "SELECT hostname, AVG(value) as max_value FROM query_5_table WHERE usage_type='usage_irq' GROUP BY hostname"

#print("\nQuery 5: Average value of usage_irq for each host.")
try:
    start_time = time.time()
    rows = session.execute(query5)
    end_time = time.time()

    exec_times["query5"]=end_time-start_time;
    print(f'Query:{query5}')
    print(f'Latency:{end_time-start_time} seconds\n')
    '''
    data = PrettyTable()
    data.field_names = ["Hostname", "Average Value"]
    data.align = "l"
    data.align["Average Value"] = "r"
    for row in rows:
        data.add_row([row.hostname, row.max_value])
    print(data)
    '''
except Exception as e:
    print(e)

## Query 6
# Sum the most recent values of a specific usage type.
query6 = "SELECT SUM(value) as summary FROM query_6_table WHERE usage_type='usage_iowait' AND timestamp=1672552740000000000"

#print("\nQuery 6: Sum the most recent values of usage_iowait")
try:
    
    start_time = time.time()
    rows = session.execute(query6)
    end_time = time.time()

    exec_times["query6"]=end_time-start_time;
    print(f'Query:{query6}')
    print(f'Latency:{end_time-start_time} seconds\n')
    '''
    data = PrettyTable()
    data.field_names = ["Sum"]
    data.align = "l"
    data.align["Sum"] = "r"
    for row in rows:
        data.add_row([row.summary])
    print(data)
    '''
except Exception as e:
    print(e)


## Query 7 
# Max value of a specific usage_type for a scpecific datacenter
query7 = "SELECT MAX(value) as max_value FROM query_7_table WHERE datacenter='us-west-2b' AND usage_type = 'usage_guest'"

#print("\nQuery 7: Maximum value of usage_guest for datacenter=us-west-2b.")
try:
    start_time = time.time()
    rows = session.execute(query7)
    end_time = time.time()

    exec_times["query7"]=end_time-start_time;
    print(f'Query:{query7}')
    print(f'Latency:{end_time-start_time} seconds\n')
    '''
    data = PrettyTable()
    data.field_names = ["Max Value"]
    data.align = "l"
    data.align["Max Value"] = "r"
    for row in rows:
        data.add_row([row.max_value])
    print(data)
    '''
except Exception as e:
    print(e)

## Query 8 
# Value of each usage_type for a specific datacenter in the last timestamp
query8 = "SELECT hostname, usage_type, value FROM query_8_table WHERE datacenter='us-west-1b' ORDER BY timestamp DESC LIMIT 80"

#print("\nQuery 8: Values of all usage types for datacenter=us-west-1b in the last timestamp.")
try:
    start_time = time.time()
    rows = session.execute(query8)
    end_time = time.time()

    exec_times["query8"]=end_time-start_time;
    print(f'Query:{query8}')
    print(f'Latency:{end_time-start_time} seconds\n')
    '''
    data = PrettyTable()
    data.field_names = ["Hostname", "Usage", "Value"]
    data.align = "l"
    data.align["Value"] = "r"
    for row in rows:
        data.add_row([row.hostname, row.usage_type, row.value])
    print(data)
    '''
except Exception as e:
    print(e)

## Query 9
# Max value in a specific datacenter
query9 = "SELECT MAX(value) as max_value FROM query_9_table WHERE datacenter='ap-southeast-1a'"

#print("\nQuery 9: Maximum value for datacenter=ap-southeast-1a.")
try:
    start_time = time.time()
    rows = session.execute(query9)
    end_time = time.time()

    exec_times["query9"]=end_time-start_time;
    print(f'Query:{query9}')
    print(f'Latency:{end_time-start_time} seconds\n')
    '''
    data = PrettyTable()
    data.field_names = ["Max Value"]
    data.align = "l"
    data.align["Max Value"] = "r"
    for row in rows:
        data.add_row([row.max_value])
    print(data)
    '''
except Exception as e:
    print(e)

## Query 10
# Average value of a specific usage_type for a specific datacenter and a specific service
# Needs index on service
query10 = "SELECT AVG(value) as avg_value FROM query_10_table WHERE datacenter='us-west-1b' AND usage_type='usage_iowait' AND service='4'"

#print("\nQuery 10: Average value of usage_iowait for datacenter=us-west-1b and service=4.")
try:
    start_time = time.time()
    rows = session.execute(query10)
    end_time = time.time()

    exec_times["query10"]=end_time-start_time;
    print(f'Query:{query10}')
    print(f'Latency:{end_time-start_time} seconds\n')
    '''
    data = PrettyTable()
    data.field_names = ["Average Value"]
    data.align = "l"
    data.align["Average Value"] = "r"
    for row in rows:
        data.add_row([row.avg_value])
    print(data)
    '''
except Exception as e:
    print(e)
end_cpu_usage = psutil.cpu_percent(interval=1, percpu=False)

total_latency = 0
#print("\nQuery Latencies:")
for t in exec_times:
    total_latency += exec_times[t]
    #print(f'{t}: {exec_times[t]} sec')

total_queries = 10

throughput = total_queries/total_latency

print(f'Total Latency: {total_latency} seconds')
print(f'Throughput: {throughput} queries per second')

total_cpu_usage = end_cpu_usage - start_cpu_usage
print(f"Total CPU Usage: {total_cpu_usage}%")
