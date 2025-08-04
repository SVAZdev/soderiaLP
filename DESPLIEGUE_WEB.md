# 🌐 Despliegue Web - Consulta de Saldo Sodería

## 🚀 Opciones de Despliegue Gratuito

### 1. **Railway** (Recomendado - Más fácil)
Railway es una plataforma moderna y fácil de usar.

#### Pasos:
1. **Crear cuenta en Railway:**
   - Ve a [railway.app](https://railway.app)
   - Regístrate con GitHub

2. **Conectar repositorio:**
   - Haz clic en "New Project"
   - Selecciona "Deploy from GitHub repo"
   - Conecta tu repositorio

3. **Configurar variables de entorno:**
   - En Railway, ve a "Variables"
   - Agrega: `FLASK_ENV=production`

4. **Desplegar:**
   - Railway detectará automáticamente que es una app Python
   - Se desplegará automáticamente

#### URL resultante:
```
https://tu-app.railway.app
```

---

### 2. **Render** (Alternativa gratuita)
Render ofrece hosting gratuito para aplicaciones web.

#### Pasos:
1. **Crear cuenta en Render:**
   - Ve a [render.com](https://render.com)
   - Regístrate

2. **Crear nuevo servicio:**
   - "New Web Service"
   - Conecta tu repositorio GitHub

3. **Configurar:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn wsgi:app`
   - **Environment:** `FLASK_ENV=production`

4. **Desplegar:**
   - Render construirá y desplegará automáticamente

#### URL resultante:
```
https://tu-app.onrender.com
```

---

### 3. **Heroku** (Tradicional)
Heroku es una opción establecida pero requiere tarjeta de crédito.

#### Pasos:
1. **Instalar Heroku CLI:**
   ```bash
   # macOS
   brew install heroku/brew/heroku
   ```

2. **Login y crear app:**
   ```bash
   heroku login
   heroku create tu-soderia-app
   ```

3. **Configurar variables:**
   ```bash
   heroku config:set FLASK_ENV=production
   ```

4. **Desplegar:**
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

#### URL resultante:
```
https://tu-soderia-app.herokuapp.com
```

---

## 📁 Preparación del Repositorio

### 1. **Crear repositorio en GitHub:**
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/tu-usuario/soderia-saldo.git
git push -u origin main
```

### 2. **Verificar archivos necesarios:**
```
SoderiaLP/
├── app.py              ✅
├── wsgi.py             ✅
├── config.py           ✅
├── requirements.txt    ✅
├── Procfile            ✅
├── runtime.txt         ✅
├── clientes.xlsx       ✅
├── templates/          ✅
├── static/             ✅
└── README.md           ✅
```

---

## 🔧 Configuración para Producción

### Variables de Entorno Recomendadas:
```bash
FLASK_ENV=production
SECRET_KEY=tu-clave-secreta-muy-segura
PORT=5000
```

### Actualizar clientes.xlsx:
- **Sube el archivo actualizado** a tu repositorio
- **O usa una base de datos** para datos dinámicos

---

## 📱 Acceso Público

Una vez desplegado, los clientes podrán:

1. **Acceder desde cualquier dispositivo:**
   - Computadora
   - Celular
   - Tablet

2. **Buscar por:**
   - Número de teléfono
   - Dirección
   - Nombre

3. **Ver su saldo y enviar WhatsApp**

---

## 🔄 Actualización de Datos

### Opción 1: Archivo Excel (Actual)
- Edita `clientes.xlsx` localmente
- Haz commit y push al repositorio
- La plataforma se actualizará automáticamente

### Opción 2: Base de Datos (Futuro)
- Migrar a SQLite o PostgreSQL
- Panel de administración web
- Actualización en tiempo real

---

## 🛡️ Seguridad

### Recomendaciones:
- ✅ **Cambia la SECRET_KEY** en producción
- ✅ **Usa HTTPS** (automático en Railway/Render)
- ✅ **No subas datos sensibles** al repositorio
- ✅ **Configura variables de entorno** para secretos

### Para datos sensibles:
```bash
# En lugar de hardcodear en el código
DATABASE_URL=postgresql://user:pass@host:port/db
SECRET_KEY=tu-clave-super-secreta
```

---

## 📊 Monitoreo

### Métricas a revisar:
- **Uptime:** Tiempo de actividad
- **Response time:** Velocidad de respuesta
- **Error rate:** Tasa de errores
- **Traffic:** Número de visitas

### Logs:
- Revisa los logs de la plataforma
- Monitorea errores 404, 500, etc.
- Verifica búsquedas exitosas

---

## 🆘 Solución de Problemas

### Error: "Application Error"
- Verifica los logs de la plataforma
- Revisa que `requirements.txt` esté correcto
- Confirma que `wsgi.py` existe

### Error: "Module not found"
- Asegúrate de que todas las dependencias estén en `requirements.txt`
- Verifica que `gunicorn` esté incluido

### Error: "Port already in use"
- La plataforma maneja esto automáticamente
- Usa la variable `PORT` del entorno

---

## 🎯 Próximos Pasos

1. **Elegir plataforma** (Railway recomendado)
2. **Crear repositorio GitHub**
3. **Configurar despliegue**
4. **Probar la aplicación**
5. **Compartir URL con clientes**
6. **Monitorear uso**

---

## 📞 Soporte

Si tienes problemas con el despliegue:
1. Revisa la documentación de la plataforma elegida
2. Verifica que todos los archivos estén en el repositorio
3. Revisa los logs de error
4. Confirma que las variables de entorno estén configuradas 