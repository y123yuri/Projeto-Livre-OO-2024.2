class Materia():
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        
    def __repr__(self):
        return f"Materia(nome={self.nome}, codigo={self.codigo})" #isso daqui é a forma como se enxerga o objeto
    

class Turma():
    def __init__(self, professor, horario, local, semestre, materia ):
        self.professor = professor  
        self.horario = horario  
        self.local = local  
        self.semestre = semestre  
        self.materia = materia

    def __repr__(self):
        return f"Turma(nome={self.professor}, codigo={self.materia})"

class Usuario():
    def __init__(self, turmas_horarios, materias):
        self.turmas_horarios = turmas_horarios
        self.materias = materias


    
        



