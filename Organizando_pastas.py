from pathlib import Path



def organize_files():
    

    types = ['exe', 'txt', 'jpg', 'png', 'pdf', 'docx', 'pdf', 'zip']

    raiz = Path.home() / "Downloads"
    

    for type in types:
        new_folder = raiz / type
        new_folder.mkdir(exist_ok=True)

    for file in raiz.iterdir():
        name_file = file.name
        
