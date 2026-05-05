from database.DAO import DAO

distanza = 5
allObjects = DAO.getAllFlights(distanza)
print(len(allObjects))
