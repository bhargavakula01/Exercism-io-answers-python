class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        list_sol = self.matrix_string.split('\n')

        for x in range(len(list_sol)):
            new_list = list_sol[x].split(' ')
            list_sol[x] = new_list

        for x in range(len(list_sol[index-1])):
            list_sol[index-1][x] = int(list_sol[index-1][x])
        return list_sol[index-1]

    def column(self, index):
        list_sol = self.matrix_string.split('\n')

        for x in range(len(list_sol)):
            new_list = list_sol[x].split(' ')
            list_sol[x] = new_list
        solution_list = []
        for z in list_sol:
            solution_list.append(int(z[index-1]))
        return solution_list