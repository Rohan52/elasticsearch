from elasticsearch import Elasticsearch
# conntect es
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
# delete index if exists
if es.indices.exists('shakespeare_2'):
    es.indices.delete(index='shakespeare_2')
# index mappings

settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
      "doc": {
   	  "properties": {
    		"speaker": {"type": "keyword"},
    		"play_name": {"type": "keyword"},
    		"line_id": {"type": "integer"},
    		"speech_number": {"type": "integer"}
   }
  }
 }
}

# create index
es.indices.create(index='shakespeare_2', ignore=400, body=settings)



