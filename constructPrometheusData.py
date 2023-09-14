import pandas as pd
import subprocess
import time

push_gateway_url = "http://localhost:9091"

input_file = "~/info_sys/data/medium-data-mod.csv"
#input_file = "~/data-500"
#output_file = "/home/user/medium-data.txt"
#output_lines = []
counter = 1

columns = ["series_text", "metric_text", "hostname", "region", "datacenter", "rack", "os", "arch", "team", "service", "service_version", "service_environment", "usage_type", "date", "timestamp", "value"] 

df = pd.read_csv(input_file, header=None, names=columns)

job_list=[]
start_time = time.time()
for index, row in df.iterrows():
    metric_name = row["usage_type"]
    labels = 'hostname="{hostname}", region="{region}", datacenter="{datacenter}", rack="{rack}", os="{os}", arch="{arch}", team="{team}", service="{service}", service_version="{service_version}", service_environment="{service_environment}", date="{date}", timestamp="{timestamp}"'.format(
        hostname=row["hostname"],#.split("=")[1],
        region=row["region"],#.split("=")[1],
        datacenter=row["datacenter"],#.split("=")[1],
        rack=row["rack"],#.split("=")[1],
        os=row["os"],#.split("=")[1],
        arch=row["arch"],#.split("=")[1],
        team=row["team"],#.split("=")[1],
        service=row["service"],#.split("=")[1],
        service_version=row["service_version"],#.split("=")[1],
        service_environment=row["service_environment"],#.split("=")[1],
        date=row["date"],
        timestamp=row["timestamp"]
    )
    #timestamp = row["timestamp"]
    value = row["value"]
    prometheus_line = '{}{{{}}} {}'.format(metric_name, labels, value)
    #prometheus_line = '{}{{{}}} {} {}'.format(metric_name, labels, value, timestamp)
    #output_lines.append(prometheus_line)
    metric_url = '{}/metrics/job/{}'.format(push_gateway_url, metric_name)
    metric_data = '# TYPE {} gauge\n{}\n'.format(metric_name, prometheus_line)

    #time_instance = int(time.time()) + counter
    #curl_command = f'curl --data-binary "{metric_data}" {push_gateway_url}/metrics/job/{metric_name}'
    #/instance/{time_instance}'
    job_name = metric_name+"_"+row["hostname"] #+ "_" +str(counter)
    job_list.append(job_name)
    #curl_command = f'curl --data-binary "{metric_data}" {push_gateway_url}/metrics/job/{job_name}'
    curl_command = 'curl --data-binary \'{}\' {}/metrics/job/{}'.format(metric_data, push_gateway_url, job_name)

    #print(curl_command)
    # Execute the curl command using subprocess
    try:
        result = subprocess.run(curl_command, shell=True, capture_output=True, text=True, check=True)
        #print("Command output: ", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error executing command:", e)
        print("Error output: ", e.stderr)
    
    if counter==1000:
        counter=1 
    """      
    if counter>0 and (counter+1)%1000==0:
        garbage_start = time.time()
        time.sleep(4)
        for job in job_list:
            delete_curl_command = 'curl -X DELETE {}/metrics/job/{}'.format(push_gateway_url, job)
            #job_list.remove(job)
            try:
                delete_result = subprocess.run(delete_curl_command, shell=True, capture_output=True, text=True, check=True)
                # print(delete_curl_command)
                # print("Delete Command output: ", delete_result.stdout)
            except subprocess.CalledProcessError as e:
                print("Error executing command:", e)
                print("Error output: ", e.stderr)
            # job_list.remove(job)
        job_list=[]
        print('Job list:', counter)
        garbage_end = time.time()
        garbage_time += garbage_end - garbage_start
     
    counter += 1
    """
end_time = time.time()
elapsed_time = end_time - start_time
print(f'Total time for data loading: {elapsed_time}')
#prometheus_data = '\n'.join(output_lines)

#with open(output_file, 'w') as f:
#    f.write(prometheus_data)



