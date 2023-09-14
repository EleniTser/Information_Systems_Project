import subprocess
import time
import psutil

# Prometheus server URL
PROMETHEUS_SERVER = "http://prometheus-server:9090"

# List of PromQL queries
QUERIES = [
    "usage_idle",
    "{hostname=\"host_2\"}",
    "avg(usage_user)",
    "max(max_over_time(usage_user{hostname=\"host_3\"}[15h]))",
    "avg(avg_over_time(usage_irq[5h])) by(hostname)",
    "sum(usage_iowait)",
    "max(max_over_time(usage_guest{datacenter=\"us-west-2b\"}[15h]))",
    "{datacenter=\"us-west-1b\"}",
    "max(max_over_time({datacenter=\"ap-southeast-1a\"}[15h]))",
    "avg(avg_over_time(usage_iowait{datacenter=\"us-west-1b\", service=\"4\"}[5h]))",
]

# Initialize variables
total_latency = 0
total_queries = 0

# Function to measure CPU usage
def measure_cpu_usage():
    return psutil.cpu_percent(interval=1, percpu=False)  # Interval in seconds

# Function to calculate latency
def calculate_latency(start_time, end_time):
    return end_time - start_time

# Start measuring CPU usage
start_cpu_usage = measure_cpu_usage()

# Loop through the queries
for query in QUERIES:
    # Send query and record start time using curl
    start_time = time.time()
    curl_command = f'curl -g "{PROMETHEUS_SERVER}/api/v1/query?query={query}"'
    response = subprocess.getoutput(curl_command)
    end_time = time.time()

    # Calculate latency for the query
    latency = calculate_latency(start_time, end_time)
    print(f"Query: {query}")
    print(f"Latency: {latency:.4f} seconds\n")
    # Increment the total latency and query count
    total_latency += latency
    total_queries += 1

# Stop measuring CPU usage
end_cpu_usage = measure_cpu_usage()

# Calculate and display throughput
throughput = total_queries / total_latency if total_latency > 0 else 0
total_cpu_usage = end_cpu_usage - start_cpu_usage
print(f"Total Queries: {total_queries}")
print(f"Total Latency: {total_latency:.4f} seconds")
print(f"Total CPU Usage: {total_cpu_usage}%")
print(f"Throughput: {throughput:.4f} queries per second")
