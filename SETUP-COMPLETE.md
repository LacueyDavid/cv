# CV Adapter - Installation et Test

## ✅ Installation terminée !

Les dépendances Python sont installées dans l'environnement virtuel `venv/`.

## 🔑 Configuration requise

Pour utiliser les scripts, tu dois obtenir une clé API Anthropic (Claude) :

1. **Créer un compte** sur https://console.anthropic.com
2. **Obtenir une clé API** (section API Keys)
3. **Définir la variable d'environnement** :

```bash
export ANTHROPIC_API_KEY='ta-clé-api-ici'
```

Ou l'ajouter de manière permanente dans ton `~/.zshrc` :

```bash
echo 'export ANTHROPIC_API_KEY="ta-clé-api-ici"' >> ~/.zshrc
source ~/.zshrc
```

## 🧪 Test rapide

Une fois la clé API configurée, lance :

```bash
./test-cv-adapter.sh
```

Ou manuellement :

```bash
source venv/bin/activate
python3 adapt-cv.py example-job-offer.txt
```

## 📝 Utilisation

### 1. Avec texte direct

```bash
source venv/bin/activate
python3 adapt-cv.py "Nous recherchons un développeur Python..."
```

### 2. Avec un fichier texte

```bash
source venv/bin/activate
python3 adapt-cv.py job-offer.txt
```

### 3. Avec une URL

```bash
source venv/bin/activate
python3 adapt-cv-from-url.py "https://welcometothejungle.com/..."
```

### 4. Interface web

```bash
source venv/bin/activate
python3 cv-adapter-web.py
# Puis ouvre http://localhost:8080
```

## 📂 Fichiers générés

Après adaptation, tu trouveras :

- `src/data/cv-data-adapted.json` - Ton CV adapté
- `last-job-offer.txt` - La dernière offre analysée (si URL)

## 💡 Prochaines étapes

1. Configure ta clé API Anthropic
2. Lance le test : `./test-cv-adapter.sh`
3. Compare les résultats : `diff src/data/cv-data.json src/data/cv-data-adapted.json`
4. Utilise le CV adapté dans ton application React

## 📖 Documentation complète

Voir `README-CV-ADAPTER.md` pour plus de détails.
