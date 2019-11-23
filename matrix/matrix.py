class Matrix(object):
    def __init__(self, matrix_string):
        
        rows = matrix_string.splitlines()
        self.mat = [[int(i) for i in row.split(' ')] for row in rows]       

    def row(self, index):
        return self.mat[index-1][:]
        

    '''def column(self, index):
        mat_trans = [[self.mat[j][i] for j in range(len(self.mat))] for i in range(len(self.mat[0]))]
        return mat_trans[index-1][:]
    '''
    def column(self,index):
        return [self.mat[i][index-1] for i in range(len(self.mat))]