from dataclasses import dataclass
from datetime import datetime
from typing import List
import uuid


@dataclass
class Item:
    name: str
    price: float

    def __post_init__(self) -> None:
        self.name = self.name.capitalize()
        self.price = float(round(self.price, 3))

    @property
    def manifest(self) -> dict:
        return {
            'item_name': self.name,
            'item_price': self.price,
        }


@dataclass
class Participant:
    name: str
    items: List[Item]

    def __post_init__(self) -> None:
        self.name = self.name.capitalize()

    @property
    def total(self) -> float:
        return sum([item.price for item in self.items])

    @property
    def manifest(self) -> dict:
        return {
            'participant_name': self.name,
            'participant_items': [item.manifest for item in self.items],
        }


@dataclass
class Tab:
    name: str
    shared_items: List[Item]
    participants: List[Participant]

    def __post_init__(self) -> None:
        self.ID = str(uuid.uuid1())
        self.name = self.name.capitalize()
        self.date = datetime.today().strftime("%d/%m/%Y")

    def participant_share(self, name: str) -> float:
        participant = [
            participant for participant in self.participants
            if participant.name == name
        ][0]
        return participant.total + self.equal_share

    def set_number_of_shared_participants(self, count: int) -> None:
        self.number_of_shared_participants: int = count

    @property
    def all_participants_share(self) -> dict:
        all_shares = {}
        for participant in self.participants:
            all_shares[participant.name] = self.participant_share(
                name=participant.name)
        return all_shares

    @property
    def number_of_participants(self) -> int:
        return len(self.participants)

    @property
    def participants_total(self) -> float:
        return sum([participant.total for participant in self.participants])

    @property
    def shared_items_total(self) -> float:
        return sum([item.price for item in self.shared_items])

    @property
    def equal_share(self) -> float:
        if not self.participants:
            return self.shared_items_total / self.number_of_shared_participants
        else:
            return self.shared_items_total / self.number_of_participants

    @property
    def total(self) -> float:
        return self.shared_items_total + self.participants_total

    @property
    def manifest(self) -> dict:
        if not self.shared_items:
            return {
                'tab_ID': self.ID,
                'tab_name': self.name,
                'tab_date': self.date,
                'tab_total': self.total,
                'tab_number_of_participants': self.number_of_participants,
                'tab_participants':
                [participant.manifest for participant in self.participants],
                'tab_participants_share': self.all_participants_share,
            }

        elif not self.participants:
            return {
                'tab_ID': self.ID,
                'tab_name': self.name,
                'tab_date': self.date,
                'tab_total': self.total,
                'tab_shared_items':
                [item.manifest for item in self.shared_items],
                'tab_number_of_shared_participants':
                self.number_of_shared_participants,
                'tab_equal_share': self.equal_share,
            }

        else:
            return {
                'tab_ID': self.ID,
                'tab_name': self.name,
                'tab_date': self.date,
                'tab_total': self.total,
                'tab_shared_items':
                [item.manifest for item in self.shared_items],
                'tab_shared_items_total': self.shared_items_total,
                'tab_equal_share': self.equal_share,
                'tab_number_of_participants': self.number_of_participants,
                'tab_participants':
                [participant.manifest for participant in self.participants],
                'tab_participants_share': self.all_participants_share,
            }
