
try:
    import cPickle as pickle
except:
    import pickle
import gzip

with open('/home/mohacsi/Desktop/optimizer/optimizer/checkpoint.pkl', 'rb') as f:
    BPO_pkl = pickle.load(f)

# BPO_pkl = pickle.load('/home/mohacsi/Desktop/optimizer/optimizer/checkpoint.pkl')

print(BPO_pkl)

print(BPO_pkl.keys())

print(BPO_pkl['population'])
'''
print len(BPO_pkl['logbook'])
print BPO_pkl['logbook']
'''
print(len(BPO_pkl['population'][0])) 
print(len(BPO_pkl['population']))

'''
print len(BPO_pkl['halloffame'])
print BPO_pkl['parents']
print len(BPO_pkl['parents'])
print BPO_pkl['history']
'''
