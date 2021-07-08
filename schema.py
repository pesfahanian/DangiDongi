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


@dataclass
class Participant:
    name: str
    items: List[Item]

    def __post_init__(self) -> None:
        self.name = self.name.capitalize()

    @property
    def total(self) -> float:
        return sum([item.price for item in self.items])


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
        return self.shared_items_total / self.number_of_participants

    @property
    def total(self) -> float:
        return self.shared_items_total + self.participants_total
