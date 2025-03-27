class HotelsDataBase(object):
    def __init__(self, connectingString):
        self.connectingString = connectingString
        self.lines = []
        self.update_hotels_list()
        
    def add_hotel(self, name, price, region, mark, myMark):
        row = f"{name} {price} {region} {mark} {myMark}\n"  
        
        with open(self.connectingString, 'r+') as file:
            lines = file.readlines()
            file.seek(0)  

            for line in lines:
                file.write(line)
            
            file.write(row)
   
        self.update_hotels_list()
    
    def update_hotel(self, name, updaterow):
         with open(self.connectingString, 'r+') as file:
             lines = file.readlines()
             file.seek(0)  
             for line in lines:
                 new_name = line.split()[0]
                 if new_name == name:
                     file.write(updaterow)
                 else: file.write(line)
         self.update_hotels_list()
        
    def delete_hotel(self, row):
        
        with open(self.connectingString, 'r+') as file:
            lines = file.readlines()
            file.seek(0)  

            for line in lines:
                if row not in line: 
                    file.write(line)
        
            file.truncate()
        self.update_hotels_list()
    
    def update_hotels_list(self):
        with open(self.connectingString, 'r') as file:
            self.lines = file.readlines()
            
    pass




