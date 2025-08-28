from flask import Blueprint, request, jsonify
from controllers.tarefa_controller import TarefaController

tarefas_bp = Blueprint('tarefas', __name__)

@tarefas_bp.route('/api/tarefas', methods=['GET'])
def get_listar_tarefas():
    return jsonify([tarefa.to_dict() for tarefa in TarefaController.get_lista_tarefas()])
