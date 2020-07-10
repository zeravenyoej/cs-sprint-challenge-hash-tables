#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

def reconstruct_trip(tickets, length):
    # initialize an array that will show all cities
    route = []
    flight_cache = {}
    current_ticket = {}   # initialize a cache to store the source: destination
    temp_ticket = {}

    for ticket in tickets:                  # go through the array 
        flight_cache[ticket.source] = ticket.destination   # build the flight_cache 

        if ticket.source == "NONE":         # find first ticket
            route.append(ticket.destination)   # add the first destination to the route array
            current_ticket[ticket.source] = ticket.destination   # update current ticket dictionary

    while route[len(route)-1] != "NONE":                # make a loop to go through the cache
        for source, destination in flight_cache.items():
            
            if source == current_ticket.values():         # find the ticket whose source matches the current ticket's destination
                route.append(destination)    # once found, append the destination city
                
                temp_ticket = {source: destination}
                current_ticket.update(temp_ticket)


                # current_ticket[ticket.source] = destination  # set a current_ticket pointer to ticket whose source matches the first's destination

    return route

print(reconstruct_trip(tickets, 3))


    # print("route: ", route)
    # print("current ticket: ", current_ticket)
    # print("last in route: ", route[len(route)-1])
