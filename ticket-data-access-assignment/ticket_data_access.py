class TicketDataAccess:

    def __init__(self):
        pass
# this class will handle reading ticket data from file
class TicketDataAccess:

    def __init__(self):
        pass
    def read_file(self, filename):

        file = open(filename, "r")

        lines = file.readlines()

        file.close()

        return lines