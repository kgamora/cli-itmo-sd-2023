import argparse


class CustomArgumentParser(argparse.ArgumentParser):
    class ArgumentException(Exception):
        pass

    def error(self, message):
        if message:
            raise CustomArgumentParser.ArgumentException(message)
        super(CustomArgumentParser, self).error(message)
