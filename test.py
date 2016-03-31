from pymongo import MongoClient
from sklearn import cluster, datasets
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import offsetbox
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE

def connectToDatabase(URI):
    client = MongoClient(URI)
    db = client.get_default_database()
    #print client.database_names()
    #print db.collection_names()
    accounts = db['accounts']
    cursor = accounts.find()
    #print cursor.count()
    users, usernames = loadAccounts(cursor)
    #print users
    predictedClusters = clusterAccounts(users)
    #print usernames
    #printAccounts(cursor)
    visulize(users,predictedClusters)
    client.close()
    #db.drop_collection('accounts')

def loadAccounts(accounts):
    usernames = []
    array = []
    for account in accounts:
        array.append([str(getGenderValue(account['gender'])),str(getAgeGroup(account['ageGroup'])),
                      #str(account['country']), str(account['state']),
                      str(account['musicAlternative']), str(account['musicBlues']), str(account['musicChildren']),
                      str(account['musicCountry']), str(account['musicDanceEMD']), str(account['musicElectronic']),
                      str(account['musicHipHopRap']), str(account['musicJazz']), str(account['musicOpera']),
                      str(account['musicPop']), str(account['musicRAndBSoul']), str(account['musicReggae']),
                      str(account['musicRock']), str(account['museumHistory']), str(account['museumTheme']),
                      str(account['museumArt']), str(account['movieAction']), str(account['movieAdventure']),
                      str(account['movieAnimation']), str(account['movieBiography']), str(account['movieComedy']),
                      str(account['movieCrime']), str(account['movieDocumentary']), str(account['movieDrama']),
                      str(account['movieFamily']), str(account['movieFantasy']), str(account['movieHistory']),
                      str(account['movieHorror']), str(account['movieMusical']), str(account['movieRomance']),
                      str(account['movieSciFi']), str(account['movieSport']), str(account['movieThriller']),
                      str(account['movieWar']), str(account['movieWestern']), str(account['nightlifePub']),
                      str(account['nightlifeBrewery']), str(account['nightlifeBar']), str(account['nightlifeSports']),
                      str(account['nightlifeDive']), str(account['nightlifeWine']), str(account['nightlifeLounge']),
                      str(account['nightlifeNightclub']), str(account['restaurantBurger']), str(account['restaurantCafe']),
                      str(account['restaurantScandinavian']), str(account['restaurantGeneral']), str(account['restaurantItalian']),
                      str(account['restaurantSushi']), str(account['restaurantBBQ']), str(account['restaurantIndian']),
                      str(account['restaurantMexican']), str(account['restaurantVegetarian']), str(account['restaurantSteakhouse']),
                      str(account['restaurantTapas']), str(account['restaurantOriental'])])
        usernames.append(str(account['username']))
    #print array
    d = dict()
    d.setdefault('data',array)
    return d, usernames

def getGenderValue(gender):
    if(gender=='Mann'):
        return 0
    elif(gender=='Kvinne'):
        return 1
    else:
        return 2

def getAgeGroup(ageGroup):
    age = str(ageGroup)
    if(age=='0-19'):
        return 0
    elif(age=='20-29'):
        return 1
    elif(age=='30-39'):
        return 2
    elif(age=='40-49'):
        return 3
    elif(age=='50-59'):
        return 4
    elif(age=='60-69'):
        return 5
    else:
        return 6

def clusterAccounts(users):
    accounts = users['data']
    #print accounts
    k_means = cluster.KMeans(n_clusters=2)
    k_means.fit(accounts)
    print k_means.labels_[::1]
    return k_means.predict(accounts)

def visulize(users, clusters):
    account = users['data']
    X = np.array(account)
    model = TSNE(n_components=2,random_state=0)
    np.set_printoptions(suppress=True)
    reduserteData = model.fit_transform(X)
    #plt.scatter(bilde[:,0], bilde[:,1],c='r',marker='^')
    i=0
    for datapunkt in reduserteData:
        if clusters[i] == 0:
            plt.scatter(datapunkt[0],datapunkt[1],c='r',marker='^')
        elif clusters[i] == 1:
            plt.scatter(datapunkt[0],datapunkt[1],c='g',marker='^')
        elif clusters[i] == 2:
            plt.scatter(datapunkt[0],datapunkt[1],c='b',marker='^')
        elif clusters[i] == 3:
            plt.scatter(datapunkt[0],datapunkt[1],c='r',marker='o')
        elif clusters[i] == 4:
            plt.scatter(datapunkt[0],datapunkt[1],c='g',marker='o')
        elif clusters[i] == 5:
            plt.scatter(datapunkt[0],datapunkt[1],c='b',marker='o')
        elif clusters[i] == 6:
            plt.scatter(datapunkt[0],datapunkt[1],c='r',marker='+')
        elif clusters[i] == 7:
            plt.scatter(datapunkt[0],datapunkt[1],c='g',marker='+')
        elif clusters[i] == 8:
            plt.scatter(datapunkt[0],datapunkt[1],c='b',marker='+')
        else:
            plt.scatter(datapunkt[0],datapunkt[1], c='r', marker='*')
        i=i+1
    plt.xlabel('X Label')
    plt.ylabel('Y Label')


    model3D = TSNE(n_components=3,random_state=0)
    reduserteData3D = model3D.fit_transform(X)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #print bilde
    i = 0
    for datapunkt in reduserteData3D:
        print clusters[i]
        if clusters[i] == 0:
            ax.scatter(datapunkt[0],datapunkt[1],datapunkt[2],c='r',marker='^')
        elif clusters[i]==1:
            ax.scatter(datapunkt[0],datapunkt[1],datapunkt[2],c='g',marker='^')
        elif clusters[i]==2:
            ax.scatter(datapunkt[0],datapunkt[1],datapunkt[2],c='b',marker='^')
        elif clusters[i]==3:
            ax.scatter(datapunkt[0],datapunkt[1],datapunkt[2], c='r', marker='o')
        elif clusters[i]==4:
            ax.scatter(datapunkt[0],datapunkt[1],datapunkt[2], c='g', marker='o')
        elif clusters[i]==5:
            ax.scatter(datapunkt[0],datapunkt[1],datapunkt[2], c='b', marker='o')
        elif clusters[i]==6:
            ax.scatter(datapunkt[0],datapunkt[1],datapunkt[2], c='r', marker='+')
        elif clusters[i]==7:
            ax.scatter(datapunkt[0],datapunkt[1],datapunkt[2], c='g', marker='+')
        elif clusters[i]==8:
            ax.scatter(datapunkt[0],datapunkt[1],datapunkt[2], c='b', marker='+')
        else:
            ax.scatter(datapunkt[0],datapunkt[1],datapunkt[2], c='r', marker='*')
        i= i+1
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()


