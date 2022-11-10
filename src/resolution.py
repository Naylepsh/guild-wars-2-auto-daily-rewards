from dataclasses import dataclass
from typing import Tuple


Coordinates = Tuple[int, int]


@dataclass
class RewardsCoordinates:
    x: int
    top_y: int
    bottom_y: int


@dataclass
class ResolutionCoordinates:
    email: Coordinates
    password: Coordinates
    login: Coordinates
    play: Coordinates
    character: Coordinates
    rewards: RewardsCoordinates


FHD = ResolutionCoordinates(
    email=(520, 540),
    password=(520, 620),
    login=(480, 700),
    play=(1200, 840),
    character=(755, 980),
    rewards=RewardsCoordinates(x=1880, top_y=680, bottom_y=1030),
)
WQHD = ResolutionCoordinates(
    email=(760, 710),
    password=(760, 790),
    login=(800, 880),
    play=(1500, 1000),
    # TODO:
    character=(-1, -1),
    rewards=RewardsCoordinates(x=-1, top_y=-1, bottom_y=-1),
)
