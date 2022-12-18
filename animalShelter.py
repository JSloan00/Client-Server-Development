from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        if username and password:
            self.client = MongoClient('mongodb://%s:%s@localhost:38888/AAC' % (username, password)) # Make sure port is updated with current port used
            self.database = self.client['AAC'] # Database name inside brackets
            # print("Connection successful")

    # Define create method
    def create(self, data):
        # If data parameter has data 
        if data is not None:
            # Inserts data as a new object
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
        else:
            # Create exception if parameter is empty
            raise Exception("Nothing to save because data parameter is empty")
            
        
    # Define read method 
    def read(self, search):
        # Search the database for data object
        searchResult = self.database.animals.find(search,{"_id":False})
        # Return searchResult
        return searchResult
                
    # Define update method
    def update(self, curValue, newValue):
        # if curValue and newValue parameters have data
        if curValue and newValue is not None:
            # Update data object
            if curValue and newValue:
                updateResult = self.database.animals.update_one(curValue, {"$set": newValue})
                # Find new object
                find = self.database.animals.find(newValue)
                # Print new object
                for r in find:
#                     print("Update Result: ", r)    THIS DOES NOT WORK WITH DASHBOARD
                    return r
            else:
                # Create exception if data parameter is empty
                raise Exception("Nothing to update because data parameters are empty")
            
    #Define delete method
    def delete(self, data):
        # If data parameter had data
        if data is not None:
            # Create variable to hold data object
            dataObj = self.database.animals.find(data)
            # Prints out data object that is being deleted
            for r in dataObj:
#                 print("Deleted: ", r)    THIS DOES NOT WORK WITH DASHBOARD
                return r
            # Remove data object
            deleteResult = self.database.animals.delete_many(data)
            print("Remove Count: ", deleteResult.deleted_count)
        else:
            # Create exception if parameter is emtpy
            raise Exception("Nothing to delete because data parameter is empty")
                