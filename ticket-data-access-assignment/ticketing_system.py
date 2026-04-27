
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

# get tickets for AgentA
print("Tickets for AgentA:", service.get_tickets_for_agent("AgentA"))

# assign next available ticket
next_ticket = service.assign_next_ticket("AgentA")

print("Next ticket assigned:", next_ticket)
print("Unassigned tickets now:", service.get_unassigned_tickets())