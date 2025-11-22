#!/usr/bin/env python3
"""
Interface web simple pour adapter le CV
Lance un serveur local avec un formulaire
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import os
from dotenv import load_dotenv
from adapt_cv import adapt_cv_to_job
from adapt_cv_from_url import scrape_job_offer

# Charger les variables d'environnement depuis .env
load_dotenv()


class CVAdapterHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Affiche le formulaire HTML"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>CV Adapter</title>
            <style>
                body {
                    font-family: -apple-system, BlinkMacSystemFont,
                        'Segoe UI', sans-serif;
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                    background: #f5f5f5;
                }
                .container {
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }
                h1 {
                    color: #333;
                    margin-bottom: 30px;
                }
                label {
                    display: block;
                    margin: 20px 0 8px;
                    font-weight: 600;
                    color: #555;
                }
                input[type="url"], textarea {
                    width: 100%;
                    padding: 12px;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                    font-size: 14px;
                    box-sizing: border-box;
                }
                textarea {
                    min-height: 200px;
                    font-family: monospace;
                }
                button {
                    background: #007bff;
                    color: white;
                    padding: 12px 30px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 16px;
                    margin-top: 20px;
                }
                button:hover {
                    background: #0056b3;
                }
                .tabs {
                    display: flex;
                    gap: 10px;
                    margin-bottom: 20px;
                    border-bottom: 2px solid #ddd;
                }
                .tab {
                    padding: 10px 20px;
                    cursor: pointer;
                    background: none;
                    border: none;
                    border-bottom: 3px solid transparent;
                    font-size: 16px;
                }
                .tab.active {
                    border-bottom-color: #007bff;
                    color: #007bff;
                }
                .tab-content {
                    display: none;
                }
                .tab-content.active {
                    display: block;
                }
                .success {
                    background: #d4edda;
                    color: #155724;
                    padding: 15px;
                    border-radius: 5px;
                    margin: 20px 0;
                }
                .error {
                    background: #f8d7da;
                    color: #721c24;
                    padding: 15px;
                    border-radius: 5px;
                    margin: 20px 0;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🤖 CV Adapter</h1>
                
                <div class="tabs">
                    <button class="tab active"
                            onclick="showTab('url')">Par URL</button>
                    <button class="tab"
                            onclick="showTab('text')">Par Texte</button>
                </div>
                
                <form method="POST" action="/">
                    <div id="tab-url" class="tab-content active">
                        <label for="job_url">URL de l'offre d'emploi :</label>
                        <input type="url" id="job_url" name="job_url"
                               placeholder="https://welcometothejungle.com...">
                        <input type="hidden" name="mode" value="url">
                    </div>
                    
                    <div id="tab-text" class="tab-content">
                        <label for="job_text">Texte de l'offre
                            d'emploi :</label>
                        <textarea id="job_text" name="job_text"
                                  placeholder="Collez ici le texte de
 l'offre..."></textarea>
                        <input type="hidden" name="mode" value="text">
                    </div>
                    
                    <button type="submit">✨ Adapter mon CV</button>
                </form>
            </div>
            
            <script>
                function showTab(tabName) {
                    // Hide all tabs
                    document.querySelectorAll('.tab-content').forEach(el => {
                        el.classList.remove('active');
                    });
                    document.querySelectorAll('.tab').forEach(el => {
                        el.classList.remove('active');
                    });
                    
                    // Show selected tab
                    document.getElementById('tab-' + tabName)
                        .classList.add('active');
                    event.target.classList.add('active');
                    
                    // Update hidden mode field
                    const form = document.querySelector('form');
                    const modeInput = form.querySelector('input[name="mode"]');
                    modeInput.value = tabName === 'url' ? 'url' : 'text';
                }
            </script>
        </body>
        </html>
        """

        self.wfile.write(html.encode())

    def do_POST(self):
        """Traite le formulaire et adapte le CV"""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = urllib.parse.parse_qs(post_data)

        mode = params.get('mode', ['text'])[0]

        try:
            if mode == 'url':
                job_url = params.get('job_url', [''])[0]
                if not job_url:
                    raise ValueError("URL manquante")

                job_description = scrape_job_offer(job_url)
            else:
                job_description = params.get('job_text', [''])[0]
                if not job_description:
                    raise ValueError("Texte de l'offre manquant")

            # Adapter le CV
            adapt_cv_to_job(job_description)

            # Réponse de succès
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <title>CV Adapté - Succès</title>
                <style>
                    body {
                        font-family: -apple-system, BlinkMacSystemFont,
                            'Segoe UI', sans-serif;
                        max-width: 800px;
                        margin: 50px auto;
                        padding: 20px;
                    }
                    .success {
                        background: #d4edda;
                        color: #155724;
                        padding: 20px;
                        border-radius: 10px;
                        margin: 20px 0;
                    }
                    a {
                        color: #007bff;
                        text-decoration: none;
                    }
                </style>
            </head>
            <body>
                <div class="success">
                    <h2>✅ CV adapté avec succès !</h2>
                    <p>Votre CV a été adapté et sauvegardé dans
                        <code>src/data/cv-data-adapted.json</code></p>
                    <p>Vous pouvez maintenant l'utiliser pour votre
                        candidature.</p>
                </div>
                <a href="/">← Adapter un autre CV</a>
            </body>
            </html>
            """

            self.wfile.write(html.encode())

        except Exception as e:
            # Réponse d'erreur
            self.send_response(500)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Erreur</title>
                <style>
                    body {{
                        font-family: -apple-system, BlinkMacSystemFont,
                            'Segoe UI', sans-serif;
                        max-width: 800px;
                        margin: 50px auto;
                        padding: 20px;
                    }}
                    .error {{
                        background: #f8d7da;
                        color: #721c24;
                        padding: 20px;
                        border-radius: 10px;
                        margin: 20px 0;
                    }}
                    a {{
                        color: #007bff;
                        text-decoration: none;
                    }}
                </style>
            </head>
            <body>
                <div class="error">
                    <h2>❌ Erreur</h2>
                    <p>{str(e)}</p>
                </div>
                <a href="/">← Retour</a>
            </body>
            </html>
            """

            self.wfile.write(html.encode())


if __name__ == "__main__":
    # Vérifier la clé API
    if not os.environ.get('ANTHROPIC_API_KEY'):
        print(
            "❌ Erreur: Variable d'environnement "
            "ANTHROPIC_API_KEY non définie"
        )
        print("   Exécutez: export ANTHROPIC_API_KEY='votre-clé-api'")
        exit(1)

    port = 8080
    server = HTTPServer(('localhost', port), CVAdapterHandler)
    print(f"🚀 Serveur lancé sur http://localhost:{port}")
    print("   Ouvrez ce lien dans votre navigateur")
    print("   Appuyez sur Ctrl+C pour arrêter")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Serveur arrêté")
        server.shutdown()
