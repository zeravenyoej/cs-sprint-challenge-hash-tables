#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    route = []      
    flight_cache = {}

    for ticket in tickets:                                 # go through the array 
        flight_cache[ticket.source] = ticket.destination   # build the flight_cache 

        if ticket.source == "NONE":                        # find first ticket
            route.append(ticket.destination)               # add the first destination to the route array

    while route[len(route)-1] != "NONE":                  # make a loop to go through the cache
        route.append(flight_cache[route[len(route)-1]])

    return route
