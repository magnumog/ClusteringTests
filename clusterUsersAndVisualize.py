import numpy as np
from pymongo import MongoClient
from sklearn import cluster
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import offsetbox
from datetime import datetime

def getUsersFromDatabase(URI):
    client = MongoClient(URI)
    db = client.get_default_database()
    accounts = db['accounts']
    return accounts.find()

def getUsersFromCursor(cursor):
    usernames = []
    array = []
    for account in cursor:
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

def clusterUsers(users, numberOfClusters,reducedData):
    accounts=None
    if(reducedData==False):
        accounts = users['data']
    else:
        accounts=users
    k_means = cluster.KMeans(n_clusters=numberOfClusters)
    k_means.fit(accounts)
    return k_means.predict(accounts)

def reduceDimensions(users,numberOfDimensions):
    accounts = users['data']
    X = np.array(accounts)
    model = TSNE(n_components=numberOfDimensions,random_state=0)
    np.set_printoptions(suppress=True)
    reduserteData = model.fit_transform(X)
    return reduserteData

def visualize2DClusterBeforeReduction(users,numberOfClusters):
    clusters = clusterUsers(users, numberOfClusters,False)
    reduserteData = reduceDimensions(users,2)
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
    plt.title("visualize 2D Cluster Before Reduction")
    plt.show()

def visualize3DClusterBeforeReduction(users,numberOfClusters):
    clusters = clusterUsers(users, numberOfClusters,False)
    reduserteData3D = reduceDimensions(users,3)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    i = 0
    for datapunkt in reduserteData3D:
        #print clusters[i]
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
    ax.set_title('visualize 3D Cluster Before Reduction')
    plt.show()

def visualize2DReduceBeforeCluster(users,numberOfClusters):
    reduserteData = reduceDimensions(users,2)
    clusters = clusterUsers(reduserteData, numberOfClusters, True)
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
    plt.title("visualize 2D Reduction Before Cluster")
    plt.show()

def visualize3DReduceBeforeCluster(users,numberOfClusters):
    reduserteData3D = reduceDimensions(users,3)
    clusters = clusterUsers(reduserteData3D, numberOfClusters, True)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    i = 0
    for datapunkt in reduserteData3D:
        #print clusters[i]
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
    ax.set_title('visualize 3D Reduction Before Cluster')
    plt.show()

def readUsersFromFile(filename):
    f = file(filename,'r')
    users = []
    username = []
    for line in f:
        data = line.split(' ')
        username.append(data.pop(0))
        users.append(data)
    f.close()
    d = dict()
    d.setdefault('data',users)
    return d, username

def insertUserAndClusterToDatabase(URI,username, cluster):
    client = MongoClient(URI)
    db = client.tourism_mongoose
    clusterAccount = db.clusters
    post = { "username" : username ,
             "cluster" : str(cluster),
             "updateTime" : datetime.utcnow() }
    post_id = clusterAccount.insert_one(post).inserted_id

def updateUserAndClusterToDatabase(URI,username,cluster):
    client = MongoClient(URI)
    db = client.tourism_mongoose
    clusterAccount = db.clusters.update_one(
        { "username" : username },
        {"$set":{"cluster" : str(cluster),"updateTime" : datetime.utcnow()}}
    )
    if(clusterAccount.modified_count==0):
        insertUserAndClusterToDatabase(URI,username,cluster)

def updateDatabase(URI,users,clusters):
    for i in range(0,len(users)):
        updateUserAndClusterToDatabase(URI, users[i], clusters[i])
    print "Database Updated"

def getUsersInClusters(URI,clusterNumber):
    client = MongoClient(URI)
    db = client.get_default_database()
    cursor = db.clusters.aggregate(
        [
            {"$match": {"cluster" : str(clusterNumber)}}
        ]
    )
    for document in cursor:
        print document['username']


def main():
    MONGODB_URI = 'mongodb://localhost:27017/tourism_mongoose'
    #cursor = getUsersFromDatabase(MONGODB_URI)
    #users, username = getUsersFromCursor(cursor)
    #users, username = readUsersFromFile('fixedUsers.txt')
    #clusters = clusterUsers(users, 8, False)
    #visualize2DClusterBeforeReduction(users,5)
    #visualize3DClusterBeforeReduction(users,5)
    #visualize2DReduceBeforeCluster(users,5)
    #visualize3DReduceBeforeCluster(users,5)
    #updateDatabase(MONGODB_URI,username,clusters)
    getUsersInClusters(MONGODB_URI, 2)


main()
