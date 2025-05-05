from pathlib import Path


def organize_files():
    
# Lista com os nomes dos Tipos de arquivos que estamos separando(Adicione mais Tipos Caso queira)
    types = ['exe', 'txt', 'jpg', 'png', 'pdf', 'docx', 'zip']

 # Diretorio da pasta Downlouds 
    raiz = Path.home() / "Downloads"
    
# laço que cria as Pastas com nomes da lista {Types}
    for type in types:
        new_folder = raiz / type
        new_folder.mkdir(exist_ok=True)

#Cria a pasta de arquivos gerais (Arquivos que não estão na lista {types})
    folder_name_general_folder = "Arquivos Gerais" # O nome do variavel ficou muito grande! :(
    folder_path = raiz / folder_name_general_folder
    folder_path.mkdir(exist_ok=True)
    
# Laço de repetição que adiciona os arquivos em suas respectivas pastas classificas pelo tipo de arquivos
    for type in types:
        for file in raiz.glob(f"*.{type}"):
            file_name = file.name
            new_path_folder = raiz / type / file_name
            file.rename(new_path_folder)
    
    
# Laço de repetição que adiciona Pastas ou arquivos não classificados na pasta "Arquivos Gerais" 
    for folder in raiz.iterdir():
        if folder.is_dir and folder.name not in types:
            if folder != folder_path:
                folder.rename(folder_path / folder.name)
        
                    
                
                
                
                
                
    print("Pasta Downloads organizada com sucesso!")        
if __name__ == "__main__":
    organize_files()
            
        
            
        
