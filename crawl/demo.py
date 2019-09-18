import mysql.connector
from mysql.connector import Error  
from data_context import DataContext

#Define class context
dbclass = DataContext()

class ProductModel: 
    #Get all product -----------------------------------------
    def getProducts(self): 
        return dbclass.getData("select * from product")

    #Insert multi row  ---------------------------------------
    def insertProducts(self):
        sqlform = "Insert into product(name,price,price_new,image,lang,year,sort,status,author_id,category_id,company_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        products =  [
                        ("Đắc nhân tâm 5",100000,120000,'logo.png','vn',2019,0,1,1,1,1),
                        ("Đắc nhân tâm 6",200000,300000,'logo.png','vn',2019,0,1,1,1,1)
                    ]
        dbclass.insertMultiRowData(sqlform,products) 

    #Update row  ----------------------------------------------
    def updateProduct(self):
        sql = "Update product Set name = 'Đắc nhân tâm X' where id = 1" 
        dbclass.updateData(sql)

#Call function -----------------------------------------------------

model = ProductModel()

#model.insertProducts()
model.updateProduct()
model.getProducts()