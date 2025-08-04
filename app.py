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

@app.route('/login')
def login():
    """Endpoint para autenticar clientes"""
    direccion = request.args.get('direccion', '').strip().lower()
    telefono = request.args.get('telefono', '').strip()
    
    if not direccion or not telefono:
        return jsonify({'success': False, 'message': 'Datos incompletos'})
    
    customers = load_customers()
    
    # Buscar cliente que coincida exactamente con dirección y teléfono
    for customer in customers:
        customer_direccion = str(customer.get('direccion', '')).lower()
        customer_telefono = str(customer.get('numero', ''))
        
        if direccion in customer_direccion and telefono == customer_telefono:
            # Agregar enlace de WhatsApp
            customer['whatsapp_link'] = generate_whatsapp_link(customer)
            return jsonify({
                'success': True, 
                'customer': customer,
                'message': 'Cliente autenticado correctamente'
            })
    
    return jsonify({'success': False, 'message': 'Datos incorrectos'})

@app.route('/refresh-balance')
def refresh_balance():
    """Endpoint para actualizar saldo del cliente"""
    direccion = request.args.get('direccion', '').strip().lower()
    telefono = request.args.get('telefono', '').strip()
    
    if not direccion or not telefono:
        return jsonify({'success': False, 'message': 'Datos incompletos'})
    
    customers = load_customers()
    
    # Buscar cliente y actualizar saldo (simulado)
    for customer in customers:
        customer_direccion = str(customer.get('direccion', '')).lower()
        customer_telefono = str(customer.get('numero', ''))
        
        if direccion in customer_direccion and telefono == customer_telefono:
            # En un caso real, aquí se consultaría la base de datos
            # Por ahora, simulamos una pequeña variación en el saldo
            import random
            variation = random.uniform(-100, 100)
            customer['saldo'] = round(float(customer.get('saldo', 0)) + variation, 2)
            
            # Agregar enlace de WhatsApp
            customer['whatsapp_link'] = generate_whatsapp_link(customer)
            return jsonify({
                'success': True, 
                'customer': customer,
                'message': 'Saldo actualizado'
            })
    
    return jsonify({'success': False, 'message': 'Cliente no encontrado'})

@app.route('/search')
def search():
    """Endpoint para buscar clientes (mantenido para compatibilidad)"""
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