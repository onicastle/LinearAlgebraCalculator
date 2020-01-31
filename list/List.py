

class List:

    def __init__(self):
        self.main_list = list()

    @property.getter
    def main_list(self):
        return self.main_list()

    def isEmpty(self):
        if len(self.main_list) is 0:
            return True
        else:
            return False

    def add(self, index =None, element=None):
        if element is None:
            raise Exception("No argument to add to List")
        if index is None:
            self.main_list.append(element)
        else:
            self.main_list[index] = element

    def remove(self, element, index = None):
        if index is None:
            try:
                self.main_list.remove(element)
            except ValueError:
                return False
            else:
                return True
        else:
            if index >= self.size or index < 0:
                raise IndexError
            else:
                del self.main_list[index]
                return True

    def removeAll(self, element):
        counter = 0
        while element in self.main_list:
            self.main_list.remove(element)
            counter = counter + 1

        return counter


    def get(self, index):

        if index >= self.size or index < 0:
            raise IndexError
        else:
            return self.main_list[index]

    def set(self,index, element):

        if index < 0 or index >= self.size:
            raise IndexError
        else:
            result = self.main_list[index]
            self.main_list[index] = element
            return result


    def first(self):

        if self.isEmpty():
            return None
        else:
            return self.main_list[0]

    def last(self):

        if self.isEmpty():
            return None
        else:
            self.main_list[self.size - 1]

    def firstIndex(self, element):

        if element not in self.main_list:
            return -1
        else:
            counter = 0
            for target in self.main_list:
                if target is element:
                    return counter
                else:
                    counter = counter + 1

    def getLast(self, element):

        if element not in self.main_list:
            return -1
        else:
            counter = self.size() - 1
            for target in self.main_list.reverse():
                if target is element:
                    return counter
                else:
                    counter = counter - 1

    def clear(self):
        self.main_list.clear()


