#!/usr/bin/env python3
"""
Script pour adapter le CV en scrapant une offre d'emploi depuis une URL
"""

import sys
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from adapt_cv import adapt_cv_to_job

# Charger les variables d'environnement depuis .env
load_dotenv()


def scrape_job_offer(url: str) -> str:
    """
    Scrape le contenu d'une offre d'emploi depuis une URL

    Args:
        url: URL de l'offre d'emploi

    Returns:
        Le texte de l'offre nettoyé
    """
    print(f"🌐 Récupération de la page {url}")

    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/91.0.4472.124 Safari/537.36'
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur lors de la récupération de l'URL: {e}")
        sys.exit(1)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Enlever scripts, styles, et autres éléments non pertinents
    for element in soup(["script", "style", "nav", "footer", "header"]):
        element.decompose()

    # Extraire le texte
    text = soup.get_text(separator='\n', strip=True)

    # Nettoyer les lignes vides multiples
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    clean_text = '\n'.join(lines)

    print(f"✅ Offre récupérée ({len(clean_text)} caractères)")

    return clean_text


def adapt_cv_from_url(
    job_url: str,
    cv_path: str = "../src/data/cv-data.json",
    output_path: str = "../src/data/cv-data-adapted.json"
):
    """
    Adapte le CV à partir d'une URL d'offre d'emploi

    Args:
        job_url: URL de l'offre d'emploi
        cv_path: Chemin vers le CV JSON original
        output_path: Chemin où sauvegarder le CV adapté
    """

    # Scraper l'offre
    job_description = scrape_job_offer(job_url)

    # Sauvegarder l'offre pour référence
    offer_file = "last-job-offer.txt"
    with open(offer_file, 'w', encoding='utf-8') as f:
        f.write(f"URL: {job_url}\n\n")
        f.write(job_description)
    print(f"💾 Offre sauvegardée dans {offer_file}")

    # Adapter le CV
    adapt_cv_to_job(job_description, cv_path, output_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print(
            "  python adapt-cv-from-url.py "
            "https://example.com/job-offer"
        )
        print("\nExemple:")
        print(
            "  python adapt-cv-from-url.py "
            "'https://welcometothejungle.com/fr/companies/...'"
        )
        print("\nNote: Définir ANTHROPIC_API_KEY dans l'environnement")
        sys.exit(1)

    job_url = sys.argv[1]

    # Vérifier que c'est bien une URL
    if not job_url.startswith(('http://', 'https://')):
        print(
            "❌ Erreur: Veuillez fournir une URL valide "
            "(commençant par http:// ou https://)"
        )
        sys.exit(1)

    adapt_cv_from_url(job_url)
