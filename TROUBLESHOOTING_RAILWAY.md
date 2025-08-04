# 🔧 Solución de Problemas - Railway Deployment

## 🚨 Error Actual: "Application not found"

El error `{"status":"error","code":404,"message":"Application not found"}` indica que Railway no puede encontrar o ejecutar la aplicación.

## 🔍 Pasos de Diagnóstico

### 1. Verificar Railway Dashboard

1. **Ve a [railway.app](https://railway.app)**
2. **Selecciona tu proyecto**
3. **Ve a la pestaña "Deployments"**
4. **Revisa el deployment más reciente**

### 2. Verificar Logs de Construcción

En Railway Dashboard:
- Haz clic en el deployment más reciente
- Ve a "Build Logs"
- Busca errores como:
  - `ModuleNotFoundError`
  - `ImportError`
  - `FileNotFoundError`

### 3. Verificar Logs de Ejecución

En Railway Dashboard:
- Ve a "Runtime Logs"
- Busca errores como:
  - `Port already in use`
  - `Address already in use`
  - `Permission denied`

## 🛠️ Soluciones Comunes

### Problema 1: Repositorio no conectado

**Síntomas:** No hay deployments en Railway

**Solución:**
1. En Railway, ve a "New Project"
2. Selecciona "Deploy from GitHub repo"
3. Conecta tu repositorio: `SVAZdev/soderiaLP`

### Problema 2: Variables de entorno faltantes

**Síntomas:** App se construye pero no inicia

**Solución:**
En Railway → Variables → Agrega:
```
FLASK_ENV=production
SECRET_KEY=tu-clave-secreta-aqui
PORT=5000
```

### Problema 3: Dependencias faltantes

**Síntomas:** Error de módulo no encontrado

**Solución:**
Verifica que `requirements.txt` contenga:
```
Flask==3.1.1
pandas==2.3.0
openpyxl==3.1.5
Werkzeug==3.1.3
gunicorn==21.2.0
```

### Problema 4: Archivo wsgi.py incorrecto

**Síntomas:** App no inicia

**Solución:**
Verifica que `wsgi.py` contenga:
```python
import os
from app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
```

### Problema 5: Procfile incorrecto

**Síntomas:** Railway no sabe cómo iniciar la app

**Solución:**
Verifica que `Procfile` contenga:
```
web: gunicorn wsgi:app
```

## 🔄 Re-deploy Manual

Si los problemas persisten:

1. **En Railway Dashboard:**
   - Ve a tu proyecto
   - Haz clic en "Deployments"
   - Busca "Redeploy" o "Manual Deploy"

2. **O fuerza un nuevo deploy:**
   ```bash
   git commit --allow-empty -m "Force redeploy"
   git push origin main
   ```

## 📊 Verificación de Archivos

Asegúrate de que estos archivos estén en tu repositorio:

```
✅ app.py
✅ wsgi.py
✅ requirements.txt
✅ Procfile
✅ railway.json
✅ runtime.txt
✅ clientes.xlsx
✅ templates/index.html
✅ static/style.css
```

## 🆘 Contacto con Railway

Si nada funciona:

1. **Revisa la documentación:** [docs.railway.app](https://docs.railway.app)
2. **Únete al Discord:** [railway.app/discord](https://railway.app/discord)
3. **Abre un ticket:** Desde Railway Dashboard

## 🔄 Alternativa: Render

Si Railway sigue dando problemas, puedes usar Render:

1. Ve a [render.com](https://render.com)
2. Crea un nuevo "Web Service"
3. Conecta tu repositorio GitHub
4. Configura:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn wsgi:app`
   - **Environment:** `FLASK_ENV=production`

## 📱 URL de Verificación

Una vez solucionado, verifica:
```
https://web-production-3acd.up.railway.app
```

## ✅ Checklist de Verificación

- [ ] Repositorio conectado en Railway
- [ ] Variables de entorno configuradas
- [ ] Todos los archivos subidos
- [ ] Build logs sin errores
- [ ] Runtime logs sin errores
- [ ] URL accesible
- [ ] Búsqueda funcionando 