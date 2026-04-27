# ticketing_system.py

from ticket_service import TicketService
from ticket_data_access import TicketDataAccess

# create data access object
data_access = TicketDataAccess()

# read ticket data from file
lines = data_access.read_file("tickets.txt")

# for now just print lines (we will process later)
print("File data:", lines)


# --- OLD TEST CODE (still works for now) ---

unassigned = ["Ticket1", "Ticket2"]
assigned = {}

service = TicketService(unassigned, assigned)

print("Unassigned tickets:", service.get_unassigned_tickets())

result = service.assign_ticket("Ticket1", "AgentA")

print("Was ticket assigned?", result)
print("Unassigned tickets after assignment:", service.get_unassigned_tickets())

print("Agents:", service.get_agents())

print("Tickets for AgentA:", service.get_tickets_for_agent("AgentA"))

next_ticket = service.assign_next_ticket("AgentA")

print("Next ticket assigned:", next_ticket)
print("Unassigned tickets now:", service.get_unassigned_tickets())