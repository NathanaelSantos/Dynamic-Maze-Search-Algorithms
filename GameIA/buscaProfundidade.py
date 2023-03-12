import graph_tool.all as gt                       # Biblioteca para GRAFO
import csv                                        # Biblioteca para Leitura do csv


class VisitorExample(gt.DFSVisitor):                                            # É um objeto visitante que é chamado nos pontos de evento dentro do algoritmo bfs_search()

    def __init__(self, name, pred, dist, time, name_time, color, v_color, e_action_dfs):
        self.name = name
        self.pred = pred
        self.dist = dist
        self.time = time
        self.name_time = name_time
        self.last_time = 0
        self.color = color
        self.fill_color = v_color
        self.e_action_dfs = e_action_dfs

    def discover_vertex(self, u):                                               # Invocado quando um vértice é encontrado pela primeira vez.
        self.name[u] = v_name[u]
        self.time[u] = self.last_time
        self.last_time += 1        
        self.name_time[u] = str(self.name[u]) + "(" + str(self.time[u]) + ")"
        print("-->", self.name[u], "foi encontrado e entrou na PILHA") 
        self.fill_color[u] = "white"

    def examine_vertex(self, u):                                                # Invocado em um vértice à medida que é retirado da fila. 
        print(self.name[u], "saiu da PILHA e está sendo analisado (expandido)...") 

    def tree_edge(self, e):                                                     # Invocado em cada aresta à medida que se torna um 
        self.pred[e.target()] = int(e.source())                                 # membro das arestas que formam a árvore de pesquisa.
        self.dist[e.target()] = self.dist[e.source()] + 1
        e = g_dfs.add_edge(int(e.source()), int(e.target()))
        self.color[e] = "gray"
        self.e_action_dfs[e] = e_action[g.edge(int(e.source()), int(e.target()))]

    def finish_vertex(self, u):
        print("Todos os vértices adjacentes à", self.name[u], "foram descobertos!") 


g = gt.Graph() 
g.set_directed(False)                                   # criação do objeto
v_name = g.new_vertex_property("string")          # referenciação da lista v_name com uma nova propriedade (label) criada para o vértice - tipo string  
e_action = g.new_edge_property("string")

#Criação dos vértices no grafo à partir do arquivo .cvs de vértices
f_network = open("vertex.csv", 'r')
reader_network = csv.reader(f_network, delimiter=";")
for vertice in reader_network:
     v = g.add_vertex()
     v_name[v] = str(vertice[1])
f_network.close()
# Lista de vértices criados
print(list(v_name))

#Criação das arestas no grafo à partir do arquivo .cvs de arestas
f_network = open("edges.csv", 'r')
reader_network = csv.reader(f_network, delimiter=";")
for edge in reader_network:
     e = g.add_edge(int(edge[0]), int(edge[1]))
     e_action[e] = str(edge[2])
f_network.close()
# Lista de arestas criadas
print(g.get_edges())

#Desenhando o grafo
'''gt.graph_draw(g, #pos=gt.arf_layout(visual_G),
               vertex_text= v_name,
               edge_text = e_action,
               edge_pen_width = 10,              
               vertex_font_size=18,
               edge_font_size = 10,
               vertex_shape="circle",
               vertex_fill_color="#729fcf",
               output_size=(6000, 6000),
               output="BuscaProfundidade.png")'''

#Busca em Profundidade (bfs) e geração das arestas
g_dfs = gt.Graph()                                      # criação do objeto para busca em Profundidade
v_name_dfs   = g_dfs.new_vertex_property("string")      # referenciação da lista v_name com uma nova propriedade (label) criada para o vértice - tipo string 
v_name_time  = g_dfs.new_vertex_property("string")      # referenciação da lista timed com uma nova propriedade da aresta criada para a ordem de expansão - tipo int
dist         = g_dfs.new_vertex_property("int")         # referenciação da lista dist como uma propriedade do vértice criada para a distância da raiz
pred         = g_dfs.new_vertex_property("int64_t")     # referenciação da lista pred como uma propriedade do vétice criada para referenciar o predecessor (pai)
time         = g_dfs.new_vertex_property("int")         # referenciação da lista timed com uma nova propriedade da aresta criada para a ordem de expansão - tipo int
color        = g_dfs.new_edge_property("string")        # referenciação da lista ecolor com uma nova propriedade criada para a aresta - tipo string  
v_color      = g_dfs.new_vertex_property("string")      # referenciação da lista ecolor com uma nova propriedade criada para o vértice - tipo string  
e_action_dfs = g_dfs.new_edge_property("string")

print("------------------------------------------------------")
print("> Busca em Profundidade - Caminhamento pelos Estados")
print("------------------------------------------------------\n")
raiz = '(1, 0)'
alvo = '(11, 15)'
index_raiz = list(v_name).index(raiz)

gt.dfs_search(g, g.vertex(index_raiz), VisitorExample(v_name_dfs, pred, dist, time, v_name_time, color, v_color, e_action_dfs))
print("\n> Informações relevantes:")
print("-----------------------------\n")
print("Espaço de Estados......:", list(v_name_dfs))
print("Ordem de Expansão......:", list(time))
print("Estados e Ordem de Exp.:", list(v_name_time))
print("Precedessores..........:", list(pred))
print("Distância da raiz......:", list(dist))
print("Cores Arestas..........:", list(color))
print("Ações das Arestas......:", list(e_action_dfs))

print("\n> Procura de um Estado e Caminho:")
print("-----------------------------\n")
index = list(v_name_dfs).index(alvo)                     # Localizando o índice do Estado a ser encontrado
path = []                                                # array do caminho
path.insert(0,v_name_dfs[index])                         # inserções sendo realizadas no início
v_color[index] = "green"
while index != index_raiz:
  e = g_dfs.edge(pred[index], index)
  color[e] = "red"
  index = pred[index]
  path.insert(0,v_name_dfs[index])
  v_color[index] = "#729fcf"
v_color[index_raiz] = "#729fcf"; print("Cores Vértices.........:", list(v_color))

print("Caminho encontrado.....:",path)                   # mostrando o caminho encontrado da raiz ao alvo

#Desenhando o grafo
gt.graph_draw(g_dfs, #pos=gt.sfdp_layout(g_dfs),
              vertex_size = 80,
              vertex_text= v_name_dfs,
              edge_text= e_action_dfs,
              edge_color= color,
              vertex_font_size=18,
              edge_font_size = 10,
              edge_pen_width = 10,
              vertex_fill_color=v_color,              
              vertex_shape="circle",
              #vertex_fill_color="#729fcf",
              output_size=(6000, 6000),
              output="BuscaProfundidade.png")  

string_list = '\n'.join(path) + '\n'
with open('dfs_path.txt', 'w') as file:
    file.write(string_list)  