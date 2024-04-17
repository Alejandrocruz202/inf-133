from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "¡Hola, mundo!"


@app.route('/saludar',methods=['get'])
def saludar():
    nombre= request.args.get("nombre")
    if not nombre:
        return(
            jsonify({"error":"se requiere un nombre en los parametros de la url"}),
            400,
        )
    return jsonify({"mensaje":f"¡Hola, {nombre}!"})

@app.route('/sumar',methods=['get'])
def sumar():
    suma1=int(request.args.get("suma1"))
    suma2=int(request.args.get("suma2"))
    total=suma1+suma2
    if not(total) :
        return(
            jsonify({"error":"se requiere numeros en los parametros de la url"}),
            400,
        )
    return jsonify({"mensaje":f"¡La suma, {suma1}+{suma2}= {total}!"})

@app.route("/palindromo",methods=['get'])
def palindromo():
    pal=request.args.get("cadena")
    cad=pal[::-1]
    if(cad==pal):
        mens=f"la palabra: {pal} es un palindromo"
    else :
        mens=f"la palabra: {pal} no es un palindromo"
    if not(cad==pal):
        return(
            jsonify({"error":"se requiere un dato en los parametros de la url"}),
            400,
        )
    return jsonify({"mensaje":mens})

@app.route("/vocal",methods=["get"])
def vocal():
    cadena=request.args.get("cad")
    vocal=request.args.get("vocal")
    cont=cadena.count(vocal)
    if not(cadena):
        return(
            jsonify({"error":"se requiere un dato en los parametros de la url"}),
            400,
        )
    return jsonify({"mensaje":f"el numero de vocales {vocal} es de : {cont}"})
if __name__=='__main__':
    app.run()