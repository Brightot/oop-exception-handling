
class TicketService:

    def __init__(self, unassigned_tickets, assigned_tickets):

        # list of unassigned tickets
        self._unassigned_tickets = unassigned_tickets

        # dictionary of assigned tickets
        self._assigned_tickets = assigned_tickets