from __future__ import print_function
import requests
import base64
import csv
import json
from tabulate import tabulate
from pandas.io.json import json_normalize

from requests.exceptions import HTTPError
pat = '{PAT}'
authorization = str(base64.b64encode(bytes(':'+pat, 'ascii')), 'ascii')
headers = {
    'Accept': 'application/json',
    'Authorization': 'Basic '+authorization
}
response = requests.get(
    url="https://dev.azure.com/{ORG}/JAVA/_apis/git/repositories/{REPO}/pullrequests?searchCriteria.status=completed&api-version=6.1-preview.1", headers=headers)
#sys.stdout = open("mytest.json", "w")
#azDict = response.json()
#az_json = json.dumps(azDict)
#print(az_json)
#sys.stdout.close()
request_text = response.text

data = json.loads(request_text)

data_serialization = json.dump(data, open('data.json', "w"), indent= 4)

with open("./data.json") as file:
    data = json.load(file)

fname = "output.csv"

with open(fname, "w") as file:
    csv_file = csv.writer(file)
    csv_file.writerow(["createdBy","creationDate","closedDate","title","mergeStatus"])
    for item in data["value"]:
        csv_file.writerow([item['createdBy']['displayName'],item['creationDate'],item['closedDate'],item['mergeStatus']])
