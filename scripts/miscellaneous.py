from json import load, dumps, decoder
from os import name, system, mkdir
from os.path import exists, isdir
from requests import Response


def clear_screen() -> None:
    if name == "nt":
        system("cls")
    else:
        system("clear")


def write_result(
    uuid: int, response: Response, billing_response: Response, token: str
) -> None:
    if name == "nt":
        with open(f"results\\{str(uuid)}.txt", "w") as text_results:
            text_results.write(
                f"""ID: {response["id"]}
Username: {response["username"]}#{response["discriminator"]}
Email: {str(response["email"])}
Phone: {str(response["phone"])}
Token: {token}
Avatar Decoration: {str(response["avatar_decoration"])}
Bio/Description: {response["bio"]}
Language: {response["locale"]}
Verified: {str(response["verified"])}
NSFW Allowed: {str(response["nsfw_allowed"])}
MFA Enabled: {str(response["mfa_enabled"])}
Has Nitro: {bool(len(billing_response) > 0)}"""
            )
        with open(f"results\\{str(uuid)}.json", "w") as json_results:
            json_results.write(dumps(response, indent=4))
    else:
        with open(f"results/{str(uuid)}.txt", "w") as text_results:
            text_results.write(
                f"""ID: {response["id"]}
Username: {response["username"]}#{response["discriminator"]}
Email: {str(response["email"])}
Phone: {str(response["phone"])}
Token: {token}
Avatar Decoration: {str(response["avatar_decoration"])}
Bio/Description: {response["bio"]}
Language: {response["locale"]}
Verified: {str(response["verified"])}
NSFW Allowed: {str(response["nsfw_allowed"])}
MFA Enabled: {str(response["mfa_enabled"])}
Has Nitro: {bool(len(billing_response) > 0)}"""
            )
        with open(f"results/{str(uuid)}.json", "w") as json_results:
            json_results.write(dumps(response, indent=4))


def get_config() -> dict:
    try:
        with open("config.json", "r") as config_file:
            settings: dict[int or float] = load(config_file)
    except decoder.JSONDecodeError:
        with open("config.json", "w") as config_file:
            config_file.write(dumps({"timeout_in_seconds": 5}, indent=4))
        input("Config file damaged, please restart the program...")
        exit()
    except FileNotFoundError:
        with open("config.json", "w") as config_file:
            config_file.write(dumps({"timeout_in_seconds": 5}, indent=4))
        input("Config file not found, please restart the program...")
        exit()
    return settings


def check_folders() -> None:
    if not exists("results") or not isdir("results"):
        mkdir("results")
