import typer
from typing import List
from pprint import pprint

from console import Console

from schema import Item, Participant, Tab

from utils import error_exit_application


def _new_tab() -> None:
    tab_confirmed = False
    while not tab_confirmed:
        tab_name = typer.prompt('Tab name',
                                confirmation_prompt=False,
                                hide_input=False)

        add_shared_items = typer.confirm('Add shared items?')
        if add_shared_items:
            shared_items = _add_shared_items()
        else:
            shared_items = []

        add_participants = typer.confirm('Add participants?')
        if add_participants:
            participants = _add_participants()
        else:
            participants = []

        tab_confirmed = typer.confirm('Confirm tab?')

    tab = Tab(name=tab_name,
              shared_items=shared_items,
              participants=participants)

    if not shared_items and not participants:
        Console.error(
            message='Both `shared items` and `participants` cannot be empty.')
        error_exit_application()

    if not participants:
        count = _ask_number_of_shared_participants()
        tab.set_number_of_shared_participants(count=int(count))
        Console.log(message='Tab updated.')

    _print_tab_manifest(tab_manifest=tab.manifest)


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


def _add_participants() -> List:
    Console.log(message='Adding participants...')
    participants_confirmed = False
    while not participants_confirmed:
        participants = []
        participant = _add_participant()
        participants.append(participant)
        add_more_participants = typer.confirm('Add more participants?')
        while add_more_participants:
            participant = _add_participant()
            participants.append(participant)
            add_more_participants = typer.confirm('Add more participants?')
        participants_confirmed = typer.confirm('Confirm participants?')
    Console.log(message='Participants added!')
    return participants


def _add_participant() -> Participant:
    participant_confirmed = False
    while not participant_confirmed:
        Console.log(message='Add participant:')
        participant_name = typer.prompt('Participant name',
                                        confirmation_prompt=False,
                                        hide_input=False)
        Console.log(message='Adding participant items...')
        participant_items = []
        item = _add_item()
        participant_items.append(item)
        add_more_participant_items = typer.confirm(
            'Add more participant items?')
        while add_more_participant_items:
            item = _add_item()
            participant_items.append(item)
            add_more_participant_items = typer.confirm(
                'Add more participant items?')
        Console.log(message='Participant items added!')
        participant_confirmed = typer.confirm('Confirm participant?')
    Console.log(message='Participant added!')
    return Participant(name=participant_name, items=participant_items)


def _add_item() -> Item:
    item_confirmed = False
    while not item_confirmed:
        Console.log(message='Add item:')
        item_name = typer.prompt('Item name',
                                 confirmation_prompt=False,
                                 hide_input=False)
        item_price = typer.prompt('Item price',
                                  confirmation_prompt=False,
                                  hide_input=False)
        item_confirmed = typer.confirm('Confirm item?')
    Console.log(message='item added!')
    return Item(name=item_name, price=float(item_price))


def _ask_number_of_shared_participants() -> int:
    count_confirmed = False
    while not count_confirmed:
        Console.log(message='Add number of participants in shared items:')
        count = typer.prompt('Participants count',
                             confirmation_prompt=False,
                             hide_input=False)
        count_confirmed = typer.confirm('Confirm the count?')
    Console.log(message='item added!')
    return count


def _print_tab_manifest(tab_manifest: dict) -> None:
    Console.log(message='Displaying tab manifest:')
    print('-----------------------------------------------------------------')
    pprint(tab_manifest, sort_dicts=False)
    print('-----------------------------------------------------------------')
