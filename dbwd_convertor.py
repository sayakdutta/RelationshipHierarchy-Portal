import os

file = open('dbwd.csv')

filecontent = file.readlines()
file.close()
root = ['rel']
level1 = ['per', 'loc', 'org']

level2 = []

def createNode(name):
	temp = {
	"name": name,
	"children": []
	}

	return temp
	

def findChild(dicti, child):
	temp = next((item for item in dicti["children"] if item["name"] == child), False)

	return temp


def addChild(dicti, child):
	childDict = createNode(child)
	dicti["children"].append(childDict)


	


data = {"name": root[0], "children": [] }

for lev in level1:
	addChild(data, lev)


for line in filecontent[2:]:
	rels = line.replace(',',' ').strip().split(".")

	# print(rels)
	tdict = data
	for i in range(1, len(rels)-1):
		tdict = findChild(tdict, rels[i])
		if not tdict:
			print("noooooooo")
		if not findChild(tdict, rels[i+1]):
			addChild(tdict, rels[i+1])


import simplejson as json


with open('dbwd.json', 'w') as file:
     file.write(json.dumps(data, indent=4, sort_keys=True))




		



