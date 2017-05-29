import pymongo

from pymongo import MongoClient
dbConnection = MongoClient("localhost", 27017)
dbTable = dbConnection.dbCompany

def main():
    while(1):
        optSelect = input("\n1 - Insert, 2 - Update, 3 - Select, 4 - Delete\n")
        if optSelect == "1":
            Insert()
        elif optSelect == "2":
            Update()
        elif optSelect == "3":
            Select()
        elif optSelect == "4":
            Delete()
        else:
            print("\nINVALID SELECTION\n")


def Insert():
    try:
        dbTable.companies.insert_one(
            {"index": 3.0, "name": "MVL"}
        )
        print("\nInserted data successfully\n")

    except Exception as ex:
        print(ex)



def Update():
    try:
        for lin in dbTable.companies.find():
            if lin["index"] == 3.0:
                dbTable.companies.update_one({"_id": lin["_id"]},{"$set": {"name": "MZ''"}})
        print("\nRecords updated successfully\n")

    except Exception as ex:
        print(ex)


def Select():
    try:
        for lines in dbTable.companies.find():
            print(lines)
        print("\nAll data from Company database\n")

    except Exception as ex:
        print(ex)



def Delete():
    try:
        dbTable.companies.remove()
        #dbTable.companies.remove({"index": 3.0})
        print("\nDeletion successfull\n")

    except Exception as ex:
        print(ex)





main()