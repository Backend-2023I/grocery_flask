import tinydb
from tinydb import Query

class GroceryDB:
    def __init__(self):
        self.db = tinydb.TinyDB('db.json',indent=4, separators=(',', ': '))
        self.table = self.db.table('grocery')

    def add(self, grocery: dict):
        '''Add a fruit to the database
        
        Args:
            fruit (dict): A dictionary containing the fruit name, quantity, price and type
        '''
        if grocery.get("name") == None:
            return {"result": "name field not found"}
        
        elif grocery.get("quantity") == None:
            return {"result": "quantity field not found"}
        
        elif grocery.get("price") == None:
            return {"result": "price field not found"}
        
        elif grocery.get("type") == None:
            return {"result": "type field not found"}
        
        else:
            self.table.insert(grocery)
            return {"result": "successfully"}


    def all(self):
        '''Get all fruits from the database'''
        data = self.table.all()
        return data

    
    def get_by_type(self, type: str) -> list:
        '''Get all fruits of a specific type from the database
        
        Args:
            type (str): The type of fruit to get
        
        Returns:
            list: A list of fruits of the specified type
        '''
        User = Query()
        data = self.table.search(User.type == type)
        return data

    def get_by_name(self, name: str) -> list:
        '''Get all fruits of a specific name from the database
        
        Args:
            name (str): The name of fruit to get
        
        Returns:
            list: A list of fruits of the specified name
        '''
        User = Query()
        data = self.table.get(User.name == name)
        return data

    def get_by_price(self, price: float) -> list:
        '''Get all fruits of a specific price from the database
        
        Args:
            price (float): The price of fruit to get
        
        Returns:
            list: A list of fruits of the specified price
        '''
        User = Query()
        data = self.table.search(User.price == price)
        return data
    
    def update_by_doc_id(self, doc_id, data):
        data = self.table.update(data, doc_ids=[doc_id])
        return data
    