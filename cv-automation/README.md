# CV Automation

🤖 **Système d'adaptation automatique de CV** basé sur l'IA Claude d'Anthropic.

## ⚡ Commandes rapides

```bash
# Installation complète
cd cv-automation
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Tester avec l'exemple
./test-cv-adapter.sh

# Adapter pour une offre spécifique
python adapt-cv.py "Texte de l'offre d'emploi..."
python adapt-cv.py mon-offre.txt
python adapt-cv-from-url.py "https://example.com/job-offer"

# Lancer l'interface web
python cv-adapter-web.py
```

---

## 📋 Qu'est-ce que c'est ?

Ce dossier contient des scripts Python qui utilisent l'API Claude (Anthropic) pour adapter automatiquement ton CV en fonction d'offres d'emploi.

**Principe :**

1. Tu fournis une offre d'emploi (texte ou URL)
2. Claude analyse l'offre et ton CV
3. Il réorganise ton CV pour mettre en avant les compétences/projets pertinents
4. Un nouveau CV adapté est généré

**Important :** Claude ne **modifie jamais** tes vraies compétences ou expériences, il réorganise juste la présentation et l'ordre pour maximiser la pertinence.

## 🚀 Installation rapide

```bash
cd cv-automation

# 1. Créer l'environnement virtuel Python (si pas déjà fait)
python3 -m venv .venv

# 2. Activer l'environnement
source .venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer ta clé API
# Ouvre .env et ajoute ta clé Anthropic
nano .env
```

## 🔑 Configuration de l'API

1. Va sur https://console.anthropic.com
2. Crée un compte (ou connecte-toi)
3. Génère une clé API dans "API Keys"
4. Ajoute-la dans le fichier `.env` :
   ```
   ANTHROPIC_API_KEY=sk-ant-xxxxx
   ```

## 🎯 Utilisation

### Option 1 : Script de test automatique (Recommandé)

```bash
./test-cv-adapter.sh
```

**Ce qu'il fait :**

- ✅ Vérifie la clé API
- ✅ Active l'environnement virtuel
- ✅ Installe les dépendances manquantes
- ✅ Lance l'adaptation avec `example-job-offer.txt`
- ✅ Affiche le résultat

**Sortie :** `../src/data/cv-data-adapted.json`

---

### Option 2 : Script Python avec texte direct

```bash
python adapt-cv.py "Nous recherchons un développeur Python/Django avec expérience Docker et Kubernetes..."
```

**Arguments :**

- `arg1` : Description de l'offre d'emploi (texte)

**Sortie :** `../src/data/cv-data-adapted.json`

**Exemple :**

```bash
python adapt-cv.py "Développeur Full-Stack React/Node.js, expérience en microservices et CI/CD"
```

---

### Option 3 : Script Python avec fichier texte

```bash
python adapt-cv.py mon-offre.txt
```

**Arguments :**

- `arg1` : Chemin vers un fichier `.txt` contenant l'offre

**Format du fichier :**

```
Description de l'offre d'emploi

Nous recherchons un développeur Full-Stack pour rejoindre notre équipe...

Compétences requises :
- Python (Django/Flask)
- React/TypeScript
- Docker
...
```

**Sortie :** `../src/data/cv-data-adapted.json`

---

### Option 4 : Script avec scraping d'URL

```bash
python adapt-cv-from-url.py "https://welcometothejungle.com/fr/companies/..."
```

**Arguments :**

- `arg1` : URL de l'offre d'emploi

**Ce qu'il fait :**

1. Scrappe le contenu de la page web
2. Extrait le texte de l'offre
3. Appelle `adapt-cv.py` avec ce texte

**Sortie :** `../src/data/cv-data-adapted.json`

**Note :** Fonctionne avec la plupart des sites d'emploi (Welcome to the Jungle, LinkedIn, Indeed, etc.)

---

### Option 5 : Interface web

```bash
python cv-adapter-web.py
```

**Ce qu'il fait :**

- Lance un serveur HTTP sur `http://localhost:8080`
- Interface graphique avec 2 onglets :
  - **Par URL** : Colle l'URL d'une offre
  - **Par Texte** : Colle le texte de l'offre

