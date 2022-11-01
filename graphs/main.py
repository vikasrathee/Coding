import heapq
from os import preadv
from xxlimited import new


class GamesGraph:

    def __init__(self, file_name) -> None:
        self.adjList = {}

        try:
            file = open(file_name, 'r')
            games = file.readlines()

            for game in games:
                game_details = game.split(" ")

                if game_details[0] not in self.adjList:
                    self.adjList[game_details[0]] = [(game_details[2], int(game_details[1]) - int(game_details[3]))]        
                else:
                    self.adjList[game_details[0]].append((game_details[2], int(game_details[1]) - int(game_details[3])))
        except:
            print("ERROR: Processing game_data file")
            raise(Exception)

class GraphsAlgo:

    def get_largest_avg_margin_team(G):

        avg_margin = {}

        for team, opponent  in G.adjList.items():
            count = 0
            sum = 0

            for opponent_team in opponent:
                sum += opponent_team[1]
                count += 1

            avg_margin[team] = sum/count

        return max(avg_margin, key=avg_margin.get)

    # def dfs(self, source):
    #     pass


    # def get_dominating_teams_list(G):
    #     in_degree = {k: 0 for k in G.adjList.keys()}

    #     dominates = {}

    #     for vertex in G.adjList.keys():
    #         dominates[vertex] = self.dfs(vertex)

    #     return dominates

    def dijkstra(G, source):
        ## set source distance as 0
        source.setDistance(0)
        unvisitedQueue = [(v.getDistance(), v) for v in G]
        heapq.heapify(unvisitedQueue)

        while len(unvisitedQueue):
            uv = heapq.heappop(unvisitedQueue)
            current = uv[1]
            current.setVisited()
            for next in current.adj:
                if next.visited:
                    continue
                
                newDist = current.getDistance() + current.getWeigfht(next)
                if newDist < next.getDistance():
                    new dist 
                    and set as prev

                else:

        





        


g = GamesGraph("./sports.txt")
print(g.adjList)

print("Team based on Max Average Margin of Victory: ", GraphsAlgo.get_largest_avg_margin_team(g))
#print("Most Dominating Teams: ", g.get_dominating_teams_list())