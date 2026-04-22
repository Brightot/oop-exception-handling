
class TicketService:

    def __init__(self, unassigned_tickets, assigned_tickets):

        # list of unassigned tickets
        self._unassigned_tickets = unassigned_tickets

        # dictionary of assigned tickets
        self._assigned_tickets = assigned_tickets
        # return all unassigned tickets
    def get_unassigned_tickets(self):
        return self._unassigned_tickets
    
    def assign_ticket(self, ticket, agent):

        if ticket in self._unassigned_tickets:
            self._unassigned_tickets.remove(ticket)

            # if agent not already in dictionary, create list
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