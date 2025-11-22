#!/usr/bin/env python3
"""
Script pour adapter automatiquement le CV JSON en fonction d'une offre d'emploi
"""

import json
import anthropic
import sys
import os
from dotenv import load_dotenv
from datetime import datetime

# Charger les variables d'environnement depuis .env
load_dotenv()


def generate_unique_output_path(base_path: str) -> str:
    """
    Génère un nom de fichier unique en ajoutant un timestamp
    
    Args:
        base_path: Chemin de base (ex: ../src/data/cv-data-adapted.json)
    
    Returns:
        Chemin unique (ex: ../src/data/cv-data-adapted-20250122-143052.json)
    """
    directory = os.path.dirname(base_path)
    filename = os.path.basename(base_path)
    name, ext = os.path.splitext(filename)
    
    # Générer un timestamp
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    
    # Créer le nouveau nom
    unique_filename = f"{name}-{timestamp}{ext}"
    unique_path = os.path.join(directory, unique_filename)
    
    return unique_path


def adapt_cv_to_job(
    job_description: str,
    cv_path: str = "../src/data/cv-data.json",
    output_path: str = "../src/data/cv-data-adapted.json"
):
    """
    Adapte le CV JSON en fonction d'une annonce d'emploi

    Args:
        job_description: Texte de l'offre d'emploi
        cv_path: Chemin vers le CV JSON original
        output_path: Chemin où sauvegarder le CV adapté

    Returns:
        Le CV adapté (dict)
    """

    # Vérifier que le fichier CV existe
    if not os.path.exists(cv_path):
        print(f"❌ Erreur: Le fichier {cv_path} n'existe pas")
        sys.exit(1)

    # Charger le CV actuel
    print(f"📄 Chargement du CV depuis {cv_path}")
    with open(cv_path, 'r', encoding='utf-8') as f:
        cv_data = json.load(f)

    # Récupérer la clé API depuis la variable d'environnement
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print(
            "❌ Erreur: Variable d'environnement "
            "ANTHROPIC_API_KEY non définie"
        )
        print("   Exécutez: export ANTHROPIC_API_KEY='votre-clé-api'")
        sys.exit(1)

    # Initialiser Claude
    print("🤖 Connexion à Claude API...")
    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""Tu es un expert en recrutement et optimisation de CV.

Voici un CV au format JSON et une offre d'emploi.

Adapte le CV pour MAXIMISER la correspondance avec l'offre en :

1. **SUMMARY** : Réécrire pour mettre en avant UNIQUEMENT les compétences
   demandées dans l'offre. Utiliser les mots-clés exacts de l'offre.

2. **COMPÉTENCES (skills.competences)** :
   - Sélectionner les 7 compétences les PLUS pertinentes pour l'offre
   - Si une compétence de l'offre correspond à plusieurs compétences du CV,
     regrouper sous le nom utilisé dans l'offre
   - Ordre : compétences les plus demandées en premier
   - Supprimer les compétences non pertinentes pour l'offre

3. **PROJETS (experience.projects)** :
   - Reformuler les descriptions pour mettre en avant les
     technologies/compétences demandées dans l'offre
   - Ajouter les mots-clés techniques de l'offre naturellement
   - Réorganiser l'ordre des projets : les plus pertinents en premier

4. **LOGICIELS (skills.logiciels)** :
   - Prioriser les outils mentionnés dans l'offre
   - Ajouter les outils de l'offre s'ils sont cohérents avec l'expérience

RÈGLES IMPORTANTES:
- Garde EXACTEMENT la même structure JSON
- Tu peux reformuler et adapter les compétences existantes pour matcher l'offre
- INTERDICTION d'inventer des compétences totalement nouvelles
- Si l'offre demande "React" et que le CV a "React", mets "React" en priorité
- Si l'offre demande "CI/CD" et que le CV a "Docker/Git", reformule pour
  mentionner "CI/CD avec Docker et Git"
- Reste factuel mais optimise la présentation pour matcher l'offre
- Retourne UNIQUEMENT le JSON complet, sans commentaires ni texte autour

RÈGLES DE FORMATAGE:
- Maximum 25 mots pour les descriptions dans "experience.projects"
- Maximum 25 mots pour les descriptions dans "interests.hobbies"
- Le champ "summary" peut être plus long (pas de limite stricte)
- Dans "skills.competences" : EXACTEMENT 7 compétences (les plus pertinentes)
- Phrases courtes et impactantes
- Utiliser la terminologie EXACTE de l'offre d'emploi

OBJECTIF FINAL:
Le recruteur doit voir IMMÉDIATEMENT que le candidat correspond parfaitement
à l'offre. Chaque compétence, chaque mot-clé de l'offre doit se retrouver
dans le CV adapté.

CV ACTUEL:
{json.dumps(cv_data, ensure_ascii=False, indent=2)}

OFFRE D'EMPLOI:
{job_description}

Retourne le CV adapté en JSON :"""

    # Afficher un avertissement sur les coûts
    print("⚠️  Attention : Cette opération consomme des crédits API")
    print("   Coût estimé : ~0.01-0.05€ par adaptation")
    print("")
    
    # Demander confirmation
    confirm = input("Continuer ? (o/n) : ").lower()
    if confirm not in ['o', 'oui', 'y', 'yes']:
        print("❌ Opération annulée")
        sys.exit(0)

    # Appeler Claude
    print("\n✨ Adaptation du CV en cours...")
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # Extraire le JSON de la réponse
    response_text = message.content[0].text

    # Nettoyer la réponse (enlever les markdown code blocks si présents)
    if "```json" in response_text:
        response_text = response_text.split("```json")[1].split("```")[0]
    elif "```" in response_text:
        response_text = response_text.split("```")[1].split("```")[0]

    # Parser le JSON
    try:
        adapted_cv = json.loads(response_text.strip())
    except json.JSONDecodeError as e:
        print(f"❌ Erreur lors du parsing JSON: {e}")
        print("Réponse reçue:")
        print(response_text[:500])
        sys.exit(1)

    # Générer un nom de fichier unique
    unique_output_path = generate_unique_output_path(output_path)

    # Sauvegarder le CV adapté
    with open(unique_output_path, 'w', encoding='utf-8') as f:
        json.dump(adapted_cv, f, ensure_ascii=False, indent=2)

    print(f"✅ CV adapté sauvegardé dans {unique_output_path}")
    print("\n📊 Changements principaux:")
    print("   - Summary mis à jour")
    num_skills = len(adapted_cv.get('skills', {}).get('competences', []))
    print(f"   - {num_skills} compétences réorganisées")
    exp = adapted_cv.get('experience', [])
    num_projects = len(exp[0].get('projects', [])) if exp else 0
    print(f"   - {num_projects} projets optimisés")

    return adapted_cv


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python adapt-cv.py 'description de l'offre'")
        print("  python adapt-cv.py job-description.txt")
        print("\nExemple:")
        print(
            "  python adapt-cv.py "
            "'Nous recherchons un développeur Python/Django...'"
        )
        print("\nNote: Définir ANTHROPIC_API_KEY dans l'environnement")
        sys.exit(1)

    job_input = sys.argv[1]

    # Si c'est un fichier, le lire
    if job_input.endswith('.txt') and os.path.exists(job_input):
        print(f"📖 Lecture de l'offre depuis {job_input}")
        with open(job_input, 'r', encoding='utf-8') as f:
            job_description = f.read()
    else:
        job_description = job_input

    adapt_cv_to_job(job_description)
