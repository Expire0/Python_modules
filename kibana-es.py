from elasticsearch import Elasticsearch,RequestsHttpConnection
from esquery import esquery
#https://github.com/influxdata/influxdb-python/issues/240
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

mas = Elasticsearch('<host>', verify_certs=False,use_ssl=True
 ,connection_class=RequestsHttpConnection,ssl_show_warn=False)

#https://github.com/elastic/elasticsearch-py/issues/712
#res = mas.search(index="quv3*", body={"query": {"match_all": {}}})
res = mas.search(index="quuv*", body=esquery() )
print(res)
print("Got %d Hits:" % res['hits']['total'])
