from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello',methods=['GET'])
def hello_world():
    return jsonify({'message':'Ola, Mundo! Bem-vindo a API Flask'})

@app.route('/api/tarefas', methods=['GET'])
def get_tarefas():
    tarefas = [
        {'id':1,'titulo':'Estudar Flask', 'concluida': False},
        {'id':2,'titulo':'Criar primeira API', 'concluida': False},
        {'id':3,'titulo':'Estudar Flask', 'concluida': False},
    ]
    return jsonify({'tarefas': tarefas})

if __name__ == '__main__':
    app.run(debug=True)