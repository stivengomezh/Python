from model import modelLSE


class ListSEService:
    def __init__(self):
        self.__kids = modelLSE.ListSE()

    def get_kids(self):
        return self.__kids
