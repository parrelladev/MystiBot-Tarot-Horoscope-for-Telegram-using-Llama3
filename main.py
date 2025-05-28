import subprocess
import time
import requests
import os
import signal

OLLAMA_PORT = 11434
OLLAMA_MODEL = 'deepseek-r1:8b'

def start_ubuntu_with_ollama():
    print("🚀 Abrindo terminal Ubuntu com Ollama serve...")
    # Abre o Ollama no Ubuntu (WSL)
    return subprocess.Popen(
        ['wsl.exe', '-d', 'Ubuntu', '--', 'bash', '-c', 'OLLAMA_USE_CUDA=1 ollama serve'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def wait_for_ollama(timeout=20):
    print("⏳ Aguardando Ollama ficar disponível...")
    url = f"http://localhost:{OLLAMA_PORT}/api/tags"
    for _ in range(timeout):
        try:
            res = requests.get(url, timeout=1)
            if res.status_code == 200:
                print("✅ Ollama está pronto!")
                return True
        except:
            pass
        time.sleep(1)
    print("❌ Ollama não respondeu a tempo.")
    return False

def run_bot():
    from core.bot import run_bot
    print("🤖 Iniciando MystiBot...")
    run_bot()
    print("📴 MystiBot finalizado.")

def stop_ollama():
    print("🛑 Encerrando processo do Ollama no Ubuntu...")
    subprocess.call([
        'wsl.exe', '-d', 'Ubuntu', '--',
        'bash', '-c', "pkill -9 ollama"
    ])

if __name__ == "__main__":
    print("🔄 Iniciando MystiBot com controle total...")

    ollama_process = start_ubuntu_with_ollama()

    if wait_for_ollama():
        try:
            run_bot()
        finally:
            stop_ollama()
            print("✅ Processo concluído.")
    else:
        print("⚠️ Encerrando: Ollama não respondeu.")
