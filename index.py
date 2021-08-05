import dbconnector

class Merchandise_Main_Category:
    
    def __init__(self,Main_ID,CategoryName,active) :
        self.Main_ID = Main_ID
        self.CategoryName =CategoryName
        self.active=active
        self.sub_categories =[]

    def add_sub_categories(self, Merchandise_Sub_Category):
        self.sub_categories.append(Merchandise_Sub_Category)
            
class Merchandise_Sub_Category:
    
    def __init__(self,Sub_ID ,CategoryName,active, Merchandise_Main_Category) :
        self.Sub_ID  = Sub_ID
        self.MainID = Merchandise_Main_Category.Main_ID
        self.CategoryName =CategoryName
        self.active=active

# m = Merchandise_Main_Category(12,"Food",True)
# m .add_sub_categories(Merchandise_Sub_Category(23,"Kottu",True,m))
# m .add_sub_categories(Merchandise_Sub_Category(25,"Rice",True,m))

def add():
    newMainCat = str(input("Do you want to create new Category? (Y/N) "))
    if(newMainCat == "Y"):
        Main_Category_name =str(input("Enter Main Category name: "))
        m=Merchandise_Main_Category(1,Main_Category_name,True)



add()