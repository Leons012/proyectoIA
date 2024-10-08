from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import ttkbootstrap as tb
import networkx as nx
import matplotlib.pyplot as plt
from bfs_method import searchBFS
from dfs_method import searchDFS
from ucs_method import searchUCS
from dsf_method import searchDSF
from UCSInf_method import searchUCSInf
from Dijkstra_method import searchDijkstra
from Hill_Climbing_method import searchHillClimbing

SEARCHES = ("amplitud", "profundidad", "coste uniforme", "profundidad iterativa", "coste uniforme informado", "Dijkstra", "Hill Climbing")

CONEXIONES = {
    'Rincón del bosque': {'Villa Martha': 2500},
    'Villa Martha': {'Santa Ana': 1400, 'Pacande': 900, 'Rincón del bosque':2500},
    'Santa Ana': {'Pacande': 700, 'Villa Martha': 1400, 'Jardin de los Abuelos': 1000},
    'Pacande': {'Reservas de Cantabria': 200, 'Floresta': 400, 'Santa Ana':700, 'Villa Martha':900},
    'Reservas de Cantabria': {'La cabaña': 120, 'Floresta': 200, 'Pacande':200},
    'La cabaña': {'Diana Milady': 220, 'Rosales de Tailandia': 270, 'San Luis Gonzaga': 240, 'Reservas de Cantabria': 120},
    'Diana Milady': {'Rosales de Tailandia': 350, 'San Luis Gonzaga': 300, 'La cabaña': 220},
    'Rosales de Tailandia': {'San Luis Gonzaga': 150, 'Diana Milady': 350, 'La cabaña': 270},
    'San Luis Gonzaga': {'Cantabria': 96, 'Rosales de Tailandia': 150, 'Diana Milady': 300, 'La cabaña': 240},
    'Cantabria': {'Floresta': 500, 'Praderas del norte': 150, 'San Pablo': 450, 'San Luis Gonzaga': 96},
    'Praderas del norte': {'Tierra firme': 85, 'Mirador de Cantabria': 200, 'Cantabria':150},
    'Tierra firme': {'Praderas del norte': 85},
    'Mirador de Cantabria': {'Bella Suiza': 230, 'Praderas del norte': 200},
    'Bella Suiza': {'San Pablo': 400, 'Mirador de Cantabria':230},
    'Floresta': {'Villa Cindy': 210, 'Pacande': 400, 'Reservas de Cantabria': 200, 'Cantabria': 500},
    'Villa Cindy': {'Villa Rocio': 96, 'Floresta': 210},
    'Villa Rocio': {'San Pablo': 400, 'Villa Cindy': 96, 'Jardin de los Abuelos': 1200, 'Villa Marin': 500},
    'San Pablo': {'Cantabria': 450, 'La Candelaria': 550, 'Jardin de los Abuelos': 1400, 'Villa Rocio': 400, 'Bella Suiza':400},
    'La Candelaria': {'San Pablo':550, 'Jardin de los Abuelos': 1300, 'Villa Marin': 550},
    'Jardin de los Abuelos': {'La Candelaria': 1400, 'San Pablo': 1400, 'Santa Ana': 1000, 'Villa Marin': 800, 'Villa Rocio': 1200},
    'Villa Marin': {'Jardin de los Abuelos': 800, 'La Candelaria': 550, 'Villa Rocio': 500, 'Montecarlo 2': 300},
    'Montecarlo 2': {'Villa Marin':300, 'Fuentes del salado': 250, 'San Tropel': 450, 'Nueva Bilbao': 700},
    'Fuentes del salado': {'Montecarlo 2': 250},
    'San Tropel': {'San Sebastian': 110, 'Montecarlo 2': 450},
    'San Sebastian': {'Villa zulay': 400, 'San Tropel': 110, 'Portales del norte': 350},
    'Villa zulay': {'San Sebastian': 400, 'Fuente real': 300, 'Portales del norte': 700},
    'Fuente real': {'Villa zulay': 300, 'Nueva Bilbao': 190},
    'Nueva Bilbao': {'Montecarlo 2': 700, 'Fuente real': 190},
    'Portales del norte': {'San Sebastian': 350, 'Villa zulay': 350, 'La ceiba norte': 400, 'Montecarlo': 500},
    'Montecarlo': {'Portales del norte': 500, 'Palma del Rio': 900, 'La victoria': 400},
    'Palma del Rio': {'Montecarlo': 900},
    'La victoria': {'Montecarlo': 400, 'El salado': 100, 'Ambikaima': 180},
    'Ambikaima': {'La victoria': 180},
    'El salado': {'La victoria': 100, 'Los lagos': 250, 'Villa Clara': 750},
    'Los lagos': {'El salado': 250,'San Isidro Labrador': 140},
    'San Isidro Labrador': {'Los lagos': 140, 'La ceiba norte': 500},
    'La ceiba norte': {'San Isidro Labrador': 500, 'Portales del norte':400},
    'Villa Clara': {'El salado':750, 'Comfatolima': 450},
    'Comfatolima': {'Villa Clara': 450, 'Territorio de paz': 150, 'Villa Camila': 700},
    'Villa Camila': {'Comfatolima': 700, 'Chico': 280},
    'Chico': {'Villa Camila': 280,'Territorio de paz':550, 'Modelia 1': 400, 'Modelia 2': 550, 'Villa Salome': 260},
    'Territorio de paz': {'Comfatolima': 150, 'Chico': 550},
    'Modelia 1': {'Chico': 400, 'Modelia 2': 450, 'Villa Salome': 350, 'Protecho': 450, 'La Ceibita': 700, 'Santa Catalina': 600},
    'Modelia 2': {'Chico':550, 'Modelia 1': 450, 'Villa Salome':550},
    'Villa Salome': {'Chico': 260, 'Modelia 2': 550,'El Dorado': 59, 'Timaka': 280, 'Modelia 1': 350},
    'El Dorado': {'Villa Salome': 59, 'Timaka': 300, 'Lady di': 170, 'El Recreo': 190},
    'Timaka': {'Villa Salome': 280, 'El Dorado': 300},
    'Lady di': {'El Dorado': 170, 'El Recreo': 150},
    'El Recreo': {'El Dorado': 190, 'Lady di': 150, 'Protecho': 210, 'Alamos': 270},
    'Alamos': {'El Recreo': 270, 'Protecho': 260},
    'Protecho': {'Modelia 1': 450, 'El Recreo': 210, 'Alamos': 260, 'Santa Catalina': 150},
    'Santa Catalina': {'Protecho': 150, 'La Ceibita': 450, 'Modelia 1': 600},
    'La Ceibita': {'Santa Catalina': 450, 'El Pais': 500, 'Modelia 1': 700},
    'El Pais': {'La Ceibita': 500}
}

