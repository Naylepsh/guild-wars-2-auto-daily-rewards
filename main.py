from src.credentials import get_credentials
import src.flow
from src.cli import Resolution, parser
from src.resolution import FHD, WQHD


def main() -> None:
    args = parser.parse_args()
    resolution: Resolution = args.resolution

    if resolution == Resolution.FHD:
        coordinates = FHD
    elif resolution == Resolution.WQHD:
        coordinates = WQHD
    else:
        coordinates = None

    if coordinates:
        for credentials in get_credentials():
            src.flow.run(credentials, coordinates)


if __name__ == "__main__":
    main()
