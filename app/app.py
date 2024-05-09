# src/app.py
from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator

COUCHBASE_URL = 'couchbase://couchbase:8091'
COUCHBASE_USERNAME = 'Administrator'
COUCHBASE_PASSWORD = 'password'

cluster = Cluster(COUCHBASE_URL, ClusterOptions(PasswordAuthenticator(COUCHBASE_USERNAME, COUCHBASE_PASSWORD)))
bucket = cluster.bucket('default')
collection = bucket.default_collection()

# Example operation: Get a document
result = collection.get('some-key')
print(result.content)
