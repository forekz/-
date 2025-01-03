import os
import shutil
import requests
import subprocess

def delete_roblox():
    roblox_paths = [
        os.path.join(os.environ['LOCALAPPDATA'], 'Roblox'),
        os.path.join(os.environ['PROGRAMFILES'], 'Roblox'),
        os.path.join(os.environ['PROGRAMFILES(X86)'], 'Roblox')
    ]
    
    for path in roblox_paths:
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
                print(f'Роблокс успешно удален из {path}')
            except Exception as e:
                print(f'Ошибка при удалении Роблокс: {e}')

def download_tanks():
    tanks_url = "https://redirect.wargaming.net/WoT/latest_web_install_na"
    save_path = os.path.join(os.environ['TEMP'], 'wot_install.exe')
    
    try:
        print('Начинаем загрузку World of Tanks...')
        response = requests.get(tanks_url, stream=True)
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print('Запускаем установщик World of Tanks...')
        subprocess.run([save_path])
        
    except Exception as e:
        print(f'Ошибка при скачивании/установке World of Tanks: {e}')

if __name__ == '__main__':
    print('Начинаем процесс замены Роблокс на World of Tanks...')
    delete_roblox()
    download_tanks()
    print('Процесс завершен!')
