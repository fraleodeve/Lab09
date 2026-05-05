import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza_aeroporti(self, e):
        txtIdOggetto = self._view._txt_distanza.value

        if txtIdOggetto == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Attenzione! Inserire un valore nel campo id.", color="red"))
            self._view.update_page()
            return

        try:  # verifico che l'utente inserisca un valore numerico
            idOggetto = int(txtIdOggetto)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Attenzione! Inserire un valore numerico nel campo id.", color="red"))
            self._view.update_page()
            return

        self._model.buildGraph(idOggetto)
        edges = self._model.getEdgesPesati()

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato!"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo è costituito da {self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo è costituito da {self._model.getNumEdges()} archi."))
        self._view.txt_result.controls.append(ft.Text(f"\nI collegamenti sono:"))
        for el in edges:
            self._view.txt_result.controls.append(
                # ft.Text(f"{el[2]}: {el[0]} -> {el[1]}"))
                ft.Text(f"{el[0]} -> {el[1]}: {el[2]}"))

        self._view.update_page()