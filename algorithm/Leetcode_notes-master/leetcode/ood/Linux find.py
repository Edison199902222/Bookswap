from abc import ABC, abstractmethod


class File:
    def __init__(self, name, type, size, is_Directory, file):
        self.name = name
        self.type = type
        self.size = size
        self.is_Directory = is_Directory
        self.child = collections.defaultdict(File)

# 一个filter 只对应一个条件
class Filter(ABC):
    @abstractmethod
    def apply(self, file):
        pass


class Minsize_filter(ABC):
    def __init__(self, size):
        self.min_size = size

    def apply(self, file):
        return file.size > self.min_size

class Type_filter(ABC):
    def __init__(self, type):
        self.target = type

    def apply(self, file):
        return self.target == file.type


class Linux_find:
    def __init__(self, directory, filter):
        self.directory = directory
        self.filter = filter


    def find_(self, directory, filter):
        result = []
        self.findwithfilter(directory, filter, result)
        return result

    def findwithfilter(self, directory, filter, result):
        if not directory.is_Directory:
            return False

        for file in directory.file:
            if file.is_Directory:
                self.findwithfilter(file, filter)
            else:
                flag = True
                for filter_ in filter:
                    if not filter_.apply(file):
                        flag = False
                        break
                if flag:
                    result.append(file)