TUPLA_CONEXIONES = tuple(CONEXIONES)

TUPLA_COORD = (
    (4.44788, -75.17431),  # Rincón del bosque
    (4.44590, -75.1727),   # Villa Martha
    (4.44364, -75.16488),  # Santa Ana
    (4.44698, -75.16572),  # Pacande
    (4.44775, -75.16489),  # Reservas de Cantabria
    (4.44863, -75.16461),  # La cabaña
    (4.44939, -75.1461),   # Diana Milady
    (4.44966, -75.16425),  # Rosales de Tailandia
    (4.44932, -75.16349),  # San Luis Gonzaga
    (4.45128, -75.16159),  # Cantabria
    (4.45106, -75.16258),  # Praderas del norte
    (4.45400, -75.16758),  # Tierra firme
    (4.45132, -75.16160),  # Mirador de Cantabria
    (4.45154, -75.14440),  # Bella Suiza
    (4.44711, -75.16204),  # Floresta
    (4.44721, -75.16094),  # Villa Cindy
    (4.44752, -75.16031),  # Villa Rocio
    (4.44917, -75.16008),  # San Pablo
    (4.44906, -75.15904),  # La Candelaria
    (4.44626, -75.15928),  # Jardin de los Abuelos
    (4.44849, -75.15698),  # Villa Marin
    (4.44945, -75.15587),  # Montecarlo 2
    (4.45154, -75.15602),  # Fuentes del salado
    (4.44916, -75.15321),  # San Tropel
    (4.44906, -75.15236),  # San Sebastian
    (4.44686, -75.15197),  # Villa zulay
    (4.44605, -75.15352),  # Fuente real
    (4.44625, -75.15473),  # Nueva Bilbao
    (4.44789, -75.15040),  # Portales del norte
    (4.44992, -75.14796),  # Montecarlo
    (4.45300, -75.14823),  # Palma del Rio
    (4.45061, -75.14506),  # La victoria
    (4.45162, -75.14439),  # Ambikaima
    (4.45058, -75.14496),  # El salado
    (4.44781, -75.14474),  # Los lagos
    (4.44757, -75.14545),  # San Isidro Labrador
    (4.44713, -75.14788),  # La ceiba norte
    (4.45090, -75.14063),  # Villa Clara
    (4.44974, -75.13988),  # Comfatolima
    (4.45511, -75.13500),  # Villa Camila
    (4.45237, -75.13544),  # Chico
    (4.45072, -75.13765),  # Territorio de paz
    (4.45137, -75.13357),  # Modelia 1
    (4.44950, -75.13653),  # Modelia 2
    (4.45408, -75.13465),  # Villa Salome
    (4.45465, -75.13454),  # El Dorado
    (4.45513, -75.13500),  # Timaka
    (4.45598, -75.1336),   # Lady di
    (4.45450, -75.13307),  # El Recreo
    (4.45571, -75.13232),  # Alamos
    (4.45397, -75.13140),  # Protecho
    (4.45421, -75.13039),  # Santa Catalina
    (4.45304, -75.12748),  # La Ceibita
    (4.45458, -75.12482)   # El Pais
)

