from bs4 import BeautifulSoup
import requests, json
from pprint import pprint

def ngo_details_from_giveindia():
    link = ("https://www.giveindia.org/certified-indian-ngos")
    res = requests.get(link)
    soup = BeautifulSoup(res.text, "html.parser")
    name = soup.find_all("td",class_="jsx-697282504")
    Name, list2, list3 = [], [], []
    for j in name:
        list2.append(j.text)
        aaa = j.find("div")
        if aaa == None:
            pass
        else:
            list2.remove(aaa.text)
            Name.append(aaa.text)

    c=1
    state, education = [], []
    for i in list2:
        if c%2 == 0:
            state.append(i)
        else:
            education.append(i)
        c+=1

    for i,j,k in zip(Name,education,state):
        dict1={}
        dict1["Name"] = i
        dict1["Cause"] = j
        dict1["State"] = k
        list3.append(dict1.copy())
    
    json_files = open("Ngo_data.json", "w")
    json.dump(list3, json_files, indent = 4)
    json_files.close()
    return list3

details = ngo_details_from_giveindia()
# pprint(details)

