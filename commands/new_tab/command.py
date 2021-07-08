import typer
from typing import List

from console import Console

from schema import Item


def _new_tab() -> None:
    tab_name = typer.prompt('Tab name',
                            confirmation_prompt=False,
                            hide_input=False)
    add_shared_items = typer.confirm('Add shared items?')
    if add_shared_items:
        shared_items = _add_shared_items()
        print(shared_items)


def _add_shared_items() -> List:
    Console.log(message='Adding shared items...')
    shared_items_confirmed = False
    while not shared_items_confirmed:
        Console.log(message='Add shared items:')
        shared_items = []
        item = _add_item()
        shared_items.append(item)
        add_more_shared_items = typer.confirm('Add more shared items?')
        while add_more_shared_items:
            item = _add_item()
            shared_items.append(item)
            add_more_shared_items = typer.confirm('Add more shared items?')
        shared_items_confirmed = typer.confirm('Confirm shared items?')
    Console.log(message='Shared items added!')
    return shared_items


def _add_item() -> Item:
    item_name = typer.prompt('Item name',
                             confirmation_prompt=False,
                             hide_input=False)
    item_price = typer.prompt('Item price',
                              confirmation_prompt=False,
                              hide_input=False)
    return Item(name=item_name, price=float(item_price))
