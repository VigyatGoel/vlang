class Interpreter:
    def __init__(self):
        self.variables = {}

    def run(self, tree):
        for node in tree:
            if node:
                self.execute(node)

    def execute(self, node):
        type = node[0]
        if type == "ASSIGN":
            self.variables[node[1]] = eval(node[2], {}, self.variables)
        elif type == "PRINT":
            print(eval(node[1], {}, self.variables))
        elif type == "WHILE":
            while eval(node[1], {}, self.variables):
                self.run(node[2])
        elif type == "IF":
            if eval(node[1], {}, self.variables):
                self.run(node[2])
            elif node[3] is not None:
                self.run(node[3])
