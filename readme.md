
# 💧 Web de Consulta de Saldo para una Sodería

Este es un proyecto web simple que permite a los clientes de una sodería consultar su saldo ingresando su **número de teléfono** o **dirección**. La información de los saldos se carga desde un archivo Excel.

---

## ✅ Funcionalidad principal

- Los usuarios ingresan su **número** o **dirección** en un campo de búsqueda.
- Si hay coincidencia, el sistema muestra el **nombre del cliente y su saldo**.
- También se muestra un botón para enviar un mensaje por **WhatsApp** al número registrado.
- Si no hay coincidencias, muestra un mensaje adecuado ("No se encontró ningún cliente").

---

## 📁 Formato del archivo Excel (`clientes.xlsx`)

El archivo debe estar en la raíz del proyecto y tener estas columnas:

| nombre      | numero       | direccion        | saldo   |
|-------------|--------------|------------------|---------|
| Juan Pérez  | 2664123456   | Mitre 123        | 2500.00 |
| Ana Gómez   | 2664123457   | Belgrano 456     | 1500.00 |

- `numero`: sin código de país (solo el número local).
- `direccion`: dirección del cliente.
- `saldo`: en pesos argentinos.

---

## 🧑‍💻 Tecnologías a usar

- **Frontend**: HTML, CSS, JavaScript (puede usar Tailwind o Bootstrap)
- **Backend**: Python con **Flask**
- **Lectura de Excel**: `pandas` y `openpyxl`

---

## 🔗 Enlace de WhatsApp

Usar esta estructura para generar el botón:

```

[https://wa.me/549\[número\]?text=Hola%20\[nombre\]%2C%20tu%20saldo%20es%20de%20$\[saldo](https://wa.me/549[número]?text=Hola%20[nombre]%2C%20tu%20saldo%20es%20de%20$[saldo)]

```

Ejemplo:

```

[https://wa.me/5492664123456?text=Hola%20Juan%2C%20tu%20saldo%20es%20de%20\$2500](https://wa.me/5492664123456?text=Hola%20Juan%2C%20tu%20saldo%20es%20de%20$2500)

````

---

## 🧠 Requisitos

- Python 3.9+
- Flask
- Pandas
- openpyxl

---

## ▶️ Cómo ejecutarlo

### 🖥️ Desarrollo Local

1. Instalar dependencias:

```bash
python3 -m pip install Flask pandas openpyxl
```

2. Ejecutar el servidor:

```bash
python3 app.py
```

3. Abrir en el navegador:

```
http://localhost:5001
```

### 🌐 Despliegue Web (Para clientes)

Para que los clientes puedan acceder desde cualquier lugar:

1. **Despliegue rápido:**
   ```bash
   ./deploy.sh
   ```

2. **Seguir las instrucciones** en `DESPLIEGUE_WEB.md`

3. **Resultado:** URL pública como `https://tu-app.railway.app`

---

## 📂 Estructura del proyecto

```
SoderiaLP/
├── app.py              # Servidor Flask principal
├── wsgi.py             # Punto de entrada para producción
├── config.py           # Configuración de entornos
├── clientes.xlsx       # Datos de clientes
├── requirements.txt    # Dependencias Python
├── Procfile            # Configuración para Heroku/Railway
├── runtime.txt         # Versión de Python
├── deploy.sh           # Script de despliegue automático
├── .gitignore          # Archivos a ignorar en Git
├── templates/
│   └── index.html      # Interfaz web
├── static/
│   └── style.css       # Estilos CSS
├── readme.md           # Documentación principal
├── INSTRUCCIONES.md    # Guía de uso detallada
└── DESPLIEGUE_WEB.md   # Guía de despliegue web
```

---

## 📝 Extras

* La búsqueda debe ignorar mayúsculas y minúsculas.
* Si hay más de una coincidencia (ej. varios con la misma dirección), mostrar todos los resultados.

```

