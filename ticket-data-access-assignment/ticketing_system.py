from ticket_service import TicketService
from ticket_data_access import TicketDataAccess

data_access = TicketDataAccess()

filename = input("Enter ticket file name: ")


unassigned, assigned = data_access.get_ticket_data(filename)

print("Unassigned from file:", unassigned)
print("Assigned from file:", assigned)

service = TicketService(unassigned, assigned)

print("Agents:", service.get_agents())