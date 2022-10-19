from src.credentials import get_credentials
import src.flow


def main() -> None:
    for credentials in get_credentials():
        src.flow.run(credentials)


if __name__ == "__main__":
    main()
