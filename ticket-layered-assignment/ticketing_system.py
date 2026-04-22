
from ticket_service import TicketService

unassigned = ["Ticket1", "Ticket2"]
assigned = {}

service = TicketService(unassigned, assigned)

# display unassigned tickets first
print("Unassigned tickets:", service.get_unassigned_tickets())

result = service.assign_ticket("Ticket1", "AgentA")

# show result of assignment
print("Was ticket assigned?", result)

# show updated unassigned tickets
print("Unassigned tickets after assignment:", service.get_unassigned_tickets())

# show all agents
print("Agents:", service.get_agents())