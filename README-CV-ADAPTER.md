# 🤖 CV Adapter

Adapte automatiquement ton CV JSON en fonction d'une offre d'emploi en utilisant Claude AI.

## 📋 Prérequis

1. **Python 3.7+**
2. **Clé API Anthropic (Claude)**
   - Créer un compte sur https://console.anthropic.com
   - Obtenir une clé API
   - Définir la variable d'environnement :
     ```bash
     export ANTHROPIC_API_KEY='ta-clé-api-ici'
     ```
     Ou ajouter dans ton `.zshrc` / `.bashrc` :
     ```bash
     echo 'export ANTHROPIC_API_KEY="ta-clé-api-ici"' >> ~/.zshrc
     source ~/.zshrc
     ```

## 🚀 Installation

```bash
# Installer les dépendances
pip install -r requirements.txt

# Ou avec pip3
pip3 install -r requirements.txt
```

## 💻 Utilisation

### Option 1 : Ligne de commande (texte direct)

```bash
# Avec le texte de l'offre directement
python adapt-cv.py "Nous recherchons un développeur Python/Django avec expérience Docker..."

# Avec un fichier texte
python adapt-cv.py job-offer.txt
```

Le CV adapté sera sauvegardé dans `src/data/cv-data-adapted.json`

### Option 2 : Depuis une URL

```bash
# Scrape automatiquement l'offre depuis une URL
python adapt-cv-from-url.py "https://welcometothejungle.com/fr/companies/..."

# Fonctionne aussi avec LinkedIn, Indeed, etc.
python adapt-cv-from-url.py "https://www.linkedin.com/jobs/view/..."
```

### Option 3 : Interface web

```bash
# Lancer l'interface web
python cv-adapter-web.py
```

Ouvre ton navigateur sur http://localhost:8080

L'interface te permet de :

- Coller une URL d'offre
- Coller directement le texte de l'offre
- Adapter ton CV en un clic

## 📂 Structure des fichiers

```
cv/
├── adapt-cv.py              # Script principal
├── adapt-cv-from-url.py     # Script avec scraping d'URL
├── cv-adapter-web.py        # Interface web
├── requirements.txt         # Dépendances Python
├── src/
│   └── data/
│       ├── cv-data.json           # Ton CV original
│       └── cv-data-adapted.json   # CV adapté généré
└── last-job-offer.txt       # Dernière offre scrapée (pour référence)
```

## 🎯 Ce que fait l'adaptation

L'IA adapte ton CV en :

1. **Réécrivant le summary** pour mentionner les compétences clés de l'offre
2. **Réorganisant les compétences** pour prioriser celles demandées
3. **Reformulant les descriptions de projets** pour mettre en avant les expériences pertinentes
4. **Ajoutant des mots-clés** de l'annonce de manière naturelle

⚠️ **Important** : L'IA ne modifie pas tes vraies compétences/expériences, elle adapte uniquement la présentation !

## 🔄 Workflow complet

1. **Trouver une offre** qui t'intéresse
2. **Adapter le CV** :
   ```bash
   python adapt-cv-from-url.py "URL-de-l-offre"
   ```
3. **Vérifier le résultat** dans `src/data/cv-data-adapted.json`
4. **Utiliser le CV adapté** dans ton application React
5. **Exporter en PDF** pour ta candidature

## 🛠 Intégration avec ton CV React

Pour utiliser le CV adapté au lieu de l'original :

**Option A : Remplacer temporairement**

```bash
cp src/data/cv-data-adapted.json src/data/cv-data.json
```

**Option B : Changer l'import dans ton code**

```typescript
// Dans src/components/*.tsx
import cvData from "../data/cv-data-adapted.json";
```

**Option C : Script npm**

```json
{
  "scripts": {
    "use-adapted": "cp src/data/cv-data-adapted.json src/data/cv-data.json",
    "use-original": "git checkout src/data/cv-data.json"
  }
}
```

## 💡 Conseils

- **Garde ton CV original** (`cv-data.json`) intact
- **Vérifie toujours** le CV adapté avant de l'envoyer
- **Personnalise** encore plus manuellement si nécessaire
- **Sauvegarde** les versions adaptées pour différentes offres

## 🐛 Dépannage

**Erreur "ANTHROPIC_API_KEY non définie"**

```bash
export ANTHROPIC_API_KEY='ta-clé-api'
```

**Erreur d'import de module**

```bash
pip install -r requirements.txt
```

**Erreur de scraping d'URL**

- Certains sites bloquent le scraping
- Dans ce cas, copie/colle le texte manuellement et utilise `adapt-cv.py`

## 📝 Exemples

```bash
# Exemple 1 : URL Welcome to the Jungle
python adapt-cv-from-url.py "https://www.welcometothejungle.com/fr/companies/..."

# Exemple 2 : Texte direct
python adapt-cv.py "Offre: Développeur Full Stack
Compétences: React, Node.js, PostgreSQL, Docker
Expérience avec APIs REST et microservices..."

# Exemple 3 : Fichier texte
cat > offre.txt << EOF
Nous recherchons un développeur passionné...
[texte de l'offre]
EOF
python adapt-cv.py offre.txt
```

## 🎨 Personnalisation

Tu peux modifier le prompt dans `adapt-cv.py` (ligne 34) pour changer le comportement de l'adaptation selon tes préférences.

---

**Astuce** : Utilise Git pour versionner tes différentes adaptations de CV !
