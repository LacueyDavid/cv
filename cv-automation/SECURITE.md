# 🔒 Sécurité et Gestion des Crédits API

## ⚠️ Protection de ta clé API

### 1. Stockage sécurisé

- ✅ La clé est dans `.env` (jamais commitée grâce au `.gitignore`)
- ✅ Utilise `.env.example` pour partager le projet sans exposer la clé
- ❌ **Ne partage JAMAIS** le contenu de `.env`

### 2. Vérifier que .env est ignoré

```bash
# S'assurer que .env n'est pas tracké par git
git status
# .env ne doit PAS apparaître dans la liste
```

Si .env apparaît :

```bash
git rm --cached cv-automation/.env
git commit -m "Remove .env from tracking"
```

## 💰 Gestion des Crédits

### Coûts estimés

- **1 adaptation de CV** : ~0.01-0.05€
- **100 adaptations** : ~1-5€
- Modèle utilisé : `claude-sonnet-4-20250514`

### Configurer des limites de dépenses

1. **Va sur le dashboard Anthropic** : https://console.anthropic.com/settings/billing
2. **Configure un budget mensuel** (ex: 10€/mois)
3. **Active les alertes email** pour être prévenu à 50%, 75%, 90%

### Vérifier ton solde

```bash
# Connecte-toi sur https://console.anthropic.com/settings/billing
# Tu verras :
# - Crédits restants
# - Historique des dépenses
# - Consommation par jour/semaine/mois
```

## 🛡️ Protections intégrées dans le code

### Confirmation avant chaque appel

Le script demande **toujours** confirmation avant d'appeler l'API :

```
⚠️  Attention : Cette opération consomme des crédits API
   Coût estimé : ~0.01-0.05€ par adaptation

Continuer ? (o/n) :
```

### Limites de tokens

- `max_tokens=4096` : Limite la taille de la réponse
- Empêche les coûts excessifs en cas de réponse anormalement longue

### Mode test (sans API)

Si tu veux tester le script sans consommer de crédits, tu peux :

1. **Commenter l'appel API** dans `adapt-cv.py` :

```python
# message = client.messages.create(...)
# À la place, utilise un CV fictif :
adapted_cv = cv_data  # Retourne le CV sans modification
```

2. **Créer un script de test** qui simule les résultats

## 📊 Monitoring de la consommation

### Voir l'historique des appels

Sur https://console.anthropic.com/logs tu peux voir :

- Nombre de requêtes
- Tokens consommés
- Coût par requête
- Date et heure

### Calculer ta consommation

```python
# Dans adapt-cv.py, tu peux afficher les tokens utilisés :
print(f"Tokens utilisés : {message.usage.input_tokens + message.usage.output_tokens}")
```

## 🚨 Que faire en cas de problème ?

### Si ta clé est compromise

1. **Révoque immédiatement** la clé sur https://console.anthropic.com/settings/keys
2. Génère une nouvelle clé
3. Mets à jour `.env` avec la nouvelle clé
4. Change tous les endroits où tu aurais pu partager l'ancienne

### Si tu dépenses trop

1. **Désactive la clé** temporairement
2. Vérifie les logs pour comprendre la consommation
3. Ajuste les limites de budget
4. Réactive avec un nouveau budget

### Si quelqu'un utilise ta clé

- Les clés API sont liées à ton compte
- Configure des **IP whitelisting** si Anthropic le permet
- Active l'authentification 2FA sur ton compte Anthropic

## ✅ Checklist de sécurité

- [ ] `.env` est dans `.gitignore`
- [ ] `.env` n'apparaît jamais dans `git status`
- [ ] Budget mensuel configuré sur Anthropic
- [ ] Alertes email activées
- [ ] Authentification 2FA activée sur le compte Anthropic
- [ ] Clé API stockée uniquement dans `.env` (pas en dur dans le code)
- [ ] Script demande confirmation avant chaque appel API

## 📝 Bonnes pratiques

1. **Vérifie ton solde** avant de lancer plusieurs adaptations
2. **Teste d'abord** avec l'exemple fourni (`example-job-offer.txt`)
3. **Ne lance pas** le script en boucle automatique
4. **Révoque les anciennes clés** si tu en crées de nouvelles
5. **Limite les appels** : adapte ton CV uniquement pour des offres ciblées

## 🔗 Liens utiles

- Dashboard Anthropic : https://console.anthropic.com
- Gestion des clés : https://console.anthropic.com/settings/keys
- Facturation : https://console.anthropic.com/settings/billing
- Tarifs : https://www.anthropic.com/pricing
- Documentation API : https://docs.anthropic.com
