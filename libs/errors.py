class LogfileError(Exception):
    def __init__(self, Error):
        super().__init__(self)
        self.errorinfo = Error

    def __str__(self):
        return self.errorinfo


class ExtractError(Exception):
    def __init__(self):
        super().__init__(self)
