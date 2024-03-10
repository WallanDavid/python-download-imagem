import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import tkinter as tk
from tkinter import filedialog, messagebox
from concurrent.futures import ThreadPoolExecutor
import threading

class ImageDownloaderApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Downloader")

        self.label_url = tk.Label(master, text="URL do site:")
        self.label_url.grid(row=0, column=0, sticky="w")

        self.entry_url = tk.Entry(master, width=50)
        self.entry_url.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

        self.label_folder = tk.Label(master, text="Pasta de destino:")
        self.label_folder.grid(row=1, column=0, sticky="w")

        self.entry_folder = tk.Entry(master, width=40)
        self.entry_folder.grid(row=1, column=1, padx=5, pady=5)

        self.button_browse = tk.Button(master, text="Procurar", command=self.browse_folder)
        self.button_browse.grid(row=1, column=2, pady=5)

        self.label_count = tk.Label(master, text="Número máximo de imagens:")
        self.label_count.grid(row=2, column=0, sticky="w")

        self.entry_count = tk.Entry(master, width=10)
        self.entry_count.grid(row=2, column=1, padx=5, pady=5)

        self.button_download = tk.Button(master, text="Baixar Imagens", command=self.download_images)
        self.button_download.grid(row=2, column=2, pady=5)

        self.progress_bar = tk.Label(master, text="")
        self.progress_bar.grid(row=3, column=0, columnspan=3)

        self.button_open_folder = tk.Button(master, text="Abrir Pasta", command=self.open_folder)
        self.button_open_folder.grid(row=4, column=0, pady=5)

        self.button_close = tk.Button(master, text="Fechar", command=master.quit)
        self.button_close.grid(row=4, column=2, pady=5)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        self.entry_folder.delete(0, tk.END)
        self.entry_folder.insert(0, folder_path)

    def download_images(self):
        url = self.entry_url.get()
        folder = self.entry_folder.get()
        count = int(self.entry_count.get()) if self.entry_count.get() else None

        if not url or not folder:
            messagebox.showerror("Erro", "Por favor, insira a URL do site e selecione uma pasta de destino.")
            return

        try:
            image_urls = self.extract_image_urls(url, count)
            self.download_images_threaded(image_urls, folder)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante o download das imagens:\n{str(e)}")

    def extract_image_urls(self, url, count=None):
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        image_tags = soup.find_all('img')

        image_urls = [urljoin(url, img['src']) for img in image_tags]

        if count is not None:
            image_urls = image_urls[:count]

        return image_urls

    def download_image(self, url, folder):
        try:
            response = requests.get(url)
            response.raise_for_status()

            filename = os.path.join(folder, os.path.basename(urlparse(url).path))

            with open(filename, 'wb') as f:
                f.write(response.content)
        except Exception as e:
            raise Exception(f"Erro ao baixar a imagem {url}: {str(e)}")

    def download_images_threaded(self, image_urls, folder):
        self.progress_bar.config(text="Baixando imagens...")

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = []
            for url in image_urls:
                futures.append(executor.submit(self.download_image, url, folder))

            total_images = len(futures)
            downloaded_images = 0
            for future in futures:
                try:
                    future.result()
                    downloaded_images += 1
                    self.progress_bar.config(text=f"Baixando... {downloaded_images}/{total_images}")
                except Exception as e:
                    messagebox.showwarning("Aviso", f"Alguns erros ocorreram durante o download:\n{str(e)}")

        self.progress_bar.config(text=f"Download concluído ({downloaded_images}/{total_images})")

    def open_folder(self):
        folder = self.entry_folder.get()
        if not folder:
            messagebox.showerror("Erro", "Nenhuma pasta de destino selecionada.")
            return

        os.system(f'explorer "{folder}"')

def run_app():
    root = tk.Tk()
    app = ImageDownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()
