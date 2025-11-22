# CV - Portfolio Web

Site web de CV personnel développé en React/TypeScript avec Tailwind CSS.

[Voir le PDF](./cv_lacuey_david_compressed.pdf)

## 🚀 Démarrage rapide

```bash
# Installer les dépendances
npm install

# Lancer en développement
npm start

# Builder pour production
npm run build
```

## 📂 Structure du projet

```
cv/
├── src/
│   ├── components/        # Composants React
│   │   ├── HardSkills.tsx
│   │   ├── WhoAmI.tsx
│   │   └── ...
│   ├── data/
│   │   ├── cv-data.json          # CV original
│   │   └── cv-data-adapted.json  # CV adapté par l'IA (généré)
│   ├── img/               # Images et assets
│   └── App.tsx
├── cv-automation/         # Scripts Python d'adaptation IA (voir README dédié)
└── public/
```

## 📝 Données du CV

Le CV est centralisé dans `src/data/cv-data.json` :

- **cv-data.json** : Version originale du CV
- **cv-data-adapted.json** : Version adaptée automatiquement par l'IA (optionnel)

Pour modifier le contenu du CV, édite directement `src/data/cv-data.json`.

## 🤖 Adaptation automatique du CV

Ce projet inclut un système d'adaptation automatique du CV basé sur l'IA Claude.

👉 **Voir le dossier [`cv-automation/`](./cv-automation/README.md) pour plus de détails.**

En bref :

- Place une offre d'emploi dans un fichier texte
- Lance le script d'adaptation
- Un CV optimisé pour cette offre est généré dans `src/data/cv-data-adapted.json`

## 🛠️ Technologies

### Frontend (ce dossier)

- React 18
- TypeScript
- Tailwind CSS
- Cypress (tests)

### Backend/Automation (dossier cv-automation/)

- Python 3.14
- Claude AI (Anthropic)
- BeautifulSoup4
- python-dotenv

## 📄 License

Projet personnel
