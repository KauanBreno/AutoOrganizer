from pathlib import Path

def organize_files():
    
# Lista com os Tipos de arquivos que estamos separando(Adicione mais Tipos Caso queira)
    types = ['exe', 'txt', 'jpg', 'png', 'pdf', 'docx', 'zip']

 # Diretorio da pasta Downlouds 
    raiz = Path.home() / "Downloads"
    
# laço que cria as Pastas com nomes da lista {Types}
    for type in types:
        new_folder = raiz / type
        new_folder.mkdir(exist_ok=True)

#Cria a pasta de arquivos gerais (Arquivos que não estão na lista {types})
    general_folder_name = "Arquivos Gerais" # Nome do diretório de pastas e arquivos não classificados
    folder_path = raiz / general_folder_name 
    folder_path.mkdir(exist_ok=True)
    
# Laço de repetição que adiciona os arquivos em suas respectivas pastas classificas pelo tipo de arquivos
    for type in types: 
        for file in raiz.glob(f"*.{type}"): 
            file_name = file.name
            new_path_folder = raiz / type / file_name
            if not new_path_folder.exists():
                file.rename(new_path_folder)
    
    
# Laço de repetição que adiciona Pastas ou arquivos não classificados na pasta "Arquivos Gerais" 
    for folder in raiz.iterdir():
        if folder.name not in types:
            if folder != folder_path:
                Dest = folder_path / folder.name
                if not Dest.exists():
                    folder.rename(Dest)
                else:
                    print(f"O arquivo {Dest} já exixste")
                    
        
                    
    print("Pasta Downloads organizada com sucesso!")        
if __name__ == "__main__":
    organize_files()
            