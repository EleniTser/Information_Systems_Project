import pandas as pd
import subprocess
import time

push_gateway_url = "http://localhost:9091"
input_file = "~/info_sys/data/medium-data-mod.csv"

counter = 1

columns = ["series_text", "metric_text", "hostname", "region", "datacenter", "rack", "os", "arch", "team", "service", "service_version", "service_environment", "usage_type", "date", "timestamp", "value"] 

df = pd.read_csv(input_file, header=None, names=columns)

job_list=[]
start_time = time.time()
for index, row in df.iterrows():
    metric_name = row["usage_type"]
    labels = 'hostname="{hostname}", region="{region}", datacenter="{datacenter}", rack="{rack}", os="{os}", arch="{arch}", team="{team}", service="{service}", service_version="{service_version}", service_environment="{service_environment}", date="{date}", timestamp="{timestamp}"'.format(
        hostname=row["hostname"],
        region=row["region"],
        datacenter=row["datacenter"],
        rack=row["rack"],
        os=row["os"],
        arch=row["arch"],
        team=row["team"],
        service=row["service"],
        service_version=row["service_version"],
        service_environment=row["service_environment"],
        date=row["date"],
        timestamp=row["timestamp"]
    )

    value = row["value"]
    prometheus_line = '{}{{{}}} {}'.format(metric_name, labels, value)
    
    metric_url = '{}/metrics/job/{}'.format(push_gateway_url, metric_name)
    metric_data = '# TYPE {} gauge\n{}\n'.format(metric_name, prometheus_line)

 
    job_name = metric_name+"_"+row["hostname"]
    job_list.append(job_name)
    
    curl_command = 'curl --data-binary \'{}\' {}/metrics/job/{}'.format(metric_data, push_gateway_url, job_name)

    try:
        result = subprocess.run(curl_command, shell=True, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error executing command:", e)
        print("Error output: ", e.stderr)
    
    if counter==1000:
        counter=1 
    
end_time = time.time()
elapsed_time = end_time - start_time
print(f'Total time for data loading: {elapsed_time}')
