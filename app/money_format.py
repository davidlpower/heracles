import locale


class MoneyFormat():

    def __init__(self, local_format):
        locale.setlocale(locale.LC_ALL, local_format)

    def format(self, amount):

        # guard clause
        if type(amount) is not float:
            raise TypeError('argument: "amount" must be a float')

        return locale.currency(amount)
