import os
from utils.downloader import download_site
from utils.logger import setup_logger



def afficher_ascii_htrack():
   
    print(r"""
          
   _   _ _____ _____            _    
  | | | |_   _|_   _|          | |   
  | |_| | | |   | |  _ __   ___| | __
  |  _  | | |   | | | '_ \ / _ \ |/ /
  | | | |_| |_  | | | | | |  __/   < 
  \_| |_/\___/  \_/ |_| |_|\___|_|\_\
  ===================================
  Claude Ndanda
  github : https://github.com/NdandaClaude/HTrack
  linkedin : https://www.linkedin.com/in/claude-ndanda-6aa606302/
  ===================================
    """)




def afficher_menu():
    """Affiche le menu principal."""
    print("\n=== Menu Principal ===\n")
    print("1. Télécharger un site web complet")
    print("2. Sélectionner les types de fichiers à télécharger")
    print("3. Voir les logs récents")
    print("4. Modifier les paramètres par défaut")
    print("5. Quitter\n")
    return input("Choisissez une option : ")




def voir_logs(log_file):
    if os.path.exists(log_file):
        print("\n=== Logs récents ===\n")
        with open(log_file, "r") as f:
            lines = f.readlines()
            for line in lines[-10:]:  
                print(line.strip())
    else:
        print("\nAucun log trouvé.\n")



def modifier_parametres():
    print("\n=== Modifier les paramètres ===\n")
    global default_output_dir
    new_dir = input(f"Répertoire actuel : {default_output_dir}\nEntrez un nouveau répertoire de sortie (ou appuyez sur Entrée pour conserver) : ")
    if new_dir:
        default_output_dir = new_dir
        print(f"Le répertoire par défaut a été mis à jour : {default_output_dir}")
    else:
        print("Aucun changement effectué.")




def main():
    logger = setup_logger("HTrack", "cloner.log")

    afficher_ascii_htrack()
    
    global default_output_dir, file_types

    default_output_dir = "sites/output" 
    file_types = ["html", "css", "js", "png", "jpg", "jpeg", "gif"]  

    while True:
        choice = afficher_menu()

        if choice == "1":
            url = input("Entrez l'URL du site à copier : ")
            output_dir = input(f"Entrez le dossier de destination (par défaut : '{default_output_dir}') : ") or default_output_dir
            print("\nTéléchargement en cours... Cela peut prendre quelques minutes.\n")
            try:
                download_site(url, output_dir, logger, file_types)
            except Exception as e:
                logger.error(f"Erreur lors du téléchargement : {e}")
                print("\n❌ Une erreur est survenue. Consultez le fichier de log pour plus d'informations.")
            else:
                print("\n✅ Téléchargement terminé avec succès !")


        elif choice == "2":
            print("\n=== Types de fichiers actuels ===")
            print(", ".join(file_types))
            new_types = input("Entrez les extensions de fichiers à inclure (séparées par des virgules, ou laissez vide pour conserver) : ")
            if new_types:
                file_types = [ext.strip() for ext in new_types.split(",") if ext.strip()]
                print(f"Types de fichiers mis à jour : {', '.join(file_types)}")
            else:
                print("Aucun changement effectué.")

        elif choice == "3":
            voir_logs("cloner.log")
        elif choice == "4":
            modifier_parametres()
        elif choice == "5":
            print("Au revoir !")
            break
        else:
            print("❌ Choix invalide.")

if __name__ == "__main__":
    main()
