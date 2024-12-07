import networkx as nx
import matplotlib.pyplot as plt

# Матрица переходных вероятностей
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 2/3, 1/3, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1/2, 1/2, 0, 0, 0, 0, 0],
    [0, 1/2, 0, 0, 0, 0, 1/4, 1/4],
    [0, 0, 0, 1/3, 2/3, 0, 0, 0],
    [1/2, 0, 0, 0, 0, 1/2, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0]
]

# Инициализация графа
G = nx.DiGraph()

# Добавляем рёбра в граф
num_states = len(matrix)
for i in range(num_states):
    for j in range(num_states):
        if matrix[i][j] > 0:  # Если есть переход
            G.add_edge(f"S{i+1}", f"S{j+1}", weight=matrix[i][j])

# Настройка позиций узлов для визуализации
pos = nx.spring_layout(G)  # Автоматическая раскладка графа

# Рисуем граф
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=1500, node_color="lightblue", font_size=10, font_weight="bold", arrowsize=20)

# Добавляем подписи для весов рёбер
edge_labels = nx.get_edge_attributes(G, 'weight')
edge_labels = {key: f"{value:.2f}" for key, value in edge_labels.items()}  # Округление до двух знаков
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

# Отображение графа
plt.title("Граф состояний Марковской цепи", fontsize=14)
plt.show()
