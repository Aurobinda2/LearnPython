import json
import os
with open('states.json','r')as f:
    #convert json to <dict> object
     data=json.load(f)

for state in data['states']: # for each state value in 'states' key
    print (state) # Raw data from states <dict> object

print()
print('****************************************************')
print( )

serial=1
for state in data['states']:
    #Add one 'Serial Key to the <dict> object
    state['Serial']=serial
    serial+=1
for state in data['states']:
    print (state)

# dump(put the updated <dict>(data) to a json file with name new_states.json)

with open('new_states.json','w')as f:
    json.dump(data,f,indent=2,sort_keys=True)

#check the existance of new file
print(os.path.exists('new_states.json'))





