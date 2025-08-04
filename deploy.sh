#!/bin/bash

# Script de despliegue para la aplicación de consulta de saldo
echo "🚀 Preparando despliegue de la aplicación de consulta de saldo..."

# Verificar que estamos en el directorio correcto
if [ ! -f "app.py" ]; then
    echo "❌ Error: No se encontró app.py. Asegúrate de estar en el directorio correcto."
    exit 1
fi

# Verificar que git esté instalado
if ! command -v git &> /dev/null; then
    echo "❌ Error: Git no está instalado. Por favor instala Git primero."
    exit 1
fi

# Inicializar repositorio git si no existe
if [ ! -d ".git" ]; then
    echo "📁 Inicializando repositorio Git..."
    git init
fi

# Agregar todos los archivos
echo "📝 Agregando archivos al repositorio..."
git add .

# Hacer commit
echo "💾 Haciendo commit de los cambios..."
git commit -m "Deploy: Aplicación de consulta de saldo para sodería"

# Configurar rama principal
git branch -M main

echo ""
echo "✅ Preparación completada!"
echo ""
echo "📋 Próximos pasos:"
echo "1. Crea un repositorio en GitHub: https://github.com/new"
echo "2. Ejecuta estos comandos (reemplaza 'tu-usuario' y 'tu-repo'):"
echo ""
echo "   git remote add origin https://github.com/tu-usuario/tu-repo.git"
echo "   git push -u origin main"
echo ""
echo "3. Despliega en Railway:"
echo "   - Ve a https://railway.app"
echo "   - Conecta tu repositorio GitHub"
echo "   - Agrega variable: FLASK_ENV=production"
echo ""
echo "4. Comparte la URL con tus clientes!"
echo ""
echo "📖 Para más detalles, consulta: DESPLIEGUE_WEB.md" 