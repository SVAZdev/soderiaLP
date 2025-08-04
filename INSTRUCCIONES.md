# 📋 Instrucciones de Uso - Web de Consulta de Saldo

## 🚀 Cómo ejecutar la aplicación

### 1. Verificar que tienes Python 3.9+ instalado
```bash
python3 --version
```

### 2. Instalar las dependencias
```bash
python3 -m pip install Flask pandas openpyxl
```

### 3. Ejecutar la aplicación
```bash
python3 app.py
```

### 4. Abrir en el navegador
Ve a: `http://localhost:5001`

---

## 📊 Cómo usar la aplicación

### Para los clientes:
1. **Ingresa tu número de teléfono** (ej: 2664123456) o **tu dirección** (ej: Mitre 123)
2. **Presiona Enter** o haz clic en "Buscar"
3. **Verás tu saldo** y podrás enviar un mensaje por WhatsApp

### Para el administrador:
- **Modifica el archivo `clientes.xlsx`** para actualizar los datos
- **Reinicia la aplicación** después de modificar el Excel

---

## 🔧 Personalización

### Cambiar el puerto
Si el puerto 5001 está ocupado, edita `app.py` línea 94:
```python
app.run(debug=True, host='0.0.0.0', port=5002)  # Cambia 5001 por otro puerto
```

### Modificar el mensaje de WhatsApp
Edita `app.py` línea 58:
```python
message = f"Hola {nombre}, tu saldo es de ${saldo}"
```

### Cambiar el diseño
- **Colores**: Edita `static/style.css`
- **Interfaz**: Edita `templates/index.html`

---

## 📁 Estructura de archivos

```
SoderiaLP/
├── app.py              # Servidor Flask
├── clientes.xlsx       # Datos de clientes
├── requirements.txt    # Dependencias Python
├── templates/
│   └── index.html     # Página web principal
├── static/
│   └── style.css      # Estilos CSS
└── readme.md          # Documentación principal
```

---

## 🐛 Solución de problemas

### Error: "Address already in use"
- Cambia el puerto en `app.py`
- O ejecuta: `lsof -ti:5001 | xargs kill -9`

### Error: "No module named 'pandas'"
- Ejecuta: `python3 -m pip install pandas`

### Error: "No module named 'openpyxl'"
- Ejecuta: `python3 -m pip install openpyxl`

### La aplicación no carga el Excel
- Verifica que `clientes.xlsx` esté en la raíz del proyecto
- Asegúrate de que tenga las columnas: `nombre`, `numero`, `direccion`, `saldo`

---

## 📱 Funcionalidades

✅ **Búsqueda por número de teléfono**  
✅ **Búsqueda por dirección**  
✅ **Búsqueda por nombre**  
✅ **Búsqueda en tiempo real**  
✅ **Enlace directo a WhatsApp**  
✅ **Diseño responsive**  
✅ **Interfaz moderna**  
✅ **Manejo de errores**  

---

## 🔒 Seguridad

- La aplicación es de **solo lectura**
- No se almacenan datos sensibles
- Los datos se cargan desde el archivo Excel local
- No hay base de datos externa

---

## 📞 Soporte

Si tienes problemas:
1. Verifica que Python 3.9+ esté instalado
2. Asegúrate de que todas las dependencias estén instaladas
3. Verifica que el archivo Excel tenga el formato correcto
4. Revisa los logs de error en la terminal 