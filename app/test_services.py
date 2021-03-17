from app.entities import InMemoryItem
from app.services import InMemoryService
import unittest


class InMemoryServiceTest(unittest.TestCase):

    def setUp(self):
        self.service = InMemoryService()
        self.data_store = dict()
    
    def test_add_inmemory_item(self):
        """Valida que se registre correctamente un item"""

        item = {"key": "test", "value": "a value"}
        self.service.add_inmemory_item(item, self.data_store)

        self.assertEqual(self.data_store["test"][1].key, item["key"], "El InMemoryItem debe contener el key")
        self.assertEqual(self.data_store["test"][1].value, item["value"], "No se guardo el dato requerido")
        self.assertEqual(self.data_store["test"][1].version, 1, "La versión no corresponde a la necesaria")

    
    def test_add_inmemory_item_exists(self):
        """Valida que cuando se agrega un item que existe lo haga como una nueva versión"""

        item = {"key": "test", "value": "new value"}
        existing = {"key": "test", "value": "a value"}
        self.service.add_inmemory_item(existing, self.data_store)

        self.service.add_inmemory_item(item, self.data_store)

        self.assertEqual(self.data_store["test"][2].key, item["key"], "El InMemoryItem debe contener el key")
        self.assertEqual(self.data_store["test"][2].value, item["value"], "No se guardo el dato requerido")
        self.assertEqual(self.data_store["test"][2].version, 2, "La versión no corresponde a la necesaria")

    def test_add_multiple_items(self):
        """Valida que funcione correctamente el metodo add_inmemory_item cons varios keys"""
        table_test = [
            {"item": {"key":"a", "value":"a1"}, "expected": {"version":1}},
            {"item": {"key":"a", "value":"a2"}, "expected": {"version":2}},
            {"item": {"key":"a", "value":"a3"}, "expected": {"version":3}},
            {"item": {"key":"b", "value":"b1"}, "expected": {"version":1}},
            {"item": {"key":"b", "value":"b2"}, "expected": {"version":2}},
            {"item": {"key":"b", "value":"b3"}, "expected": {"version":3}},
            {"item": {"key":"c", "value":"c1"}, "expected": {"version":1}},
            {"item": {"key":"c", "value":"c2"}, "expected": {"version":2}},
            {"item": {"key":"c", "value":"c3"}, "expected": {"version":3}},
        ]

        for t in table_test:
            self.service.add_inmemory_item(t["item"], self.data_store)

            self.assertEqual(self.data_store[t["item"]["key"]][t["expected"]["version"]].key, t["item"]["key"], "El InMemoryItem debe contener el key")
            self.assertEqual(self.data_store[t["item"]["key"]][t["expected"]["version"]].value, t["item"]["value"], "No se guardo el dato requerido")
            self.assertEqual(self.data_store[t["item"]["key"]][t["expected"]["version"]].version, t["expected"]["version"], "La versión no corresponde a la necesaria")

    def test_get_inmemory_item(self):
        """test_get_inmemory_item valida que se regrese el elemento buscado"""
        item = {"key": "test", "value": "a value"}
        self.service.add_inmemory_item(item, self.data_store)

        got = self.service.get_inmemory_item(item["key"], self.data_store)

        self.assertEqual(got.key, item["key"], "El key no corresponde al necesario")
        self.assertEqual(got.value, item["value"], "El value no corresponde al necesario")
        self.assertEqual(got.version, 1, "La version no corresponde a la necesario")

    def test_get_inmemory_item_with_version(self):
        """test_get_inmemory_item_with_version valida que se regrese el elemento buscado proporcionando la versión que se busca"""
        item1 = {"key": "a", "value": "a1"}
        item2 = {"key": "a", "value": "a2"}
        item3 = {"key": "a", "value": "a3"}
        self.service.add_inmemory_item(item1, self.data_store)
        self.service.add_inmemory_item(item2, self.data_store)
        self.service.add_inmemory_item(item3, self.data_store)

        got = self.service.get_inmemory_item(item2["key"], self.data_store, version=2)

        self.assertEqual(got.key, item2["key"], "El key no corresponde al necesario")
        self.assertEqual(got.value, item2["value"], "El value no corresponde al necesario")
        self.assertEqual(got.version, 2, "La version no corresponde a la necesario")

    def test_get_inmemory_item_key_not_exists(self):
        """test_get_inmemory_item_key_not_exists valida se arroje un KeyError cuando no se encuentre el key especificado"""

        with self.assertRaises(KeyError) as exce:
            self.service.get_inmemory_item("b", self.data_store, version=2)

    def test_get_inmemory_item_version_not_exists(self):
        """test_get_inmemory_item_version_not_exists valida regrese la versión mas antigua cuando la versión que se solicita no existe y hay mas datos en el data_store"""
        item1 = {"key": "a", "value": "a1"}
        item2 = {"key": "a", "value": "a2"}
        item3 = {"key": "a", "value": "a3"}
        self.service.add_inmemory_item(item1, self.data_store)
        self.service.add_inmemory_item(item2, self.data_store)
        self.service.add_inmemory_item(item3, self.data_store)

        got = self.service.get_inmemory_item("a", self.data_store, version=9)

        self.assertEqual(got.key, item3["key"], "El key no corresponde al necesario")
        self.assertEqual(got.value, item3["value"], "El value no corresponde al necesario")
        self.assertEqual(got.version, 3, "El key no corresponde al necesario")

    def test_get_inmemory_item_not_requesting_version(self):
        """test_get_inmemory_item_not_requesting_version valida regrese la versión mas antigua cuando la versión se omite al solicitarlo en el servicio"""
        item1 = {"key": "a", "value": "a1"}
        item2 = {"key": "a", "value": "a2"}
        item3 = {"key": "a", "value": "a3"}
        self.service.add_inmemory_item(item1, self.data_store)
        self.service.add_inmemory_item(item2, self.data_store)
        self.service.add_inmemory_item(item3, self.data_store)

        got = self.service.get_inmemory_item("a", self.data_store)

        self.assertEqual(got.key, item3["key"], "El key no corresponde al necesario")
        self.assertEqual(got.value, item3["value"], "El value no corresponde al necesario")
        self.assertEqual(got.version, 3, "El key no corresponde al necesario")


