class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        airports=defaultdict(list)

        for origin,destination in tickets:
            airports[origin].append(destination)

        for key in airports:
            airports[key].sort(reverse=True)
        
        itinerary=[] 

        def dfs(origin):
            while airports[origin]:
                city=airports[origin].pop()
                dfs(city)
            itinerary.append(origin) 

        dfs("JFK")

        itinerary.reverse()
        
        return itinerary

        


        

        