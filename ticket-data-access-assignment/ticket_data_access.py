class TicketDataAccess:

    def __init__(self):
        pass

    # this method reads file and returns lines
    def read_file(self, filename):

        file = open(filename, "r")
        lines = file.readlines()
        file.close()

        return lines

    # this method processes the file into data
    def get_ticket_data(self, filename):

        lines = self.read_file(filename)

        unassigned = []
        assigned = {}

        for line in lines:

            parts = line.strip().split(",")

            if len(parts) < 2:
                continue

            ticket = parts[0]
            agent = parts[1]

            if agent == "":
                unassigned.append(ticket)

            else:
                if agent not in assigned:
                    assigned[agent] = []

                assigned[agent].append(ticket)

        return unassigned, assigned