import argparse
from enum import Enum
from typing import List


class Resolution(Enum):
    FHD = "FHD"
    WQHD = "WQHD"

    @staticmethod
    def values() -> List[str]:
        return [res.value for res in Resolution._member_map_.values()]


class EnumAction(argparse.Action):
    """
    Argparse action for handling Enums
    Source: https://stackoverflow.com/questions/43968006/support-for-enum-arguments-in-argparse
    """

    def __init__(self, **kwargs):
        # Pop off the type value
        enum_type = kwargs.pop("type", None)

        # Ensure an Enum subclass is provided
        if enum_type is None:
            raise ValueError("type must be assigned an Enum when using EnumAction")
        if not issubclass(enum_type, Enum):
            raise TypeError("type must be an Enum when using EnumAction")

        # Generate choices from the Enum
        kwargs.setdefault("choices", tuple(e.value for e in enum_type))

        super(EnumAction, self).__init__(**kwargs)

        self._enum = enum_type

    def __call__(self, parser, namespace, values, option_string=None):
        # Convert value back into an Enum
        value = self._enum(values)
        setattr(namespace, self.dest, value)


parser = argparse.ArgumentParser(description="Guild Wars 2 Auto Reward Acquirement")

parser.add_argument(
    "-r",
    "--resolution",
    dest="resolution",
    type=Resolution,
    help=f"One of the following: {','.join(Resolution.values())}",
)


args = parser.parse_args()
