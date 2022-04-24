from flask import Flask, jsonify, request
import json

tarefas = [

    { 'id': 0, 'responsavel':'matheus','tarefa': 'feature engineering', 'status':'incompleta' },
    { 'id': 1, 'responsavel':'henrique','tarefa': 'machine learning modelling', 'status':'completa' }

]

app = Flask( __name__ )

# Pesquisar, alterar e deleter posição específica ( parâmetro posição )
@app.route( '/gerenciamento/<int:posicao>/', methods=['GET','PUT','DELETE'] )
def gerenciador_por_posicao(posicao):
    if request.method == 'GET':
        try:
            response = tarefas[posicao]
        except IndexError:
            response = 'Tarefa não existe'
        except Exception:
            response = 'Erro desconhecido'

        return jsonify( response )

    elif request.method == 'PUT':
        alteracao_status = json.loads(request.data)
        tarefas[posicao]['status'] = alteracao_status['status']

        return ( 'Tarefa modificada' )

    elif request.method == 'DELETE':
        tarefas.pop(posicao)

        return ( 'Tarefa deletada' )

# Listar todos os valores e inserir nova tarefa ( sem parâmetro de posição )
@app.route( '/gerenciamento/', methods=['GET','POST'] )
def gerenciador_generalizado():
    if request.method == 'GET':
        return( jsonify(tarefas) )

    elif request.method == 'POST':
        insercao = json.loads( request.data )
        tarefas.append( insercao )

        return( 'Nova tarefa inserida' )

if __name__ == '__main__':
    app.run( debug=True )