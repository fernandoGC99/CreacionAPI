from flask import Flask, jsonify, request

app  = Flask(__name__)

#IMPORTAMOS NUESTRO FICHERO JSON, para mas adelante poder modificarlo
from Discografia import Discografia



#El gran saludo de Fernando
@app.route("/")

def saludo():

    return("Bienvenido a mi super API de Discografias")

# Testing Route

@app.route('/ping', methods=['GET'])

def ping():

    return jsonify({'response': 'pong!'})




@app.route('/Discografia')
def getDiscografia():
    return jsonify({'Discografia': Discografia })

@app.route('/Discografia/<string:Discografia_Ano>')
def getDiscografias(Discografia_Ano):
    encontrado= False
    for Ano in Discografia:
        if Ano['Ano'].lower() == Discografia_Ano.lower():
            DiscografiaFound=Ano
            encontrado=True
    if encontrado==True:
        return jsonify({'Discografia': DiscografiaFound})
    else:
        return jsonify({'message': 'Ano no encontrado'})

#Crear data routes
@app.route('/Discografia', methods=['POST'])
def crearruta():
    new_Discografia = {
        
        "titulo": "La cancion de Juan Perro",
        "artista": "Radio Futura",
        "pais": "España",
        "discografica": "Sony Music-Ariola",
        "precio": "9.90",
        "Ano": "1987"
    }
    Discografia.append(new_Discografia)
    return jsonify({'mensaje':'Discografia agregado correctamente','Discografia': Discografia})



# Actualización de dataroute

@app.route('/Discografia/<string:Discografia_Ano>', methods=['PUT'])

def editDiscografia(Discografia_Ano):

    for Discografias in Discografia:
        if Discografias['Ano'] == Discografia_Ano.lower():
            DiscografiaFound=Discografia
            
    if (len(DiscografiaFound) > 0):
                DiscografiaFound[0]['titulo'] = request.json['titulo']
                DiscografiaFound[0]['Ano'] = request.json['Ano']
                DiscografiaFound[0]['artista'] = request.json['artista']
                return jsonify({
                    'message': 'Discografia Modificado Correctamente',
                    'Discografia': DiscografiaFound[0]

        })

    return jsonify({'message': 'Discografia No encontrado'})

# Borrado ruta

@app.route('/Discografia/<string:Discografia_titulo>', methods=['DELETE'])

def deleteProduct(Discografia):

    for product in Discografia:

        if product['titulo'] == Discografia.lower():

            DiscografiaFound=product

    if len(DiscografiaFound) > 0:

        Discografia.remove(DiscografiaFound[0])

        return jsonify({

            'message': 'Discografia Borrado',

            'Discografia': Discografia

        })

    

if __name__ == '__main__':
    app.run(debug=True, port=4000)