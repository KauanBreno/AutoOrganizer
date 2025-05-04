from pathlib import Path



def organize_files():
    
    types = ['exe', 'txt', 'jpg', 'png', 'pdf', 'docx', 'zip']

    raiz = Path.home() / "Downloads"
    

    for type in types:
        new_folder = raiz / type
        new_folder.mkdir(exist_ok=True)

    for type in types:
        for file in raiz.glob(f"*.{type}"):
            file_name = file.name
            new_path_folder = raiz / type / file_name
            file.rename(new_path_folder)
            
    
    print("Pasta Downloads organizada com sucesso!")        
if __name__ == "__main__":
    organize_files()
            
        
            
        