DICT_COORD = dict_pos = dict(zip(CONEXIONES.keys(), TUPLA_COORD))

TUPLA_POS = ((0.1, 0.8),
             (0.15, 0.7),
             (0.23, 0.6),
             (0.23, 0.75),
             (0.27, 0.95),
             (0.38, 1),
             (0.47, 0.93),
             (0.49, 0.8),
             (0.58, 0.98),
             (0.6, 0.85),
             (0.7, 0.9),
             (0.75, 1),
             (0.8, 0.75),
             (0.7, 0.7),
             (0.49, 0.7),
             (0.38, 0.65),
             (0.53, 0.64),
             (0.6, 0.75),
             (0.76, 0.46),
             (0.63, 0.55),
             (0.57, 0.42),
             (0.57, 0.32),
             (0.68, 0.37),
             (0.5, 0.27),
             (0.35, 0.32),
             (0.27, 0.45),
             (0.4, 0.52),
             (0.47, 0.45),
             (0.2, 0.35),
             (0.1, 0.25),
             (0.1, 0.4),
             (0.17, 0.2),
             (0.1, 0.1),
             (0.2, 0.1),
             (0.27, 0.17),
             (0.37, 0.2),
             (0.25, 0.27),
             (0.3, 0.1),
             (0.4, 0.1),
             (0.51, 0.1),
             (0.57, 0.15),
             (0.47, 0.22),
             (0.72, 0.2),
             (0.67, 0.1),
             (0.67, 0.3),
             (0.8, 0.3),
             (0.9, 0.45),
             (0.75, 0.1),
             (0.92, 0.35),
             (1, 0.25),
             (0.9, 0.23),
             (0.85, 0.1),
             (0.95, 0.14),
             (1, 0.05)
)

