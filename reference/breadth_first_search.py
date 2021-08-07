'''
graphs represented by dictionaries
searches graph data structures and finds if a path is possible
time complexity is O(V+E)
V - number of vertices
E - number of edges (links between vertices)

searches for person with last letter as m
'''

from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        print(search_queue)
        person = search_queue.popleft()
        if not person in searched:
            if person[-1] == "m":
                print(person+ " is a mango seller")
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")
