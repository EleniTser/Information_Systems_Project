# Information Systems Project NTUA 2022-2023

## Overall Description

In this project, we were asked to compare the performance of various aspects of two popular time-series database systems, Apache Cassandra and Prometheus. 
The tasks that we had to complete were the following:

- Installation and setup of the two Time-Series DBs.
- Data generation (or discovery of real data) and loading to the two DBs: Using either a specific data generator, online data or artificially creating data ourselves. Also, the same data should be loaded in both databases data loading process should be monitored. Namely, the time it takes to load the final amount of data, as well as the storage space it takes in each of the databases (i.e. how efficient data compression is).
- Query generation to measure performance: A set of queries (common to both DBs) must be compiled in order to test the querying performance of the timeseries DB storage and indexing. Depending on the data, queries should target the time dimension in both point and range queries (and multiple ranges and grouping functions, i.e. average, group-by, window queries).
- Measurement of relevant performance metrics for direct comparison: Client process(es) should pose the queries of the previous step and measure the DB performance (query latency, throughput, CPU load if possible, etc).

### Installation and setup

According to the installation and setup of the 2 timeseries databases, we installed the latest version of both of them from their official page. Apache Cassandra features also a distributed edition, so we setted up a cluster with 2 nodes for the purposes of this project.  

### Data Generation

For the generation of the data, we used Time Series Benchmark Suite (TSBS, https://github.com/timescale/tsbs), which for some time-series DBs (specifically Apache Cassandra in our case) contains code for data generation, loading, queries and measurement. We just used the TSBS for the data generation and we generated 3 datasets with different sizes using the cpu-only case. 

Same datasets were loaded to Prometheus local db after editing them based on the Prometheus data format. 

### What you'll find in this repo

Configuration files for both nodes of the Cassandra cluster, and respectively the configuration files of the Prometheus DB.
- `initScript.py` : Python Script that connects to our Cassandra cluster, create a keyspace and the appropriate tables based on our queries.
- `cassandraQueries.py` : Python script that after connecting to our Cassandra cluster, runs the specified queries and returns us the corresponding metrics of the queries execution i.e. latency per query, total latency, throughput. 
- `loadCSVWithdsbulk.py` : Python script that implements the data loading to our previously created tables (loading on Cassandra is implemented using the DSBulk load utility).
- `pandasModifyCSVData.py` : Python script that modifies the dataset in order to remove from the rows the part before the `=` which corresponds to the same header for all. The output file is the one that we load to the database.
- `getPrometheusMetrics.py` : Python script that runs the queries to Prometheus and gives us the corresponding metrics of the queries execution, same metrics as in Cassandra.
  
For the data loading in the Prometheus local db, we used Prometheus Pushgateway. Since our data were not real time, we pushed them in time intervals to Pushgateway so that the timestamps set by Prometheus "correspond" to the timestamps of the original data, and thus we we were able to achieve consistency in the results of the queries concerning time between the two databases.
