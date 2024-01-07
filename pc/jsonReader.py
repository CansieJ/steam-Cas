import json
try:a=open("storage/steam.json")
except:a=open("storage/steam.json")
data=json.load(a)

def lijst1x(type,a=True):
    lijst=[]
    typelijst=[]
    if type=="genres":
        for item in data:
            typelijst.append(item[f"{type}"].split(";"))
    else:
        for item in data:
            typelijst.append(item[f"{type}"])
    if a==True:
        for item in typelijst:
            for item2 in item:
                if item2 not in lijst:
                    lijst.append(item2)
        return lijst
    if a==False:
        return typelijst

#print(lijst1x("genres"))
#print(lijst1x("name",False))
def amount(naam, type):
    try:
        lijst=[]
        for item in data:
            lijst.append(item[f"{type}"].split(";"))
    except:
        print(Exception)
    num=0
    for item in lijst:
        for subitem in item:
            if naam in subitem:
                num+=1
    return num
#print(amount("Strategy","genres"))
def stats(type,l=False):
    types=lijst1x(type)
    if l==False:
        for item in types:
            print(f"{item} {amount(item,type)}")
    if l==True:
        list=[]
        for item in types:
            list.append(f"{item} {amount(item, type)}")
        return list
#print(stats("genres"))
#print(stats("genres",True))
def percentage(naam,type,t=True):
    g1=amount(f"{naam}",f"{type}")
    try:
        lijst=[]
        for item in data:
            lijst.append(item[f"{type}"].split(";"))
    except:
        print(Exception)
    counter=0
    if t==True:
        for item in lijst:
            for subitem in item:
                counter+=1
    if t==False:
        for item in lijst:
            counter+=1
    totaal=counter
    return 100/totaal*g1
#print(percentage("Action","genres",True))
#print(percentage("Action","genres",False))

def rating(game):
    for item in data:
        if type(game)!=int:
            if item["name"]==game:
                pos=item["positive_ratings"]
                neg=item["negative_ratings"]
                break
        if type(game)== int:
            if item["appid"]==game:
                pos=item["positive_ratings"]
                neg=item["negative_ratings"]
                break
    totaal=pos+neg
    rating=(pos/totaal)*100
    return rating
#print(rating("Yakuza 0"))
#print(rating(10))




#extra
aantalgames=len(data)
aantalpublishers=(len(lijst1x("publisher")))
aantaldevelopers=(len(lijst1x("developer")))
aantalgenres=(len(lijst1x("genres")))



