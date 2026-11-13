from random import Random

class Tiny_smart_python_database:
    def __init__(self, file_name, owner ):
        self.file_name=file_name
        self.owner=owner
        self.ID= Random.randint(self,1,1000)
    
    def menu(self):
        print("main menu:\n1.new data type\n2.new data\n3.save\n4.query\n5.back to main menu\n6.exit\n")
        
        
        