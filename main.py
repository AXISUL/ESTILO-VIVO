from diccionario import diccionario
from flask import Flask, render_template, request, redirect, url_for

# variable de inicio
app = Flask(__name__,template_folder='templates')

#Rutas de la app
@app.route('/')  
def index():
  return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesarCameron():
  genero = request.form['genero']
  listaEstilos = request.form['estilos']
  color = request.form['color']
  resultado = listadoPrendas(genero, listaEstilos, color)
  return redirect(url_for('prendasEscogidas', key=resultado))

@app.route('/cameron') 
def cameron():
  return render_template('cameron.html')

@app.route('/comofunciona')
def comofunciona():
  return render_template('comofunciona.html')

@app.route('/comunidad')
def comunidad():
  return render_template( 'comunidad.html')

@app.route('/iniciarsesion')
def iniciarsesion():
  return render_template('iniciarsesion.html')

@app.route('/prendasEscogidas/<key>')
def prendasEscogidas(key):
  lista_imagenes = diccionario.get(key)
  imagen = request.args.get('imagen')
  if lista_imagenes:
    return render_template('prendasEscogidas.html', lista_imagenes=lista_imagenes, imagen=imagen)
  else:
    return "Clave no encontrada"
    
@app.route('/prendaindividual')
def prendaindividual():
  #pasar parametros por medio query's
  key = request.args.get('key', '')
  imagen_seleccionada = request.args.get('imagen', 'cameron.jpeg')
  return render_template('prendaindividual.html', key=key, imagen=imagen_seleccionada)
    
#Funciones de la app
def listadoPrendas(genero, estilo, color):
  key = f"{genero}_{estilo}_{color}"
  return key
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
  app.run(debug=True)
