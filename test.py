from pymongo import MongoClient
from sklearn import cluster, datasets


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
    clusterAccounts(users)
    print usernames
    #printAccounts(cursor)
    client.close()
    print "Finished"
    #db.drop_collection('accounts')

def loadAccounts(accounts):
    usernames = []
    array = []
    for account in accounts:
        array.append([str(account['musicCountry']), str(account['musicAlternative'])])
        usernames.append(str(account['username']))
    #print array
    d = dict()
    d.setdefault('data',array)
    return d, usernames

def clusterAccounts(users):
    accounts = users['data']
    print accounts
    k_means = cluster.KMeans(n_clusters=2)
    k_means.fit(accounts)
    print k_means.labels_[::1]
    #iris = datasets.load_iris()
    #X_iris = iris.data
    #y_iris = iris.target
    #k_means = cluster.KMeans(n_clusters=3)
    #k_means.fit(X_iris)
    #print(k_means.labels_[::10])
    #print(y_iris[::10])
    #print iris
    #print X_iris


def loadData(filename):
    f = file(filename,'r')
    users = []
    for line in f:
        users.append(line.split(' '))
    f.close()
    k_means = cluster.KMeans(n_clusters=9)
    k_means.fit(users)
    print k_means.labels_[::1]
    #print k_means.score()
    return users

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
    #connectToDatabase(MONGODB_URI)
    users = loadData('users.txt')

main()






