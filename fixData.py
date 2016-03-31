def readData(filename):
    f= file(filename,'r')
    users = []
    for line in f:
        tempUser = line.split(' ')
        tempUser.pop(0)
        tempUser = tempUser[0].split('\t')
        tempUser.pop(0)
        tempUser[0] = genderValue(tempUser[0])
        tempUser[1] = maritialStatus(tempUser[1])
        tempUser[2] = ageValue(tempUser[2])
        users.append(tempUser)
    return users

def genderValue(gender):
    if(gender=='Mann'):
        return 0
    elif(gender=='Kvinne'):
        return 1
    else:
        return 2

def maritialStatus(status):
    if(status=='Enslig'):
        return 0
    elif status=='Gift/Partner':
        return 1
    elif status=='Samboer':
        return 2
    elif status=='Separert':
        return 3
    elif status=='Forlovet':
        return 4
    elif status=='Enke/Enkemann':
        return 5
    elif status=='Skilt':
        return 6
    else:
        return 7

def ageValue(age):
    age = int(age)
    if(age>0 and age<=19):
        return 0
    elif(age>=20 and age<=29):
        return 1
    elif(age>=30 and age<=39):
        return 2
    elif(age>=40 and age<=49):
        return 3
    elif(age>=50 and age<=59):
        return 4
    elif(age>=60 and age<=69):
        return 5
    else:
        return 6

def writeToFile(users, filename):
    f = file(filename, 'r+')
    for user in users:
        line = ""
        for attribut in user:
            line = line + str(attribut) + " "
        f.write(line)
    f.close()

def main():
    users = readData('brukerData.txt')
    writeToFile(users, 'fixedUsers.txt')


main()