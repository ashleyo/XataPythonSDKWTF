import json
import xata


client = xata.client.XataClient()

# get all records, all columns
post = client.search_and_filter().queryTable("jsonformatter", {"columns":[]})
records = json.loads(post.text)['records']
IK = set()
for selection in (s:=records[0]['selections']):
    IK.add(s[selection])
print(IK)