class App(tb.Window):
    def __init__(self, theme, color):
        super().__init__(themename=theme)

        global WIDTHSCREEN
        global HEIGHTSCREEN

        WIDTHSCREEN = self.winfo_screenwidth()
        HEIGHTSCREEN = self.winfo_screenheight()

        self.defineColors(theme)
        self.attributes('-fullscreen', True)
        self.attributes('-transparentcolor', self.bg)

        self.presentation = FramePresentation(self, color, (WIDTHSCREEN*0.3125), (HEIGHTSCREEN*0.37))

        self.after(2000,self.replace)

    def replace(self):
        self.presentation.destroy()

        self.grafo = GraphicFrame(self)
        self.grafo.pack(fill="both", expand=True)

        self.resultados = Results(self, 0.96, 0.5)

        self.panel_menu = MenuPanel(self, 0.58, 0.98)

        self.attributes('-transparentcolor', "")
    

    def defineColors(self, theme):
        lightmode = ("cosmo", "flatly", "journal", "litera", "minty", "lumen", "sandstone", "yeti", "pulse", "united", "cerculean")
        if (theme in lightmode):
            self.bg= "#ffffff"
        elif (theme == "simplex"):
            self.bg = "#fcfcfc"
        elif (theme == "morph"):
            self.bg = "#D9E3F1"
        elif (theme == "light"):
            self.bg= "#7e8081"
        elif (theme == "solar"):
            self.bg = "#002B36"
        elif (theme == "darkly"):
            self.bg = "#222222"
        elif (theme == "superhero"):
            self.bg = "#2b3e50"
        elif (theme == "cyborg"):
            self.bg = "#060606"
        elif (theme== "vapor"):
            self.bg = "#190831"
        
class FramePresentation(tb.Frame):
    def __init__(self, master, color, width, height):
        super().__init__(master=master, bootstyle=color, width=width, height=height)
        xposition = (WIDTHSCREEN-width)/2
        yposition = (HEIGHTSCREEN-height)/2
        self.place(x=xposition, y=yposition)

        tb.Label(self, text="Presentado por:", bootstyle=f"{color}inverse", font=("Segoe UI Light", int(HEIGHTSCREEN*0.019))).place(relx=0.32, rely=0.01)
        tb.Label(self, text="David Alejandro Camacho León", bootstyle=f"{color}inverse", font=("Segoe UI Light", int(HEIGHTSCREEN*0.013))).place(relx=0.01, rely=0.25)
        tb.Label(self, text="Kevin Guerrero Penagos", bootstyle=f"{color}inverse", font=("Segoe UI Light", int(HEIGHTSCREEN*0.013))).place(relx=0.01, rely=0.45)
        tb.Label(self, text="Andres Felipe Vasquez", bootstyle=f"{color}inverse", font=("Segoe UI Light", int(HEIGHTSCREEN*0.013))).place(relx=0.01, rely=0.65)

