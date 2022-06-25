class Singleton(type):

    _instances = {}

    def __new__(self, class_name, *args, **kwargs):
        if class_name not in self._instances:
            self._instances[class_name] = [
                super(Singleton, self).__new__(self, class_name, *args, **kwargs),
                None
            ]
        return self._instances[class_name][0]

    def __call__(self, *args, **kwargs):
        if self._instances[self.__name__][1] != None:
            return self._instances[self.__name__][1]
        else:
            self._instances[self.__name__][1] = super(Singleton, self).__call__(*args, **kwargs)
        return self._instances[self.__name__][1]
