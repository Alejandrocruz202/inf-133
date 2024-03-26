
from http.server import HTTPServer,BaseHTTPRequestHandler
import json


tacos={}

class taco:
    def __init__(self):
        self.tamaño=None
        self.masa=None
        self.ingredientes=[]
    
    def __str__(self):
        return f"tamaño: {self.tamaño}, Masa: {self.masa}, ingredientes: {", ".join(self.ingredientes)}"
    
class TacosBuilder:
    def __init__(self):
        self.pizza=taco()

    def set_tamaño(self, tamaño):
        self.pizza.tamaño=tamaño

    def set_masa(self, masa):
        self.pizza.masa=masa
    
    def add_ingrediente(self , ingrediente):
        self.pizza.ingredientes.append(ingrediente)

    def get_pizza(self):
        return self.pizza
    
class taqueria:
    def __init__(self,builder):
        self.builder=builder

    def create_tacos(self, tamaño , masa, ingredientes):
        self.builder.set_tamaño(tamaño)
        self.builder.set_masa(masa)
        for ingrediente in ingredientes:
            self.builder.add_ingrediente(ingrediente)
        return self.builder.get_pizza()

class TacosService:
    def __init__(self):
        self.builder=TacosBuilder()
        self.taqueria=taqueria(self.builder)

    def create_taco(self, post_data):
        tamaño=post_data.get("tamaño", None)
        masa = post_data.get("masa",None)
        ingredientes=post_data.get("ingredientes",[])

        taco=self.taqueria.create_tacos(tamaño, masa ,ingredientes)
        tacos[len(tacos)+1]=taco

        return taco
    
    def read_taco(self):
        return{index: taco.__dict__ for index, taco in tacos.items() }

    def update_taco(self, index,post_data):
        if(index in tacos):
            taco=taco[index]
            tamaño=post_data.get("tamaño",None)
            masa=post_data.get("masa",None)
            ingredientes=post_data.get("toppings",[])

            if tamaño:
                taco.tamaño=tamaño
            if masa: 
                taco.masa=masa
            if ingredientes:
                taco.ingredientes=ingredientes
            return taco
        else:
            return None
    def delete_taco(self, index):
        if index in tacos:
            return tacos.pop(index)
        else:
            return None

class HTTPDataHandler:
    @staticmethod
    def handler_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Conten-Type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length=int(handler.headers["Content-Length"])
        post_data=handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))

class TacoHandler(BaseHTTPRequestHandler):
    def __init__(self, *args , **kwargs) :
        self.controller=TacosService()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path =="/tacos":
            data=HTTPDataHandler.handle_reader(self)
            response_data=self.controller.create_taco(data)
            HTTPDataHandler.handler_response(self,200 ,response_data.__dict__)
        else: 
            HTTPDataHandler.handler_response(self, 404,{"error":"Ruta no existe"})

    def do_GET(self):
        if self.path =="/tacos":
            
            response_data =self.controller.read_taco()
            HTTPDataHandler.handler_response(self,200 ,response_data)
        else:
            HTTPDataHandler.handler_response(self, 404,{"error":"Ruta no existe"})
    def do_PUT(self):
        if self.path.startswith("/tacos/"):
            index=int(self.path.split("/")[2])
            data=HTTPDataHandler.handle_reader(self)
            response_data=self.controller.update_taco(index, data)
            if response_data:
                HTTPDataHandler.handler_response(self,200,response_data.__dict__)
            else:
                HTTPDataHandler.handler_response(
                    self,404,{"error":" Indice taco no valido"}
                )
        else:
            HTTPDataHandler.handler_response(self, 404, {"Error": "Ruta no existente"})
    def do_DELETE(self):
        if self.path.startswith("/tacos/"):
            index = int(self.path.split("/")[2])
            deleted_pizza = self.controller.delete_taco(index)
            if deleted_pizza:
                HTTPDataHandler.handler_response(
                    self, 200, {"message": "Pizza eliminada correctamente"}
                )
            else:
                HTTPDataHandler.handler_response(
                    self, 404, {"Error": "Índice de taco no válido"}
                )
        else:
            HTTPDataHandler.handler_response(self, 404, {"Error": "Ruta no existente"})
def run(server_class=HTTPServer, handler_class=TacoHandler ,port=8000):
    server_address =("",port)
    httpd =server_class(server_address,handler_class)
    print(f"iniciando servidor HTTP en puerto {port}...")
    httpd.serve_forever()

if __name__ =="__main__":
    run()            