class GraphFrame(tb.Frame):
    def __init__(self, master, resultados):
        super().__init__(master=master, bootstyle="light")

        self.width, self.height = WIDTHSCREEN * 0.08, HEIGHTSCREEN / 110

        # Crear el grafo
        self.G = nx.Graph()

        self.resultados = resultados
        lista_barrios = []
        self.dict_resultados = dict.fromkeys(self.resultados)
        self.lista_pos = []
        self.highlighted_edges = []
        self.path = []

        for i in self.resultados:
            self.dict_resultados[i] = CONEXIONES[i]
            self.lista_pos.append(TUPLA_POS[TUPLA_CONEXIONES.index(i)])
            for j in self.dict_resultados[i]:
                if j in self.resultados and (j, i) not in lista_barrios:
                    lista_barrios.append((i, j))
        
        self.G.add_edges_from(lista_barrios)

        # Crear el diccionario de posiciones solo para los nodos en self.resultados
        self.pos = dict(zip(self.resultados, self.lista_pos))

        # Crear la figura y el eje
        self.fig, self.ax = plt.subplots(figsize=(WIDTHSCREEN * 0.007682, HEIGHTSCREEN * 0.00737))
        self.fig.set_size_inches(self.width, self.height)

        # Asegurarse de que los nodos del grafo tengan posiciones definidas
        nx.draw(self.G, self.pos, with_labels=False, ax=self.ax, node_size=int((HEIGHTSCREEN * 0.64815)), node_color='#9ce1ff', width=2, edge_color="grey")

        # Agregar etiquetas solo si están presentes en el grafo
        labels = {node: node for node in self.G.nodes() if node in self.pos}
        nx.draw_networkx_labels(self.G, self.pos, labels=labels, ax=self.ax, font_size=int(WIDTHSCREEN * 0.0052084), font_family='Segoe UI', font_color="red", font_weight='bold')

        self.ax.set_title('Búsqueda de rutas - Comuna 7', fontsize=int(HEIGHTSCREEN*0.017), fontweight='bold')

        # Crear el canvas para mostrar la figura
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack()

    def highlight_path(self, path, color='#fffb00'):

        self.clear_highlight()
        # Resaltar nodos de la ruta
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=path, ax=self.ax, node_color=color, node_size=int((HEIGHTSCREEN * 0.64815)))

        # Crear las aristas de la ruta en forma de lista de tuplas
        edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]

        # Resaltar las aristas de la ruta
        nx.draw_networkx_edges(self.G, self.pos, edgelist=edges, ax=self.ax, edge_color=color, width=2)

        self.highlighted_edges = edges
        self.path = path
        

        # Actualizar el canvas para reflejar los cambios
        self.canvas.draw()

    def clear_highlight(self):
        """Limpiar cualquier ruta resaltada."""
        if self.highlighted_edges:

            nx.draw_networkx_nodes(self.G, self.pos, nodelist=self.path, ax=self.ax, node_color="#9ce1ff", node_size=int((HEIGHTSCREEN * 0.64815)))
            # Redibujar las aristas con su estilo original
            nx.draw_networkx_edges(self.G, self.pos, edgelist=self.highlighted_edges, ax=self.ax, edge_color='grey', width=2)
            self.highlighted_edges = []  # Vaciar la lista de aristas resaltadas
            self.path = []
            self.canvas.draw()

class GraphicFrame(tb.Frame):
    def __init__(self, master):
        super().__init__(master=master, bootstyle="light")

        # Crear el frame que contendrá el gráfico
        self.graphic = tb.Frame(self, bootstyle="secondary")
        self.graphic.pack(padx=int(WIDTHSCREEN*0.02), pady=int(HEIGHTSCREEN*0.04), fill="both", expand=True)

        self.graph_frame = GraphFrame(self.graphic, tuple(CONEXIONES))
        self.graph_frame.pack(fill="both", expand=True)

    def replaceGraph(self, results):
        # Destruir el frame del gráfico anterior
        self.graph_frame.destroy()

        # Crear un nuevo gráfico con los resultados proporcionados
        self.graph_frame = GraphFrame(self.graphic, results)
        self.graph_frame.pack(fill="both", expand=True)

        # Actualizar el canvas para asegurarse de que el gráfico se muestre
        self.graph_frame.canvas.draw()
        
class XSlidePanel(tb.Frame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent, bootstyle="light")

        self.start_pos = start_pos
        self.end_pos = end_pos
        self.height = 1-abs(start_pos-end_pos)
        self.WIDTH = 0.58

        self.pos = start_pos
        self.in_start_pos = True

        self.place(relx=0, rely=self.start_pos, relheight=self.height, relwidth=self.WIDTH)
    
    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()
        
    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.05
            self.place(relx=0, rely=self.pos, relheight=self.height, relwidth=self.WIDTH)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.05
            self.place(relx=0, rely=self.pos, relheight=self.height, relwidth=self.WIDTH)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True

