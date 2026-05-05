from model.model import Model

model = Model()
distanza = 5
model.buildGraph(distanza)
print(f"Grafo creato!")
print(f"Il grafo contiene {model.getNumNodes()} nodi e {model.getNumEdges()} archi\n")
# 85581; 399899
