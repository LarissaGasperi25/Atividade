from config import *

class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " +\
            self.email + ", " + self.telefone
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone
        }

class Animal(db.Model):
    # atributos do animal
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    raca = db.Column(db.String(254))
    pessoa_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)
    responsavel = db.relationship("Pessoa")
    sexo = db.Column(db.String(254))

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " +\
            self.raca + ", " + str(self.responsavel) + ", " + self.pessoa_id + ", " + self.sexo
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "raca": self.raca,
            "responsavel": self.responsavel.json(),
            "pessoa_id": self.pessoa_id,
            "sexo": self.sexo
        }

# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    # teste da classe Pessoa
    p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", 
        telefone = "47 99012 3232")
    # persistir
    db.session.add(p1)
    db.session.commit()
    # exibir a pessoa
    print(p1)
    # exibir a pessoa no format json
    print(p1.json())

    # teste do Animal
    a1 = Animal(nome = "Lily", raca = "Bengali", 
        responsavel = p1, sexo = "Fêmea")
    # persistir
    db.session.add(a1)
    db.session.commit()
    # exibir o animal
    print(a1)
    # exibir o animal no format json
    print(a1.json())