class Results(XSlidePanel):
    def __init__(self, master, start_pos, end_pos):
        super().__init__(parent=master, start_pos=start_pos, end_pos=end_pos)

        button_style = tb.Style()
        button_style.configure("primary.TButton", font=("Segoe UI Light", int(WIDTHSCREEN*0.00625)))

        self.resultados = tb.Button(self, bootstyle="primary", style="primary_TButton", text="Resultados", state="disabled", command=self.animate)
        self.resultados.pack(fill="x")

        self.results_title = tb.Label(self, bootstyle="lightinverse", font=("Segoe UI Light", int(WIDTHSCREEN*0.01)))
        self.results_title.pack(anchor="nw", padx=(int(WIDTHSCREEN)*0.008, 0), pady=int(HEIGHTSCREEN*0.014))

        self.results_label = tb.Label(self, bootstyle="lightinverse", wraplength=WIDTHSCREEN*0.55,font=("Segoe UI Light", int(WIDTHSCREEN*0.008)))
        self.results_label.pack(anchor="nw", padx=(int(WIDTHSCREEN)*0.008, 0), fill="both")

        self.cost_label = tb.Label(self, bootstyle="lightinverse", font=("Segoe UI Light", int(WIDTHSCREEN*0.01)))
        self.cost_label.pack(anchor="nw", padx=(int(WIDTHSCREEN)*0.008, 0), pady=int(HEIGHTSCREEN*0.015))
        self.cost = tb.Label(self,bootstyle="lightinverse", font=("Segoe UI Light", int(WIDTHSCREEN*0.008)))
        self.cost.pack(anchor="nw", padx=(int(WIDTHSCREEN)*0.008, 0))

