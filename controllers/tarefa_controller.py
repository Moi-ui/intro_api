from models import Tarefa
from models import db

class TarefaController:
    
    @staticmethod
    def get_lista_tarefas():
        return Tarefa.query.all()
    
    @staticmethod
    def get_listar_tarefas_id(tarefa_id):
        return Tarefa.query.get(tarefa_id)
    
    @staticmethod
    def post_criar_tarefa(id, tarefa, concluida):
        nova_tarefa = Tarefa(id=id, titulo=tarefa['titulo'], concluida=concluida)
        db.session.add(nova_tarefa)
        db.session.commit()
        return nova_tarefa
    
    @staticmethod
    def delete_remover_tarefa(tarefa_id: int):  
        tarefa = Tarefa.query.get(tarefa_id)
        if tarefa:
            db.session.delete(tarefa)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def put_atualizar_tarefa(self, tarefa_id: int, dados: dict):
        tarefa = Tarefa.query.get(tarefa_id)
        if tarefa:
            tarefa.titulo = dados.get('titulo', tarefa.titulo)
            tarefa.concluida = dados.get('concluida', tarefa.concluida)
            db.session.commit()
            return tarefa
        return None