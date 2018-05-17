from elasticsearch import Elasticsearch
# conntect es
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
# delete index if exists
if es.indices.exists('hospi_fin_10'):
    es.indices.delete(index='hospi_fin_10')
# index mappings

settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
      "doc": {
   	  "properties": {
    		"doctor_id": {"type": "integer"},
    		"d_name": {"type": "keyword"},
    		"hospital_name": {"type": "keyword"},
		"h_city": {"type": "keyword"},
    		"patient_id": {"type": "integer"},
    		"p_name": {"type": "keyword"},
    		"p_desease": {"type": "keyword"}
   }
  }
 }
}

# create index
es.indices.create(index='hospi_fin_10', ignore=400, body=settings)
