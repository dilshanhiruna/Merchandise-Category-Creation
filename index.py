import dbconnector
import uuid

class Merchandise_Main_Category:
    
    def __init__(self,Main_ID,CategoryName,active) :
        self.Main_ID = Main_ID
        self.CategoryName =CategoryName
        self.active=active
    
    
            
# class Merchandise_Sub_Category:
    
#     def __init__(self,Sub_ID ,CategoryName,active) :
#         self.Sub_ID  = Sub_ID
#         self.CategoryName =CategoryName
#         self.active=active


def add():
    newMainCat = str(input("Do you want to create new Category? (Y/N) "))
    newSubCat = str(input("Do you want to create new Sub Category? (Y/N) "))

    if(newMainCat == "Y"):

        UniqueID_Main =uuid.uuid4().hex
        Main_Category_name =str(input("Enter Main Category name: "))
        sql ="INSERT INTO merchandise_main_category(Main_ID,catagoryName,ActiveStatus)\
             VALUES('%s', '%s', true)" % (UniqueID_Main,Main_Category_name)
        dbconnector.mycursor.execute(sql)
        dbconnector.connection.commit()

        newPhoto = str(input("Do you want to add a Category image? (Y/N) "))

        if(newPhoto == "Y"):
            image_location ="image_location"
            sql ="INSERT INTO image_catagories(level,category_id,image_location,dimensions)\
            VALUES('%d', '%s', '%s','%d')" % (1,UniqueID_Main,image_location, 1920)
            dbconnector.mycursor.execute(sql)
            dbconnector.connection.commit()

    else:
        pass

    if(newSubCat == "Y"):
        dbconnector.mycursor.execute("SELECT * FROM merchandise_main_category")
        myresult = dbconnector.mycursor.fetchall()
        
        Main_Categories = []
        for x in myresult:
           Main_Categories.append(Merchandise_Main_Category(x[0],x[1],x[2])) 

        for x in Main_Categories:
            print(x.CategoryName)
        
        selectCat = str(input("Enter a Main Category from the above list: "))

        Notfound=True
        for x in Main_Categories:
            if(x.CategoryName==selectCat):
                sql ="INSERT INTO Merchandise_Sub_Category(Sub_ID,ActiveStatus,category_id)\
                     VALUES('%s', true, '%s')" % (uuid.uuid4().hex,x.Main_ID)
                dbconnector.mycursor.execute(sql)
                dbconnector.connection.commit()
                Notfound=False
                break
            else:
                Notfound=True
                
        if(Notfound): 
            print("Invalid Main Category")
  
    else:
        pass
        
    

    

add()