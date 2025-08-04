# 🚂 Configuración Específica para Railway

## ✅ Verificación de Archivos

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

## 🔧 Variables de Entorno en Railway

En Railway, ve a tu proyecto → Variables → Agrega:

```
FLASK_ENV=production
SECRET_KEY=tu-clave-secreta-muy-segura
PORT=5000
```

## 🚀 Comandos de Despliegue

### 1. Verificar repositorio
```bash
git status
git add .
git commit -m "Railway deployment configuration"
git push origin main
```

### 2. En Railway Dashboard:
- Ve a tu proyecto
- Verifica que el repositorio esté conectado
- Revisa los logs de construcción
- Espera a que termine el despliegue

## 🔍 Solución de Problemas

### Error: "Application not found"
1. **Verifica los logs** en Railway Dashboard
2. **Confirma que el repositorio** esté conectado
3. **Espera 2-3 minutos** después del push

### Error: "Module not found"
1. **Verifica requirements.txt** tenga todas las dependencias
2. **Revisa los logs** de construcción
3. **Confirma que gunicorn** esté incluido

### Error: "Port already in use"
- Railway maneja esto automáticamente
- Usa la variable `PORT` del entorno

## 📊 Verificación de Despliegue

### 1. Verificar que la app esté corriendo:
```bash
curl https://web-production-3acd.up.railway.app
```

### 2. Probar la búsqueda:
```bash
curl "https://web-production-3acd.up.railway.app/search?q=2664123456"
```

### 3. Verificar en navegador:
```
https://web-production-3acd.up.railway.app
```

## 🔄 Actualización de Datos

Para actualizar los datos de clientes:

1. **Edita clientes.xlsx** localmente
2. **Haz commit y push:**
   ```bash
   git add clientes.xlsx
   git commit -m "Update customer data"
   git push origin main
   ```
3. **Railway se actualizará** automáticamente

## 📱 URL Final

Una vez desplegada, tu URL será:
```
https://web-production-3acd.up.railway.app
```

## 🆘 Logs de Railway

Para ver los logs:
1. Ve a Railway Dashboard
2. Selecciona tu proyecto
3. Ve a "Deployments"
4. Haz clic en el deployment más reciente
5. Revisa los logs de construcción y ejecución

## ✅ Checklist de Despliegue

- [ ] Repositorio conectado en Railway
- [ ] Variables de entorno configuradas
- [ ] Todos los archivos subidos
- [ ] Despliegue completado sin errores
- [ ] URL accesible desde navegador
- [ ] Búsqueda funcionando
- [ ] WhatsApp links funcionando 