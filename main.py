import requests
import pandas as pd

def download_image(url, file_name):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
                
        print(f"Imagem salva como: {file_name}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar a imagem: {e}")

def main():
    df = pd.read_excel('./Tables/dados_sem_listas.xlsx')
    for index, row in df.iterrows():
        if pd.notna(row['pictureUrl']):
            download_image(row['pictureUrl'], f"./Images/img_{int(row['id'])}.jpg")
            print(f"Baixando imagem {index + 1} de {len(df)}")


if __name__ == '__main__':
    main()