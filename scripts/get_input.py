from base64 import b64encode


def get_target_BASE64(clear_screen_function) -> list[str, int]:
    while True:
        clear_screen_function()
        try:
            START_UUID: int = int(input("Targets user ID: "))
        except ValueError:
            continue
        if len(str(START_UUID)) != 18:
            continue
        return [
            (
                b64encode(str(START_UUID).encode("ascii"))
                .decode("ascii")
                .replace("=", "", -1)
            ),
            START_UUID,
        ]
