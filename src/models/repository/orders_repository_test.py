from .orders_repository import OrdersRepository

class CollectionMock:
    def __init__(self):
        self.insert_one_attributes = {}
        self.find_attributes = {}
    
    def insert_one(self, input_data: any):
        self.insert_one_attributes["dict"] = input_data

    def find(self, *args):
        self.find_attributes["args"] = args

class DbCollectionMock:
    def __init__(self, collection):
        self.get_collection_attributes = {}
        self.collection = collection
    
    def get_collection(self, collection_name):
        self.get_collection_attributes["name"] = collection_name
        return self.collection
    
def test_insert_document():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrdersRepository(db_connection)

    doc = { "alguma": "coisa"}
    repo.insert_document(doc)

    assert collection.insert_one_attributes["dict"] == doc

def test_select_many_with_properties():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repo = OrdersRepository(db_connection)

    doc = { "testando": "find"}
    repo.select_many_with_properties(doc)

    assert collection.find_attributes["args"][0] == doc
    assert collection.find_attributes["args"][1] == { "_id": 0, "cupom": 0}
