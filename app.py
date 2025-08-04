from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from urllib.parse import quote
from config import config

def create_app(config_name=None):
    """Factory function para crear la aplicación Flask"""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    return app

app = create_app()

def load_customers():
    """Carga los datos de clientes desde el archivo Excel"""
    try:
        if os.path.exists('clientes.xlsx'):
            df = pd.read_excel('clientes.xlsx')
            # Convertir a lista de diccionarios
            customers = df.to_dict('records')
            return customers
        else:
            # Datos de ejemplo si no existe el archivo
            return [
                {
                    'nombre': 'Juan Pérez',
                    'numero': '2664123456',
                    'direccion': 'Mitre 123',
                    'saldo': 2500.00
                },
                {
                    'nombre': 'Ana Gómez',
                    'numero': '2664123457',
                    'direccion': 'Belgrano 456',
                    'saldo': 1500.00
                },
                {
                    'nombre': 'Carlos López',
                    'numero': '2664123458',
                    'direccion': 'San Martín 789',
                    'saldo': 3200.00
                }
            ]
    except Exception as e:
        print(f"Error cargando datos: {e}")
        return []

def search_customers(query, customers):
    """Busca clientes por número o dirección"""
    if not query:
        return []
    
    query = query.lower().strip()
    results = []
    
    for customer in customers:
        # Buscar por número
        if query in str(customer.get('numero', '')).lower():
            results.append(customer)
        # Buscar por dirección
        elif query in str(customer.get('direccion', '')).lower():
            results.append(customer)
        # Buscar por nombre
        elif query in str(customer.get('nombre', '')).lower():
            results.append(customer)
    
    return results

def generate_whatsapp_link(customer):
    """Genera el enlace de WhatsApp para un cliente"""
    numero = str(customer.get('numero', ''))
    nombre = str(customer.get('nombre', ''))
    saldo = str(customer.get('saldo', ''))
    
    # Formatear el mensaje
    message = f"Hola {nombre}, tu saldo es de ${saldo}"
    encoded_message = quote(message)
    
    return f"https://wa.me/549{numero}?text={encoded_message}"

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/search')
def search():
    """Endpoint para buscar clientes"""
    query = request.args.get('q', '')
    customers = load_customers()
    results = search_customers(query, customers)
    
    # Agregar enlace de WhatsApp a cada resultado
    for result in results:
        result['whatsapp_link'] = generate_whatsapp_link(result)
    
    return jsonify(results)

if __name__ == '__main__':
    # Configuración para desarrollo
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.environ.get('PORT', 5001))
    
    app.run(
        debug=debug_mode, 
        host='0.0.0.0', 
        port=port,
        threaded=True
    ) 