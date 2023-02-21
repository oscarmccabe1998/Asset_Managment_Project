import requests
import json

def getres(VulnerableSoft):
    print(VulnerableSoft.Manufacturer.lower())
    headers = {'apiKey' : 'apiKey'}
    urlbase = "https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:o:"
    urltail = ":*:*:*:*:*:*:*&cvssV2Severity=HIGH&resultsPerPage=20"
    url = urlbase+VulnerableSoft.Manufacturer.lower()+":"+VulnerableSoft.Name.lower()+":"+VulnerableSoft.Version+urltail
    print(url)
    response = requests.get(url, headers=headers)
    returnlist = []

    obj = (response.json())
    y = json.loads(json.dumps(obj))
    for item in y['vulnerabilities']:
        cve = item['cve']
        test = cve['descriptions']
        innerlist = []
        for temp in test:

            if temp['lang'] == 'en':
                #print(temp['value'])
                innerlist.append(temp['value'])
                innerlist.append(cve['vulnStatus'])
                innerlist.append(cve['lastModified'])
                innerlist.append(cve['sourceIdentifier'])
        returnlist.append(innerlist)
    #print(returnlist)
    return returnlist

if __name__ == "__main__":
    getres()