**Sortie :** `../src/data/cv-data-adapted.json`

**Pour arrêter le serveur :** `Ctrl + C`

---

## 📋 Arguments détaillés

### `adapt-cv.py`

```bash
python adapt-cv.py <offre> [cv_path] [output_path]
```

**Arguments positionnels :**

- `<offre>` (requis) : Texte de l'offre OU chemin vers un fichier `.txt`

**Arguments optionnels :**

- `cv_path` : Chemin du CV source (défaut: `../src/data/cv-data.json`)
- `output_path` : Chemin du CV adapté (défaut: `../src/data/cv-data-adapted.json`)

**Exemples :**

```bash
# Avec texte direct
python adapt-cv.py "Offre pour développeur React..."

# Avec fichier
python adapt-cv.py offre.txt

# Avec chemins personnalisés
python adapt-cv.py offre.txt ../src/data/cv-data.json ./mon-cv-adapte.json
```

---

### `adapt-cv-from-url.py`

```bash
python adapt-cv-from-url.py <url> [cv_path] [output_path]
```

**Arguments positionnels :**

- `<url>` (requis) : URL de l'offre d'emploi (doit commencer par `http://` ou `https://`)

**Arguments optionnels :**

- `cv_path` : Chemin du CV source (défaut: `../src/data/cv-data.json`)
- `output_path` : Chemin du CV adapté (défaut: `../src/data/cv-data-adapted.json`)

**Exemples :**

```bash
# Basique
python adapt-cv-from-url.py "https://www.welcometothejungle.com/fr/companies/..."

# Avec chemins personnalisés
python adapt-cv-from-url.py "https://example.com/job" ./cv.json ./cv-out.json
```

---

### `cv-adapter-web.py`

```bash
python cv-adapter-web.py [port]
```

**Arguments optionnels :**

- `port` : Port du serveur (défaut: `8080`)

**Exemple :**

```bash
# Port par défaut (8080)
python cv-adapter-web.py

# Port personnalisé
python cv-adapter-web.py 3001
```

---

## 📁 Fichiers d'entrée et sortie

### Entrée (CV source)

**Fichier :** `../src/data/cv-data.json`

**Structure :**

```json
{
  "personal": { ... },
  "summary": "...",
  "formation": [...],
  "experience": [...],
  "skills": {
    "competences": [...],
    "logiciels": [...]
  },
  "interests": [...]
}
```

### Sortie (CV adapté)

**Fichier :** `../src/data/cv-data-adapted.json`

**Structure :** Identique au CV source, avec :

- Summary optimisé pour l'offre
- Compétences triées par pertinence (max 7)
- Descriptions de projets reformulées (max 20 mots/phrase)
- Ordre des éléments ajusté

**Localisation :**

```
cv/
├── src/
│   └── data/
│       ├── cv-data.json          ← CV original (ne change jamais)
│       └── cv-data-adapted.json  ← CV adapté (généré)
└── cv-automation/
    ├── adapt-cv.py               ← Scripts ici
    └── ...
```

---

## 📂 Structure complète du projet

```
cv/
├── src/
│   ├── data/
│   │   ├── cv-data.json          # ← CV source (INPUT)
│   │   └── cv-data-adapted.json  # ← CV adapté (OUTPUT)
│   └── components/               # Composants React
│
└── cv-automation/                # Scripts d'adaptation
    ├── .env                      # Clés API (NON versionné)
    ├── .env.example              # Template de configuration
    ├── .venv/                    # Environnement virtuel Python
    │
    ├── adapt-cv.py               # ⭐ Script principal
    ├── adapt-cv-from-url.py      # Script avec scraping URL
    ├── cv-adapter-web.py         # Interface web
    ├── test-cv-adapter.sh        # Script de test
    │
    ├── requirements.txt          # Dépendances Python
    ├── example-job-offer.txt     # Offre d'exemple
    │
    ├── README.md                 # Ce fichier
    └── SECURITE.md               # Guide de sécurité
```

---

## 🔄 Workflow typique

### 1. Trouver une offre

```bash
# Copie le texte de l'offre ou récupère l'URL
```

### 2. Adapter le CV

