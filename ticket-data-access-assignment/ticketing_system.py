# ticketing_system.py

from ticket_service import TicketService
from ticket_data_access import TicketDataAccess

# create data access object
data_access = TicketDataAccess()

# get ticket data from file
unassigned, assigned = data_access.get_ticket_data("tickets.txt")

# display data from file
print("Unassigned from file:", unassigned)
print("Assigned from file:", assigned)

# create service using file data
service = TicketService(unassigned, assigned)

# display agents (simple check)
print("Agents:", service.get_agents())