class YSlidePanel(tb.Frame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = abs(end_pos-start_pos)+0.02

        self.pos = start_pos
        self.in_start_pos = True

        self.place(relx=self.start_pos, rely=0, relwidth=self.width, relheight=1)
    
    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()
        
    def animate_forward(self):
        if self.pos < self.end_pos:
            self.pos += 0.05
            self.place(relx=self.pos, rely=0, relwidth=self.width, relheight=1)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos > self.start_pos:
            self.pos -= 0.05
            self.place(relx=self.pos, rely=0, relwidth=self.width, relheight=1)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True

class MenuPanel(YSlidePanel):
    def __init__(self, master, start_pos, end_pos):
        super().__init__(parent=master, start_pos=start_pos, end_pos=end_pos)

        self.frame1 = tb.Frame(self, bootstyle="light")
        self.frame1.pack(fill="y", side="left")

        self.slide_menu = tb.Button(self.frame1, text="O\np\nc\ni\no\nn\ne\ns", bootstyle="success", width=int(WIDTHSCREEN*0.00156), command=self.animate)
        self.slide_menu.pack(side="left", fill="y", pady=int(HEIGHTSCREEN*0.04))

        self.menu = Menu(self)
        self.menu.pack(fill="both", expand=True, side="right")

class Menu(tb.Frame):
    def __init__(self, master):
        super().__init__(master=master, bootstyle="dark")
        self.blank = True

        self.icon_size = int(WIDTHSCREEN * 0.03)

        IconButton(self, bootstyle="danger", path="./images/close.png", width=self.icon_size, height=self.icon_size, command=close).pack(padx=20, pady=20, anchor="ne")

        SectionTitle(self, title="Seleccion de Ruta")

        self.route = RouteSelector(self)

        SectionTitle(self, "Método de Búsqueda")

        self.search_meth = SearchMethod(self)

        frame = tb.Frame(self, bootstyle="dark")
        frame.pack()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.icon_size = int(WIDTHSCREEN * 0.04)

        IconButton(frame, bootstyle="success", path="./images/search.png", width=self.icon_size, height=self.icon_size, command=search).grid(row=0, column=0, padx=self.icon_size, pady=(int(HEIGHTSCREEN*0.02), 0))
        IconButton(frame, bootstyle="warning", path="./images/clear.png", width=self.icon_size, height=self.icon_size, command=clear).grid(row=0, column=1, padx=self.icon_size, pady=(int(HEIGHTSCREEN*0.02), 0))

class IconButton(tb.Button):
    def __init__(self, master, bootstyle, width, height, path, command=None):
        super().__init__(master=master, bootstyle=bootstyle, command=command)
        self.width = width
        self.height = height
        self.path = path

        self.icon = self.resizeImage()

        self.config(image=self.icon)
        
        
    def resizeImage(self):
        image = Image.open(self.path).resize((self.width, self.height))
        image_tk = ImageTk.PhotoImage(image)
        return image_tk

class SectionTitle(tb.Frame):
    def __init__(self, master, title):
        super().__init__(master=master, bootstyle="dark")

        tb.Label(self, text=title, font=("Segoe UI Light", int(WIDTHSCREEN*0.01)), bootstyle="darkinverse").pack(pady=int(HEIGHTSCREEN*0.018))

        tb.Separator(self, bootstyle="light", orient="horizontal").pack(fill="x", padx=int(WIDTHSCREEN*0.04), pady= int(HEIGHTSCREEN*0.018))

        self.pack(fill="x", padx=int(WIDTHSCREEN*0.04), pady=int(HEIGHTSCREEN*0.018))

class RouteSelector(tb.Frame):
    def __init__(self, master):
        super().__init__(master=master, bootstyle="dark")

        global CONEXIONES

        self.in_blank = True

        self.lista_barrios = list(sorted(CONEXIONES.keys()))

        self.barrios = []
        for i in self.lista_barrios:
            self.barrios.append(i)


        self.barrio1 = tb.Combobox(self, bootstyle="light", values=self.barrios, state="readonly", font=(("Segoe UI Bold", int(WIDTHSCREEN*0.00625))))
        self.barrio1.grid(row=0, column=0)
        self.barrio1.bind("<<ComboboxSelected>>", self.deleteOption)

        tb.Label(self, text="a", bootstyle="darkinverse", font=("Segoe UI Light", int(WIDTHSCREEN*0.01))).grid(row=0, column=1, padx=(int(WIDTHSCREEN*0.03), 0))

        self.barrio2 = tb.Combobox(self, bootstyle="light", values=self.barrios, state="readonly", font=("Segoe UI Bold", int(WIDTHSCREEN*0.00625)))
        self.barrio2.grid(row=0, column=2, padx=(int(WIDTHSCREEN*0.03), 0))
        self.barrio2.bind("<<ComboboxSelected>>", self.deleteOption)

        self.pack(fill="both", padx=(int(WIDTHSCREEN*0.04), 0))
    
    def deleteOption(self, e):

        global CONEXIONES

        # Se crea nuevamente la lista cada vez que se selecciona una opcion
        self.barrios = []
        for i in self.lista_barrios:
            self.barrios.append(i)
        
        # Si el barrio 1 está seleccionado y se encuentra en la lista, se elimina
        if ((self.barrio1.get() != "")):
            self.barrios.remove(self.barrio1.get())
        # Si el barrio 2 está seleccionado se elimina
        if ((self.barrio2.get() != "")):
            self.barrios.remove(self.barrio2.get())

        # Se actualiza los combobox con las opciones que no fueron eliminadas
        self.barrio1.config(values=self.barrios)
        self.barrio2.config(values=self.barrios)

    def inBlank(self):
        if ((self.barrio1.get() != "") or (self.barrio2.get() != "")):
            self.in_blank = False
        
        return self.in_blank
    
    def setBlank(self):
        self.in_blank = True
        self.barrios = []
        for i in self.lista_barrios:
            self.barrios.append(i)
        self.barrio1.config(values=self.barrios)
        self.barrio2.config(values=self.barrios)
        self.barrio1.set("")
        self.barrio2.set("")

class SearchMethod(tb.Frame):
    def __init__(self, master):
        super().__init__(master=master, bootstyle="dark")

        self.in_blank = True

        radiobutton_style = tb.Style()
        radiobutton_style.configure("primary-outline-toolbutton.TRadioButton", font=("Segoe UI Bold"))

        self.lensearches = len(SEARCHES)
        
        self.search = tb.StringVar()

        self.radio_size = int(WIDTHSCREEN * 0.025)

        for i in range(self.lensearches):
            radio = tb.Radiobutton(self, style="primary-outline-toolbutton_TRadioButton", variable=self.search, text=SEARCHES[i], value=SEARCHES[i], width=self.radio_size)
            if (i == 0):
                radio.pack(pady=(0, int(HEIGHTSCREEN*(0.08/self.lensearches))))
            else:
                radio.pack(pady=int(HEIGHTSCREEN*(0.08/self.lensearches)))
                
        
        self.pack(fill="both", pady=int(HEIGHTSCREEN*0.01))

    def inBlank(self):
        if (self.search.get() != ""):
            self.in_blank = False

        return self.in_blank

    def setBlank(self):
        self.search.set("")
        self.in_blank = True

def search():

    result = None

    if (main.panel_menu.menu.search_meth.search.get() != ''):
        main.resultados.cost_label.config(text="")
        main.resultados.cost.config(text="")
        main.resultados.results_title.config(text="Ruta:")

    if (main.panel_menu.menu.search_meth.search.get() == SEARCHES[6]):
            result = searchHillClimbing(DICT_COORD)

    if (not(main.panel_menu.menu.route.inBlank())):

        b1 = main.panel_menu.menu.route.barrio1.get()
        b2 = main.panel_menu.menu.route.barrio2.get()

        if (main.panel_menu.menu.search_meth.search.get() == SEARCHES[0]):
            result = searchBFS(b1, b2, CONEXIONES)
        elif (main.panel_menu.menu.search_meth.search.get() == SEARCHES[1]):
            result = searchDFS(b1, b2, CONEXIONES)
        elif (main.panel_menu.menu.search_meth.search.get() == SEARCHES[2]):
            result = searchUCS(b1, b2, CONEXIONES)
        elif (main.panel_menu.menu.search_meth.search.get() == SEARCHES[3]):
            result = searchDSF(b1, b2, CONEXIONES)
        elif (main.panel_menu.menu.search_meth.search.get() == SEARCHES[4]):
            result = searchUCSInf(b1, b2, CONEXIONES, DICT_COORD)
        elif (main.panel_menu.menu.search_meth.search.get() == SEARCHES[5]):
            result = searchDijkstra(b1, b2, CONEXIONES)
    
    if (result is not None):
        if len(result) == 2:
            main.resultados.cost_label.config(text="Coste:")
            main.resultados.cost.config(text=f"{result[1]} m")
            result = result[0]

        main.resultados.results_label.config(text='->'.join(result))
        main.resultados.resultados.config(state="enabled")
        if (main.panel_menu.menu.search_meth.search.get() != SEARCHES[6]):
            main.grafo.graph_frame.highlight_path(result)
    

def clear():
    if (not(main.panel_menu.menu.route.inBlank()) or not(main.panel_menu.menu.search_meth.inBlank())):
        main.panel_menu.menu.route.setBlank()
        main.panel_menu.menu.search_meth.setBlank()
    main.resultados.animate_backwards()
    main.resultados.results_label.config(text="")
    main.resultados.cost_label.config(text="")
    main.resultados.cost.config(text="")
    main.resultados.resultados.config(state="disabled")
    main.grafo.graph_frame.clear_highlight()
    

def close():
    plt.close("all")
    main.destroy()
    

main = App("lumen", "dark")
    
main.mainloop()