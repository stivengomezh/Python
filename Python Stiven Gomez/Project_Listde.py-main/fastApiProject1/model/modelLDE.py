from pydantic import BaseModel

from model.modelLSE import ListSE


class Kid(BaseModel):
    id:int
    name:str
    age:int
    gender:str

class NodeDE:
    def __init__(self, kid:Kid):
        self.__data = kid
        self.__next = None
        self.__prev = None


    def get_data(self):
        return self.__data

    def set_data(self, node):
        self.__next = node

    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next = node

    def get_prev(self):
        return self.__prev

    def set_prev(self, node):
        self.__prev = node

class ListDE:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def get_head(self):
        return self.__head

    def set_head(self, node):
        self.__head = node

    def get_size(self):
        return self.__size

    def set_size(self, size:int):
        self.__size = size


    def listKids(self):
        listKids = ListSE()
        temp = self.__head
        while temp != None:
            listKids.addKidToFinal(temp.get_data())
            temp = temp.get_next()
        return listKids.get_head()

    def addKidToFinal(self, data:Kid):
        newKid = NodeDE(data)
        if self.__head == None:
            self.__head = newKid
        else:
            temp = self.__head
            while temp.get_next() != None:
                temp = temp.get_next()

            temp.set_next(newKid)
            newKid.set_prev(temp)
        self.__size += 1

    def addKidToStart(self, data: Kid):

        newNode = NodeDE(data)
        if self.__head == None:
            self.__head = newNode

        else:

            newNode.set_next(self.__head)
            self.__head.set_prev(newNode)
            self.__head = newNode

        self.__size += 1

    def addKidInPosition(self, data: Kid, position: int):
        newNode = NodeDE(data)
        if position <= self.__size and position > 0:

            if position == 1:
                newNode.set_next(self.__head)
                self.__head = newNode

            else:
                temp = self.__head
                contador = 1
                while contador < position -1:
                    temp = temp.get_next()
                    contador += 1

                newNode.set_next(temp.get_next())
                temp.set_prev(temp)
                temp.set_next(newNode)
            self.__size += 1

        else:
            self.addKidToFinal(data)
            self.__size += 1

    def investKids(self):
        copyList = ListDE()
        if self.__size>=2:

            temp = self.__head
            while temp != None:
                copyList.addKidToStart(temp.get_data())
                temp = temp.get_next()

        self.__head = copyList.get_head()

    def deleteForID(self, ID:int):
        temp = self.__head
        if self.__head.get_data().id == ID:
            self.__head = self.__head.get_next()
            self.__size -= 1

        else:
            while temp != None:
                if temp.get_next.get_data().id == ID:
                    nodeDelete = temp.get_next()
                    temp.set_next(nodeDelete.get_next())
                    nodeDelete.get_next().set_prev(temp)
                    self.__size -= 1
                    return self.__head
                temp = temp.get_next()

        return self.__head


    def deleteForPosition(self, position: int):
        if position <= self.__size and position > 0:
            if position == 1:
                self.__head = self.__head.get_next()
                self.__size -= 1
            else:
                temp = self.__head
                contador = 1
                while contador < position -1:
                    temp = temp.get_next()
                    contador += 1

                nodoDelete = temp.get_next()
                temp.set_next(nodoDelete.get_next())
                nodoDelete.get_next().set_prev(temp)
                self.__size -= 1

        return self.__head

    def interleaveByGender(self):
        if self.__size >2:
            tempWomen = 1
            tempMen = 2

            copyListGender = ListSE()
            temp = self.__head
            while temp != None:
                if temp.get_data().gender == "femenino":
                    copyListGender.addKidInPosition(temp.get_data(), tempWomen)
                    tempWomen += 2
                else:
                    copyListGender.addKidInPosition(temp.get_data(), tempMen)
                    tempMen += 2
                temp = temp.get_next()
            self.__head = copyListGender.get_head()

    def interleaveHeadAndTail(self):
        if self.__size >=2:

            tempTail = self.__head

            while tempTail != None:
                tempTail = tempTail.get_next()

            kidCopy = self.__head.get_data()
            self.__head.set_data(tempTail.get_data())
            tempTail.set_data(kidCopy)

        return self.__head