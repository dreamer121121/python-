class Node:
    def __init__(self, parent, rank=0, size=1):
        #初始化的时候每一个node指包含一个元素，且设置其parent为i
        self.parent = parent
        self.rank = rank
        self.size = size

    def __repr__(self):
        return '(parent=%s, rank=%s, size=%s)' % (self.parent, self.rank, self.size)


class Forest:
    def __init__(self, num_nodes):
        self.nodes = [Node(i) for i in range(num_nodes)]
        self.num_sets = num_nodes
        print("--initial nodes--",self.nodes[50316])

    def size_of(self, i):
        return self.nodes[i].size

    def find(self, n):
        temp = n
        while temp != self.nodes[temp].parent:
            temp = self.nodes[temp].parent

        self.nodes[n].parent = temp
        if n == 10558:
            print("--10558--",self.nodes[n].parent)
        return temp

    def merge(self, a, b):
        if self.nodes[a].rank > self.nodes[b].rank:
            self.nodes[b].parent = a
            self.nodes[a].size = self.nodes[a].size + self.nodes[b].size
        else:
            self.nodes[a].parent = b
            self.nodes[b].size = self.nodes[b].size + self.nodes[a].size

            if self.nodes[a].rank == self.nodes[b].rank:
                self.nodes[b].rank = self.nodes[b].rank + 1

        self.num_sets = self.num_sets - 1

    def print_nodes(self):
        for node in self.nodes:
            print(node)


def create_edge(img, width, x, y, x1, y1, diff):
    vertex_id = lambda x, y: y * width + x
    w = diff(img, x, y, x1, y1)
    return (vertex_id(x, y), vertex_id(x1, y1), w)


def build_graph(img, width, height, diff, neighborhood_8=False):
    """
    对每一个点只计算左上，左，左下，下四个diff,避免重复计算，但最终的graph为8邻域。
    :param img:
    :param width:
    :param height:
    :param diff:
    :param neighborhood_8:
    :return:
    """
    graph_edges = []
    for y in range(height):
        for x in range(width):
            if x > 0:
                graph_edges.append(create_edge(img, width, x, y, x - 1, y, diff))

            if y > 0:
                graph_edges.append(create_edge(img, width, x, y, x, y - 1, diff))

            if neighborhood_8:
                if x > 0 and y > 0:
                    graph_edges.append(create_edge(img, width, x, y, x - 1, y - 1, diff))

                if x > 0 and y < height - 1:
                    graph_edges.append(create_edge(img, width, x, y, x - 1, y + 1, diff))

    return graph_edges


def remove_small_components(forest, graph, min_size):
    for edge in graph:
        a = forest.find(edge[0])
        b = forest.find(edge[1])

        if a != b and (forest.size_of(a) < min_size or forest.size_of(b) < min_size):
            forest.merge(a, b)

    return forest


def segment_graph(graph_edges, num_nodes, const, min_size, threshold_func):
    # Step 1: initialization
    forest = Forest(num_nodes)
    weight = lambda edge: edge[2] #定义一个匿名函数
    sorted_graph = sorted(graph_edges, key=weight)  # 按权重对所有节点进行了升序排列。
    threshold = [threshold_func(1, const) for _ in range(num_nodes)] #初始化的时候T函数的尺寸为1,为每个node添加T函数值，有多少个component就有多少个阈值

    # Step 2: merging
    for edge in sorted_graph:
        parent_a = forest.find(edge[0])
        parent_b = forest.find(edge[1])

        #第一次合并，判断是否满足条件
        a_condition = weight(edge) <= threshold[parent_a]
        b_condition = weight(edge) <= threshold[parent_b]

        if parent_a != parent_b and a_condition and b_condition:
            forest.merge(parent_a, parent_b)
            a = forest.find(parent_a)
            threshold[a] = weight(edge) + threshold_func(forest.nodes[a].size, const)

    return remove_small_components(forest, sorted_graph, min_size)
