class Logger:
    logger = None
    is_debug = True

    def __init__(self) -> None:
        if Logger.logger == None:
            return
        Logger.logger = self

    def log(text: str) -> None:
        if Logger.is_debug:
            print(text)
