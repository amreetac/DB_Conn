from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect('animals')

session.set_keyspace('animals')
session.execute('USE animals;')

#rows = session.execute('SELECT type FROM monkeys;')
#for crow in rows:
 #   print crow.type


#Simple example

rows = session.execute('SELECT type, family FROM monkeys;')
for crow in rows:
    print crow.type, crow.family
