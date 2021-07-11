from dataclasses import dataclass
from datetime import datetime
from typing import List


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
            'Item name': self.name,
            'Item price': self.price,
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
            'Participant name': self.name,
            'Participant items': [item.manifest for item in self.items],
        }


@dataclass
class Tab:
    name: str
    date: datetime
    shared_items: List[Item]
    participants: List[Participant]

    def __post_init__(self) -> None:
        self.name = self.name.capitalize()
        self.date = self.date.strftime("%d/%m/%Y")

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
                'Tab name': self.name,
                'Tab date': self.date,
                'Tab total': self.total,
                'Tab number of participants': self.number_of_participants,
                'Tab participants':
                [participant.manifest for participant in self.participants],
                'Tab participants share': self.all_participants_share,
            }

        elif not self.participants:
            return {
                'Tab name': self.name,
                'Tab date': self.date,
                'Tab total': self.total,
                'Tab shared items':
                [item.manifest for item in self.shared_items],
                'Tab number of shared participants':
                self.number_of_shared_participants,
                'Tab equal share': self.equal_share,
            }

        else:
            return {
                'Tab name': self.name,
                'Tab date': self.date,
                'Tab total': self.total,
                'Tab shared items':
                [item.manifest for item in self.shared_items],
                'Tab shared items total': self.shared_items_total,
                'Tab equal share': self.equal_share,
                'Tab number of participants': self.number_of_participants,
                'Tab participants':
                [participant.manifest for participant in self.participants],
                'Tab participants share': self.all_participants_share,
            }
