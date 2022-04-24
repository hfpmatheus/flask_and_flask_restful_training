from flask import Flask, request
from flask_restful import Resource, Api
import json

tarefas = [

    { 'id': 0, 'responsavel':'matheus','tarefa': 'feature engineering', 'status':'incompleta' },
    { 'id': 1, 'responsavel':'henrique','tarefa': 'machine learning modelling', 'status':'completa' }

]

app = Flask( __name__ )
api = Api( app )

# Pesquisar, alterar e deleter posição específica ( parâmetro posição )
class gerenciador_por_posicao( Resource ):
    def get( self, posicao ):
        try:
            response = tarefas[posicao]
        except IndexError:
            response = 'Tarefa não existe'
        except Exception:
            response = 'Erro desconhecido'

        return response

    def put( self, posicao ):
        alteracao_status = json.loads( request.data )
        tarefas[posicao]['status'] = alteracao_status['status']

        return ('Tarefa modificada')

    def delete( self, posicao ):
        tarefas.pop(posicao)

        return ('Tarefa deletada' )

# Listar todos os valores e inserir nova tarefa ( sem parâmetro de posição )
class gerenciador_generalizado( Resource ):
    def get(self):
        return tarefas

    def post(self):
        insercao = json.loads( request.data )
        tarefas.append( insercao )

        return ( 'Tarefa adicionada' )

api.add_resource( gerenciador_por_posicao, '/gerenciamento/<int:posicao>/' )
api.add_resource( gerenciador_generalizado, '/gerenciamento/')

if __name__ == '__main__':
    app.run( debug=True )