```bash
cd cv-automation

# Option A : Avec texte direct
python adapt-cv.py "Texte de l'offre..."

# Option B : Avec fichier
echo "Texte de l'offre..." > ma-offre.txt
python adapt-cv.py ma-offre.txt

# Option C : Avec URL
python adapt-cv-from-url.py "https://example.com/job"

# Option D : Avec interface web
python cv-adapter-web.py  # Puis ouvre localhost:8080
```

### 3. Vérifier le résultat

```bash
# Le CV adapté est dans :
cat ../src/data/cv-data-adapted.json

# Comparer avec l'original :
diff ../src/data/cv-data.json ../src/data/cv-data-adapted.json
```

### 4. Utiliser le CV adapté

```bash
# Le site React utilise automatiquement cv-data.json
# Pour utiliser le CV adapté, tu peux :

# Option 1 : Copier le CV adapté
cp ../src/data/cv-data-adapted.json ../src/data/cv-data.json

# Option 2 : Modifier l'import dans les composants React
# Changer : import cvData from "../data/cv-data.json"
# En : import cvData from "../data/cv-data-adapted.json"
```

---

## 🎯 Règles d'adaptation de l'IA

Le script envoie ces instructions à Claude :

✅ **Formatage :**

- Maximum **20 mots par phrase** (sauf pour le summary)
- Maximum **7 compétences** dans `skills.competences`
- Phrases courtes et impactantes

✅ **Contenu :**

- Réorganise les compétences par pertinence pour l'offre
- Reformule les descriptions de projets
- Optimise le summary avec mots-clés de l'offre
- Ajuste l'ordre des expériences

❌ **Interdictions :**

- Ne modifie JAMAIS les vraies compétences
- N'invente pas d'expériences
- Garde la structure JSON exacte
- Reste factuel et honnête

---

## 💻 Exemples d'exécution

### Exemple 1 : Adaptation basique

```bash
$ python adapt-cv.py "Recherche développeur Python Django PostgreSQL Docker"

📄 Chargement du CV depuis ../src/data/cv-data.json
🤖 Connexion à Claude API...
⚠️  Attention : Cette opération consomme des crédits API
   Coût estimé : ~0.01-0.05€ par adaptation

Continuer ? (o/n) : o

✨ Adaptation du CV en cours...
✅ CV adapté sauvegardé dans ../src/data/cv-data-adapted.json

📊 Changements principaux:
   - Summary mis à jour
   - 7 compétences réorganisées
   - 3 projets optimisés
```

### Exemple 2 : Scraping d'URL

```bash
$ python adapt-cv-from-url.py "https://www.welcometothejungle.com/fr/companies/..."

🌐 Scraping de l'offre depuis l'URL...
✅ Offre récupérée (1234 caractères)

📄 Chargement du CV depuis ../src/data/cv-data.json
🤖 Connexion à Claude API...
⚠️  Attention : Cette opération consomme des crédits API
   Coût estimé : ~0.01-0.05€ par adaptation

Continuer ? (o/n) : o

✨ Adaptation du CV en cours...
✅ CV adapté sauvegardé dans ../src/data/cv-data-adapted.json
```

### Exemple 3 : Interface web

```bash
$ python cv-adapter-web.py

🌐 Serveur CV Adapter démarré sur http://localhost:8080
   Appuyez sur Ctrl+C pour arrêter

# Dans le navigateur :
# 1. Ouvre http://localhost:8080
# 2. Onglet "Par URL" ou "Par Texte"
# 3. Colle l'offre
# 4. Clique "Adapter mon CV"
# 5. Le CV adapté est généré
```

---

## 🛠️ Technologies utilisées

- **Python 3.14** - Langage de base
- **Anthropic Claude API** - IA pour l'adaptation (modèle `claude-sonnet-4-20250514`)
- **python-dotenv** - Gestion des variables d'environnement
- **requests + BeautifulSoup4** - Scraping d'offres depuis URLs
- **http.server** - Interface web simple

---

## 🐛 Dépannage

### Erreur "No module named 'anthropic'"

```bash
cd cv-automation
source .venv/bin/activate
pip install -r requirements.txt
```

### Erreur "ANTHROPIC_API_KEY non définie"

Vérifie que le fichier `.env` existe et contient :

