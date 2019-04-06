def get_professores(cursor):
    cursor.execute(f'select nome, idprofessor from faculdade.professor order by Nome ASC')
    professores = cursor.fetchall()
    cursor.close()
    return professores

def get_prof_details(cursor, idprofessor):
    cursor.execute(f'select nome, DataNasc, NomeMae, Titulacao from faculdade.professor where professor.idprofessor = "{idprofessor}"')
    profdetails = cursor.fetchone()
    cursor.close()
    return profdetails

def get_prof_disciplinas(cursor, idprofessor):
    cursor.execute(f'select NomeDisciplina, curso, cargahoraria from faculdade.disciplina, faculdade.professor where professor.idprofessor = "{idprofessor}" and professor.idprofessor = disciplina.idprofessor')
    profdisciplinas = cursor.fetchall()
    cursor.close()
    return profdisciplinas

def get_form_titulacao(cursor,titulacao):
    cursor.execute(f'select nome, idprofessor from faculdade.professor where Titulacao = "{titulacao}"')
    professores = cursor.fetchall()
    cursor.close()
    return professores