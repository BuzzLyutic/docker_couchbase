const couchbase = require('couchbase');
const cluster = new couchbase.Cluster('couchbase://couchbase', {
 username: 'username',
 password: 'password',
});

const bucket = cluster.bucket('bucket-name');
const collection = bucket.defaultCollection();

async function run() {
 try {
    // Example: Upsert a document
    await collection.upsert('test-doc', { message: 'Hello, Couchbase!' });
    console.log('Document upserted');

    // Example: Get the document
    const result = await collection.get('test-doc');
    console.log('Document content:', result.content);
 } catch (error) {
    console.error('Error:', error);
 }
}

run();
