from json import load, JSONDecodeError, dump
from os import name, system, mkdir
from os.path import exists, isdir


def clear_screen() -> None:
    if name == "nt":
        system("cls")
    else:
        system("clear")


def write_result(uuid: int, token: str) -> None:
    if name == "nt":
        with open(f"results\\{str(uuid)}.txt", "w") as result_file:
            result_file.write(token)
    else:
        with open(f"results/{str(uuid)}.txt", "w") as result_file:
            result_file.write(token)


def get_config() -> dict:
    try:
        with open("config.json", "r") as config_file:
            settings: dict[int or float] = load(config_file)
    except FileNotFoundError or JSONDecodeError:
        with open("config.json", "w") as config_file:
            dump({"timeout_in_seconds": 5}, config_file)
        input("Config file damaged or not found, please restart the program...")
        exit()
    return settings


def check_folders() -> None:
    if not exists("results") or not isdir("results"):
        mkdir("results")
