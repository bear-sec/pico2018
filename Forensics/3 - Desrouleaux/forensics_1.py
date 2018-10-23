from collections import Counter
import json


a = json.load(open(r'C:\Users\Gera\Downloads\incidents.json','r'))
b = a['tickets']
print 'cahl 1'
print Counter([x['src_ip'] for x in b]).values()
print Counter([x['src_ip'] for x in b]).keys()
print 'chal 2'
print [x['dst_ip'] if x['src_ip']=='21.201.106.115' else None for x in b]
print 'chal 3'
print Counter([x['file_hash'] for x in b]).values()
print Counter([x['file_hash'] for x in b]).keys()
