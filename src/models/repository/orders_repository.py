from bson.objectid import ObjectId

class OrdersRepository:
    def __init__(self, db_connection):
        self.__colletion_name = "orders"
        self.__db_connection = db_connection

    def insert_document(self, document: dict) -> None:
        collection = self.__db_connection.get_collection(self.__colletion_name)
        collection.insert_one(document)

    def insert_list_of_documents(self, list_of_documents: list) -> None:
        collection = self.__db_connection.get_collection(self.__colletion_name)
        collection.insert_many(list_of_documents)

    def select_many(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__colletion_name)
        data = collection.find(doc_filter)
        return data
    
    def select_one(self, doc_filter: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__colletion_name)
        response = collection.find_one(doc_filter)
        return response
    
    def select_many_with_properties(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__colletion_name)
        data = collection.find(
            doc_filter, # Filtro de busca
            { "_id": 0, "cupom": 0} #opçoes de retorno
            )
        return data
    
    def select_if_property_exists(self) -> dict:
        collection = self.__db_connection.get_collection(self.__colletion_name)
        response = collection.find({"address": { "$exists": True }})
        return response
    
    def select_by_object_id(self, object_id: str) -> dict:
        collection = self.__db_connection.get_collection(self.__colletion_name)
        data = collection.find_one({ "_id": ObjectId(object_id) })
        return data
    
    def edit_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__colletion_name)
        collection.update_one(
            {"_id": ObjectId("6973c79d38f9e89ad952e08b")}, # Filtros
            {"$set": { "itens.pizza.quantidade": 30}} # Edição
        )

    def edit_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__colletion_name)
        collection.update_many(
            {"itens.refrigerante": {"$exists": True}}, # Filtros
            {"$set": { "itens.refrigerante.quantidade": 10}} # Edição
        )

    def edit_registry_with_increment(self) -> None:
        collection = self.__db_connection.get_collection(self.__colletion_name)
        collection.update_one(
            {"_id": ObjectId("6973c79d38f9e89ad952e08b")}, # Filtros
            {"$inc": { "itens.pizza.quantidade": 10}} # Edição
        )