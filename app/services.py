from app.entities import InMemoryItem

class InMemoryService:

    def add_inmemory_item(self, item: dict, data_store: dict) -> InMemoryItem:
        """add_inmemory_item valida que si el data_stored contiene el key. Si no existe agregará un InMemoryItem con la versión y valor correcto"""
        to_add = InMemoryItem(item["value"], 1, item["key"])
        if item["key"] in data_store:
            version = len(data_store[item["key"]]) + 1
            to_add.version = version
            data_store[item["key"]][version] = to_add
        else:
            data_store[item["key"]] = {1:to_add}

        return to_add


    def get_inmemory_item(self, key, data_store:dict, version = 0) -> InMemoryItem:
        """Regresa el item solicitado. Si la versión no existe regresará el mas cercano. Si no existe el key lanzará una excepción KeyError

        Args:
            key (any): La llave que se debe buscar en el data_store
            data_store (dict): Objeto en memoria que se usa para almacenar datos
            version (int, optional): Version especifica que se busca. Defaults 0.

        Raises:
            KeyError: Es lanzado cuando el key no es encontrado en el data_store

        Returns:
            InMemoryItem: Objeto que contiene la información del dato almacenado
        """
        
        if key not in data_store:
            raise KeyError(key)
        if version not in data_store[key]:
            version = len(data_store[key])
        return data_store[key][version]
