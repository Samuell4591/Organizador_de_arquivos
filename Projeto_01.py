import os 

def organizador_arquivos():
    caminho_atual = os.getcwd()
    arquivos = os.listdir(caminho_atual)

    pastas = {
        'imagens': ['.jpg', '.png', '.jpeg', '.gif'],
        'videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'documentos': ['.pdf', '.docx', '.txt', '.xlsx'],
        'texto': ['.txt', '.md']
    }

    # Cria as pastas se não existirem
    for pasta in pastas:
        if not os.path.exists(pasta):
            os.mkdir(pasta)

    # Move os arquivos para as pastas correspondentes
    for arquivo in arquivos:
        if os.path.isfile(arquivo):
            extensao = os.path.splitext(arquivo)[1].lower()
            for pasta, extensoes in pastas.items():
                if extensao in extensoes:
                    os.rename(arquivo, os.path.join(pasta, arquivo))
                    break  # Para evitar mover o mesmo arquivo para múltiplas pastas

organizador_arquivos()

print("Arquivos organizados com sucesso!")