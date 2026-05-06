import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()  # rispetta i paletti della traccia
        self._idMap = {}
        self._flights = []



    def buildGraph(self, distanza):
        self._flights = DAO.getAllFlights(distanza)
        for el in self._flights:
            if el.ORIGIN_AIRPORT_ID not in self._idMap.keys():
                for aeroporto in DAO.getAllAirports():
                    if aeroporto.ID == el.ORIGIN_AIRPORT_ID:
                        self._idMap[aeroporto.ID] = aeroporto
                        self._graph.add_node(aeroporto)

        for el in self._flights:
            if el.DESTINATION_AIRPORT_ID not in self._idMap.keys():
                for aeroporto in DAO.getAllAirports():
                    if aeroporto.ID == el.DESTINATION_AIRPORT_ID:
                        self._idMap[aeroporto.ID] = aeroporto
                        self._graph.add_node(aeroporto)

        print(f"I nodi sono: {len(self._idMap)}")
        self.addEdges(distanza)

    def addEdges(self, distanza):
        self._graph.clear_edges()
        print(f"I voli con distanza {distanza} sono: {len(self._flights)}")
        for connessione in self._flights:
            u = self._idMap[connessione.ORIGIN_AIRPORT_ID]
            v = self._idMap[connessione.DESTINATION_AIRPORT_ID]
            self._graph.add_edge(u, v, weight=connessione.DISTANCE)

        for conn in self._flights:
            u = self._idMap[conn.DESTINATION_AIRPORT_ID]
            v = self._idMap[conn.ORIGIN_AIRPORT_ID]
            self._graph.add_edge(u, v, weight=conn.DISTANCE)

    def getNumNodes(self):
        return len(self._graph.nodes) # equivalente a self._nodes

    def getNumEdges(self):
        return len(self._graph.edges)

    def getEdgesPesati(self):
        risultato = []
        for u, v, data in self._graph.edges(data=True):
            peso = data.get('weight')
            risultato.append((u, v, peso))

        risultato.sort(key=lambda x: x[1])
        risultato.sort(key=lambda x: x[0])
        # risultato.sort(key=lambda x: x[2], reverse=True)
        print(f"Gli archi sono: {len(risultato)}\n")
        return risultato



