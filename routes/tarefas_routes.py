from flask import Blueprint, request, jsonify
from controllers.tarefa_controller import TarefaController

tarefas_bp = Blueprint('tarefas', __name__)

@tarefas_bp.route('/api/tarefas', methods=['GET'])
def get_listar_tarefas():
    return jsonify([tarefa.to_dict() for tarefa in TarefaController.get_lista_tarefas()])

tarefas_bp.route('/api/tarefas/<int:tarefa_id>', methods=['GET'])
def get_tarefa_id(tarefa_id):
    tarefa = TarefaController.get_listar_tarefas_id(tarefa_id)
    if tarefa:
        return jsonify(tarefa.to_dict())
    return jsonify({'mensagem': 'Tarefa não encontrada'}), 404

@tarefas_bp.route('/api/criar_tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()
    id = dados.get('id')
    titulo = dados.get('titulo')
    concluida = dados.get('concluida', False) # Padrão é False se não vier no JSON
    nova_tarefa = TarefaController.post_criar_tarefa(id, {'titulo':titulo}, concluida)
    return jsonify(nova_tarefa.to_dict()), 

@tarefas_bp.route('/api/remover_tarefa/<int:tarefa_id>', methods=['DELETE'])
def remover_tarefa(tarefa_id):
    deletado = TarefaController.delete_remover_tarefa(tarefa_id)
    if deletado:
        return jsonify({'mensagem': 'Tarefa removida com sucesso'})
    return jsonify({'mensagem': 'Tarefa não encontrada'}), 404

@tarefas_bp.route('/api/atualizar_tarefa/<int:tarefa_id>', methods=['PUT'])
def atualizar_tarefa(tarefa_id):
    dados = request.get_json()
    tarefa_atualizada = TarefaController.put_atualizar_tarefa(tarefa_id, dados)
    if tarefa_atualizada:
        return jsonify(tarefa_atualizada.to_dict())
    return jsonify({'mensagem': 'Tarefa não encontrada'}), 404