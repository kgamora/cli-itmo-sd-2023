class Singleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        key = (cls.__name__, args + tuple(kwargs.values()))
        if key not in cls.instances:
            cls.instances[key] = super().__call__(*args, **kwargs)
        return cls.instances[key]
