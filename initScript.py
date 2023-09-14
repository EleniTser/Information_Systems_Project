from cassandra.cluster import Cluster

# Connect to Cassandra
cluster = Cluster(['192.168.0.2']) 
session = cluster.connect()

# Create the keyspace
session.execute("CREATE KEYSPACE IF NOT EXISTS mykeyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '2'}")

# Create the table
session.execute("""
    CREATE TABLE IF NOT EXISTS mykeyspace.cputable (
        series_text TEXT,
        metric_text TEXT,
        hostname TEXT,
        region TEXT,
        datacenter TEXT,
        rack TEXT,
        os TEXT,
        arch TEXT,
        team TEXT,
        service TEXT,
        service_version TEXT,
        service_environment TEXT,
        usage_type TEXT,
        date DATE,
        timestamp BIGINT,
        value BIGINT,
        PRIMARY KEY ((hostname, region, datacenter, rack, os, arch, team, service, service_version, service_environment, usage_type, date), timestamp)
    )
""")

session.execute("""
    CREATE TABLE IF NOT EXISTS mykeyspace.query_1_table (
        hostname TEXT,
        usage_type TEXT,
        timestamp BIGINT,
        value BIGINT,
        PRIMARY KEY (usage_type, timestamp, hostname)
    )
    WITH CLUSTERING ORDER BY (timestamp ASC)
""")

session.execute("""
    CREATE TABLE IF NOT EXISTS mykeyspace.query_2_table (
        hostname TEXT,
        usage_type TEXT,
        timestamp BIGINT,
        value BIGINT,
        PRIMARY KEY (hostname, timestamp, usage_type)
    )
    WITH CLUSTERING ORDER BY (timestamp ASC)
""")

session.execute("""
    CREATE TABLE IF NOT EXISTS mykeyspace.query_3_table (
        hostname TEXT,
        usage_type TEXT,
        timestamp BIGINT,
        value BIGINT,
        PRIMARY KEY (usage_type, hostname)
    )
""")

session.execute("""
    CREATE TABLE IF NOT EXISTS mykeyspace.query_4_table (
        hostname TEXT,
        usage_type TEXT,
        timestamp BIGINT,
        value BIGINT,
        PRIMARY KEY ((hostname, usage_type), timestamp)
    )
""")

session.execute("""
    CREATE TABLE IF NOT EXISTS mykeyspace.query_5_table (
        hostname TEXT,
        usage_type TEXT,
        timestamp BIGINT,
        value BIGINT,
        PRIMARY KEY (usage_type, hostname, timestamp)
    )
""")

session.execute("""
    CREATE TABLE IF NOT EXISTS mykeyspace.query_6_table (
        hostname TEXT,
        usage_type TEXT,
        timestamp BIGINT,
        value BIGINT,
        PRIMARY KEY (usage_type, hostname, timestamp)
    )
""")

session.execute("CREATE INDEX IF NOT EXISTS timestamp_index ON mykeyspace.query_6_table(timestamp)")

session.execute("""
    CREATE TABLE IF NOT EXISTS mykeyspace.query_7_table (
        datacenter TEXT,
        usage_type TEXT,
	timestamp BIGINT,
        value BIGINT,
        PRIMARY KEY ((datacenter, usage_type),timestamp)
    )
""")

session.execute("""
    CREATE TABLE IF NOT EXISTS mykeyspace.query_8_table (
        hostname TEXT,
        datacenter TEXT,
        usage_type TEXT,
        timestamp BIGINT,
        value BIGINT,
        PRIMARY KEY (datacenter, timestamp, usage_type, hostname)
    )
    WITH CLUSTERING ORDER BY (timestamp ASC)
""")

session.execute("""
    CREATE TABLE IF NOT EXISTS mykeyspace.query_9_table (
        datacenter TEXT,
        usage_type TEXT,
        timestamp BIGINT,
        value BIGINT,
        PRIMARY KEY (datacenter, timestamp, usage_type)
    )
    WITH CLUSTERING ORDER BY (timestamp ASC)
""")

session.execute("""
    CREATE TABLE IF NOT EXISTS mykeyspace.query_10_table (
        hostname TEXT,
        datacenter TEXT,
        service TEXT,
        usage_type TEXT,
        timestamp BIGINT,
        value BIGINT,
        PRIMARY KEY ((datacenter, usage_type), hostname, service, timestamp)
    )
""")

session.execute("CREATE INDEX IF NOT EXISTS service_index ON mykeyspace.query_10_table(service)")
