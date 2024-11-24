HTrack 

HTrack est un puissant outil en Python pour cloner intégralement des sites web. Il permet de télécharger les ressources HTML, CSS, JavaScript, images, vidéos, et bien plus.


🎯 Fonctionnalités

   📂 Téléchargement complet de sites web avec toutes leurs ressources.
   🔍 Filtrage des ressources à télécharger par type de fichier (HTML, CSS, JS, PNG, etc.).
   🛠 Personnalisation du répertoire de sortie.
   📜 Affichage des logs récents pour le suivi des opérations.
   ✅ Compatible avec les sites web modernes.


🚀 Installation


Prérequis
   Python 3.12 ou une version ultérieure.
   
Les bibliothèques Python suivantes :
   requests
   beautifulsoup4
   tqdm
   
Étapes d'installation

Clonez le dépôt GitHub :
   git clone https://github.com/NdandaClaude/htrack.git
   cd htrack
   Installez les dépendances nécessaires :
   pip install -r requirements.txt

Lancez l'application :
   python cloner.py

📝 Utilisation

Une fois lancé, HTrack vous affichera un menu interactif :


   _   _ _____ _____            _    
  | | | |_   _|_   _|          | |   
  | |_| | | |   | |  _ __   ___| | __
  |  _  | | |   | | | '_ \ / _ \ |/ /
  | | | |_| |_  | | | | | |  __/   < 
  \_| |_/\___/  \_/ |_| |_|\___|_|\_\
  ===================================
           

=== Menu Principal ===

1. Télécharger un site web complet
2. Sélectionner les types de fichiers à télécharger
3. Voir les logs récents
4. Modifier les paramètres par défaut
5. Quitter



Options principales
   
   Télécharger un site web : Entrez l'URL et le dossier de destination pour démarrer le clonage.
   Types de fichiers : Choisissez les extensions de fichiers à inclure (par défaut : html, css, js, png, jpg).
   Logs récents : Consultez les dernières activités enregistrées dans le fichier cloner.log.
   Paramètres : Changez le répertoire de destination par défaut.

📁 Arborescence du Projet


htrack/
│
├── htrack.py              # Script principal
├── requirements.txt       # Dépendances du projet
├── utils/
│   ├── downloader.py      # Gestion du téléchargement
│   ├── logger.py          # Configuration du journal
├── output/                # Répertoire par défaut pour les sites clonés
├── cloner.log             # Fichier de logs
└── README.md              # Documentation

⚙️ Personnalisation

HTrack est conçu pour être flexible. Voici quelques options que vous pouvez modifier dans le fichier htrack.py :

   Répertoire de sortie par défaut : default_output_dir = "output"
   Types de fichiers : Modifiez la variable file_types pour inclure ou exclure certains formats.
   Nombre de logs récents affichés : Ajustez la valeur dans voir_logs.
   
📖 Exemples
   
   Cloner un site web complet
   Choisissez l'option 1 dans le menu.
   
   Entrez l'URL du site, par exemple :
   
      https://www.example.com
      Entrez le dossier de destination (ou laissez vide pour utiliser le répertoire par défaut).
      Attendez que le processus de téléchargement soit terminé.
   
   Filtrer par type de fichier
      Choisissez l'option 2 dans le menu.
      Entrez les extensions séparées par des virgules, par exemple :
      html, css, js, png, jpg
      
   Voir les logs
      Choisissez l'option 3 pour consulter les dernières activités.

   
🛠 Dépendances
Les bibliothèques utilisées dans ce projet :

   Requests : Gestion des requêtes HTTP.
   BeautifulSoup4 : Parsing et manipulation des contenus HTML.
   Tqdm : Barres de progression interactives.
   
Installez-les avec :

pip install requests beautifulsoup4 tqdm

⚠️ Disclaimer
HTrack est destiné à des usages légaux uniquement. Assurez-vous d'avoir l'autorisation de cloner un site web avant d'utiliser cet outil. L'auteur décline toute responsabilité en cas d'utilisation abusive.

🏆 Auteur
Créé avec ❤️ par Claude Ndanda.

HTrack - Téléchargez, explorez et sauvegardez des sites web 
