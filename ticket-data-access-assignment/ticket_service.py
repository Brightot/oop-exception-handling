class TicketService:

    def __init__(self, unassigned_tickets, assigned_tickets):

        self._unassigned_tickets = unassigned_tickets
        self._assigned_tickets = assigned_tickets

    def get_unassigned_tickets(self):
        return self._unassigned_tickets

    def assign_ticket(self, ticket, agent):

        if ticket in self._unassigned_tickets:
            self._unassigned_tickets.remove(ticket)

            if agent not in self._assigned_tickets:
                self._assigned_tickets[agent] = []

            self._assigned_tickets[agent].append(ticket)
            return True

        return False

    def get_agents(self):
        return list(self._assigned_tickets.keys())

    def get_tickets_for_agent(self, agent):

        if agent in self._assigned_tickets:
            return self._assigned_tickets[agent]

        return []

    def assign_next_ticket(self, agent):

        if len(self._unassigned_tickets) > 0:

            ticket = self._unassigned_tickets.pop(0)

            if agent not in self._assigned_tickets:
                self._assigned_tickets[agent] = []

            self._assigned_tickets[agent].append(ticket)

            return ticket

        return None