# ticketing_system.py

from ticket_service import TicketService

# example data
unassigned = ["Ticket1", "Ticket2"]
assigned = {}

# create service object
service = TicketService(unassigned, assigned)

# test
print(service.get_unassigned_tickets())