```
ANTHROPIC_API_KEY=sk-ant-xxxxx
```

### Erreur "credit balance is too low"

Ajoute des crédits sur https://console.anthropic.com/settings/billing

### Erreur lors du scraping d'URL

Certains sites bloquent les scrapers. Essaie :

1. Copier manuellement le texte de l'offre
2. Utiliser `python adapt-cv.py "texte copié"`

### Le CV adapté est identique à l'original

- Vérifie que l'offre contient des compétences/technologies spécifiques
- Augmente le niveau de détail de l'offre

---

## 📚 Ressources

- **Documentation API Anthropic** : https://docs.anthropic.com
- **Dashboard Anthropic** : https://console.anthropic.com
- **Tarifs** : https://www.anthropic.com/pricing
- **Sécurité** : Voir `SECURITE.md`

---

## 📝 Notes importantes

⚠️ **Le CV original n'est JAMAIS modifié**

- Fichier source : `../src/data/cv-data.json`
- Fichier adapté : `../src/data/cv-data-adapted.json`

💰 **Coûts**

- ~0.01-0.05€ par adaptation
- Confirmation demandée avant chaque appel API
- Configure des limites sur https://console.anthropic.com/settings/billing

🔒 **Sécurité**

- Le fichier `.env` est dans `.gitignore`
- Ne commit JAMAIS ta clé API
- Révoque la clé si elle est compromise

---

## 🤝 Support

Pour toute question :

1. Lis d'abord `SECURITE.md`
2. Vérifie les logs d'erreur
3. Teste avec `./test-cv-adapter.sh`

## 🔄 Workflow typique

1. **Trouver une offre** qui t'intéresse
2. **Lancer l'adaptation :**
   ```bash
   python adapt-cv.py "texte de l'offre"
   ```
3. **Vérifier le résultat** dans `../src/data/cv-data-adapted.json`
4. **Utiliser le CV adapté** pour ta candidature
5. **Comparer les changements** (optionnel) :
   ```bash
   diff ../src/data/cv-data.json ../src/data/cv-data-adapted.json
   ```

## 🛠️ Technologies utilisées

- **Python 3.14** - Langage de base
- **Anthropic Claude API** - IA pour l'adaptation intelligente (modèle `claude-sonnet-4`)
- **python-dotenv** - Gestion des variables d'environnement
- **requests + BeautifulSoup4** - Scraping d'offres depuis URLs
- **http.server** - Interface web simple

## 💡 Comment ça fonctionne ?

1. **Lecture du CV** : Charge `../src/data/cv-data.json`
2. **Analyse de l'offre** : Parse le texte de l'offre d'emploi
3. **Appel API Claude** : Envoie CV + offre avec un prompt optimisé
4. **Adaptation intelligente** :
   - Réorganise le summary pour mentionner les compétences clés
   - Priorise les compétences techniques demandées
   - Met en avant les projets pertinents
   - Ajoute des mots-clés de l'offre de manière naturelle
5. **Sauvegarde** : Génère `../src/data/cv-data-adapted.json`

## 🔒 Sécurité

- ✅ Le fichier `.env` est dans `.gitignore` - tes clés API ne seront jamais commitées
- ✅ Utilise `.env.example` comme template pour partager le projet
- ✅ L'environnement virtuel (`.venv/`) est isolé du système

## 💰 Coûts

L'API Claude n'est pas gratuite mais reste abordable :

- Offre d'essai avec crédits gratuits au démarrage
- Tarification à l'usage ensuite
- Un CV adapté coûte quelques centimes

Consulte https://www.anthropic.com/pricing pour les tarifs actuels.

## 🐛 Dépannage

**Erreur "No module named 'anthropic'" :**

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

**Erreur "ANTHROPIC_API_KEY non définie" :**
Vérifie que le fichier `.env` contient bien ta clé API.

**Erreur "credit balance is too low" :**
Ajoute des crédits sur https://console.anthropic.com/settings/billing

## 📝 Notes

- Le CV original (`../src/data/cv-data.json`) n'est **jamais modifié**
- Tous les CV adaptés sont sauvegardés dans `../src/data/cv-data-adapted.json`
- Tu peux adapter ton CV autant de fois que tu veux pour différentes offres
