from model import modelLDE, modelLSE


class ListDEService:
    def __init__(self):
        self.__kids = modelLDE.ListDE()
        self.__listKids = modelLSE.ListSE()

    def get_kids(self):
        return self.__kids

