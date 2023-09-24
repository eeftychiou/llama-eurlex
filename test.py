import os

from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index import StorageContext, load_index_from_storage

import zeep

from zeep import Client
from zeep.wsse.username import UsernameToken
from zeep.plugins import HistoryPlugin
import config

print(os.environ)
input("Tets")
history = HistoryPlugin()

eul_username = config.username
eul_password = config.password
# set the WSDL URL
wsdl_url = "https://eur-lex.europa.eu/eurlex-ws?wsdl"

client = Client(
    wsdl_url,
    wsse=UsernameToken(eul_username, eul_password),plugins=[history])
# client.settings(raw_response=True)

# order_type = client.get_type('ns0:searchRequest')

request_data  = {
    'expertQuery': 'DN=3*',
    'page':1,
    'pageSize': 10,
    'searchLanguage':'en',
    'limitToLatestConsleg':'false',
    'excludeAllConsleg': 'true'
}

que='Title~"Decision (EU) 2016/342"'
que2= 'SELECT DN WHERE DN=6*'

# respo = client.service.doQuery(**request_data)
respo = client.service.doQuery(expertQuery=que2, page=1, pageSize=10, searchLanguage='en' )

print (respo)

documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
response = query_engine.query("Can an incident result in an accident? What someone must do when he observes something amiss in an airplane ?")
print(response)
