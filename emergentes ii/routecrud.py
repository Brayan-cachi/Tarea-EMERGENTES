from flask import Flask, request, jsonify

app = Flask(__name__)

tareas = [
    {'id':1,'tarea':'Aprender Flask','completada':False},
    {'id':2,'tarea':'Practica Flask','completada':False}
]

#GET - Obtener las tareas 
@app.route("/api/tareas",methods=['GET'])
def listar_tareas():
    return jsonify(tareas)

#get - obtener una tarea espesifica
@app.route("/api/tareas/<int:tarea_id>", methods=['GET'])
def obtener_tarea(tarea_id):
    tare = None
    for t in tareas:
        if t['id'] == tarea_id:
            tarea = t
            break
    if tarea:
        return jsonify(tarea)
    return jsonify({'error':'Tarea no encotrada'}),404

#POST -crear una tarea
@app.route("/api/tareas", methods=['POST'])
def crear_tarea():
    nueva_tarea ={
        'id':len(tareas)+1,
        'tarea':request.json.get('tarea',''),
        'completada':request.json.get('completada',Flask)
    }
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201

#DELET - Eliminar tarea
@app.route('/api/tareas/<int:tarea_id>', methods=['DELETE'])
def eliminar_tarea(tarea_id):
    global tareas 
    tareas = [t for t in tareas if t['id']!= tarea_id]
    return jsonify({'mensaje':'Tarea eliminada'}), 200
     
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201
    
            

if __name__ == "__main__":
    app.run(debug=True)