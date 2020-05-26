from unittest import TestCase
from models.item import ItemModel


class ItemTest(TestCase):
    def test_create_item(self):
        i = ItemModel('Test', '20.00')
        self.assertEqual('Test', i.name)
        self.assertEqual('20.00', i.price)

    def test_item_json(self):
        i = ItemModel('Test', '20.00')
        expected = {'name': 'Test', 'price': '20.00'}
        self.assertDictEqual(expected, i.json())
