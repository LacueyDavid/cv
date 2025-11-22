#!/bin/bash

# Script pour tester l'adaptation du CV

echo "🧪 Test de l'adaptation du CV"
echo ""

# Charger les variables d'environnement depuis .env si le fichier existe
if [ -f ".env" ]; then
    echo "📄 Chargement du fichier .env..."
    export $(cat .env | grep -v '^#' | xargs)
fi

# Vérifier si la clé API est définie
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "⚠️  ANTHROPIC_API_KEY n'est pas définie"
    echo ""
    echo "Pour utiliser ce script, tu dois d'abord obtenir une clé API Anthropic :"
    echo "1. Va sur https://console.anthropic.com"
    echo "2. Crée un compte et obtiens une clé API"
    echo "3. Ajoute-la dans le fichier .env :"
    echo ""
    echo "   ANTHROPIC_API_KEY=ta-clé-api-ici"
    echo ""
    exit 1
fi

echo "✅ ANTHROPIC_API_KEY trouvée"
echo ""

# Activer l'environnement virtuel
if [ ! -d ".venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv .venv
fi

source .venv/bin/activate

# Vérifier les dépendances
if ! pip show anthropic > /dev/null 2>&1; then
    echo "📥 Installation des dépendances..."
    pip install -r requirements.txt > /dev/null
fi

echo "🚀 Lancement de l'adaptation..."
echo ""

# Tester avec l'exemple d'offre
python adapt-cv.py example-job-offer.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "✨ Adaptation réussie !"
    echo ""
    echo "📄 Fichiers générés :"
    echo "   - src/data/cv-data-adapted.json"
    echo ""
    echo "Tu peux maintenant comparer les deux versions :"
    echo "   diff src/data/cv-data.json src/data/cv-data-adapted.json"
else
    echo ""
    echo "❌ Erreur lors de l'adaptation"
fi

deactivate