def loadData(filename):
    f = file(filename,'r')
    users = []
    for line in f:
        users.append(line.split(' '))
        #print line.split(' ')
    f.close()
    d = dict()
    d.setdefault('data',users)
    return d

def printAccounts(Accounts):
    for account in Accounts:
        #print('Username: %s, age: %s' % (account['username'], account['ageGroup']))
        print "Username: " + str(account['username'])
        print "Gender: " + str(account['gender'])
        print "Age: " + str(account['ageGroup'])
        print "Country: " + str(account['country'])
        print "State: " + str(account['state'])
        print "  "
        print "MUSIC"
        print "alternative: " + str(account['musicAlternative'])
        print "Blues: " + str(account['musicBlues'])
        print "Children: " + str(account['musicChildren'])
        print "Country: " + str(account['musicCountry'])
        print "DanceEMD: " +str(account['musicDanceEMD'])
        print "Electronic: " + str(account['musicElectronic'])
        print "Hip-hop Rap: " + str(account['musicHipHopRap'])
        print "Jazz: " + str(account['musicJazz'])
        print "Opera: " + str(account['musicOpera'])
        print "Pop: " + str(account['musicPop'])
        print "R and B Soul: " + str(account['musicRAndBSoul'])
        print "Reggae: " + str(account['musicReggae'])
        print "Rock: " + str(account['musicRock'])
        print "  "
        print "MUSEUM"
        print "History: " + str(account['museumHistory'])
        print "Theme: " + str(account['museumTheme'])
        print "Art: " + str(account['museumArt'])
        print "  "
        print "MOVIE"
        print "Action: " + str(account['movieAction'])
        print "Adventure: " + str(account['movieAdventure'])
        print "Animation: " + str(account['movieAnimation'])
        print "Biography: " + str(account['movieBiography'])
        print "Comedy: " + str(account['movieComedy'])
        print "Crime: " + str(account['movieCrime'])
        print "Documentary: " + str(account['movieDocumentary'])
        print "Drama: " + str(account['movieDrama'])
        print "Family: " + str(account['movieFamily'])
        print "Fantasy: " + str(account['movieFantasy'])
        print "History: " + str(account['movieHistory'])
        print "Horror: " + str(account['movieHorror'])
        print "Musical: " + str(account['movieMusical'])
        print "Romance: " + str(account['movieRomance'])
        print "Sci-fi: " + str(account['movieSciFi'])
        print "Sport: " + str(account['movieSport'])
        print "Thriller: " + str(account['movieThriller'])
        print "War: " + str(account['movieWar'])
        print "Western: " + str(account['movieWestern'])
        print "  "
        print "NIGHTLIFE"
        print "Pub: " + str(account['nightlifePub'])
        print "Brewery: " + str(account['nightlifeBrewery'])
        print "Bar: " + str(account['nightlifeBar'])
        print "Sports: " + str(account['nightlifeSports'])
        print "Dive: " + str(account['nightlifeDive'])
        print "Wine: " + str(account['nightlifeWine'])
        print "Lounge: " + str(account['nightlifeLounge'])
        print "Nightclub: " + str(account['nightlifeNightclub'])
        print "  "
        print "RESTAURANT"
        print "Burger: " + str(account['restaurantBurger'])
        print "Cafe: " + str(account['restaurantCafe'])
        print "Scandinavian: " + str(account['restaurantScandinavian'])
        print "General: " + str(account['restaurantGeneral'])
        print "Italian: " + str(account['restaurantItalian'])
        print "Sushi: " + str(account['restaurantSushi'])
        print "BBQ: " + str(account['restaurantBBQ'])
        print "Indian: " + str(account['restaurantIndian'])
        print "Mexican: " + str(account['restaurantMexican'])
        print "Vegetarian: " + str(account['restaurantVegetarian'])
        print "Steakhouse: " + str(account['restaurantSteakhouse'])
        print "Tapas: " + str(account['restaurantTapas'])
        print "Oriental: " + str(account['restaurantOriental'])
        print "   "
        print "OTHER"
        print "Radius: " + str(account['radius'])
        print "  "
        #print account


def main():
    MONGODB_URI = 'mongodb://localhost:27017/tourism_mongoose'
    connectToDatabase(MONGODB_URI)
    #users = loadData('fixedUsers.txt')
    #clusters = clusterAccounts(users)
    #visulize(users,clusters)

main()






