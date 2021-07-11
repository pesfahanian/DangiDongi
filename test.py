from pprint import pprint
from datetime import datetime

from schema import Item, Participant, Tab

item_0 = Item(name='kabab', price=30)
item_1 = Item(name='jooje', price=20)
item_2 = Item(name='shishlik', price=100)
item_3 = Item(name='doogh', price=10)
item_4 = Item(name='piaz', price=5)

person_0 = Participant(name='parsa', items=[item_0])
person_1 = Participant(name='milad', items=[item_1, item_2])

tab_0 = Tab(
    name='biroon',
    # shared_items=[item_3, item_4],
    shared_items=[],
    participants=[person_0, person_1])
    # participants=[])

pprint(tab_0.manifest, sort_dicts=False)
# print('--------------------')
# print(tab_0.date)
# print('--------------------')
# print(tab_0.all_participants_share)
# print('--------------------')
# print(tab_0.total)
