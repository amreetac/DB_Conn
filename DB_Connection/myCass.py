from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect()

rows = session.execute('SELECT cluster_name, listen_address FROM system.local;')
for crow in rows:
    print crow.cluster_name, crow.listen_address
