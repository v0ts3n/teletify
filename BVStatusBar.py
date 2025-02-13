try:

    
    api_id = 0000
    api_hash = '1111'


    #FULL PROJECT BY B_VOTSON FROM B_VOTSON TEAM
    isfirst = True
    textname = "Сейчас играет - "
    textauthor = " .Автор: "
    timebefore = 3
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth
    from tkinter import *
    import asyncio
    import time
    from telethon.sync import TelegramClient
    from telethon.tl.functions.account import *
    import os
    from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QVBoxLayout, QPushButton, QListWidget, QTextEdit
    from PyQt5.uic import loadUi
    import zipfile
    from PyQt5.QtCore import QThread, pyqtSignal
    import threading
    ison = True
    first_status = ""
    from idlelib.tooltip import Hovertip

    # Инициализация объекта Spotipy
    #sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='5c2fa33e816441f68e51540561e605ae', client_secret='9fd28d95c3af45e39bce47b1844eb89d', redirect_uri='http://bvotson.byethost7.com', scope='user-read-currently-playing'))
    client_id = input("SPOTIFY CLIENT ID: ")
    if client_id == "":
        client_id="5c2fa33e816441f68e51540561e605ae"
    client_secret = input("SPOTIFY SECRET ID: ")
    if client_secret == "":
        client_secret="9fd28d95c3af45e39bce47b1844eb89d"
    redirect_url = input("SPOTIFY REDIRECT URL: ")
    if redirect_url == "":
        redirect_url="http://bvotson.byethost7.com"
        

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret, redirect_url, scope="user-read-currently-playing"))
    # Получение информации о текущем треке
    current_track = sp.current_user_playing_track()


    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QFileDialog, QAction
    from PyQt5.QtGui import QIcon, QPixmap
    from PyQt5 import uic
    #=============================
    """
    # Use your own values from my.telegram.org
    api_id = 15304600
    api_hash = '12c4ed983eb315a4ea4ebb15381cf147'
    print("Nerif Project Status Bar")
    # The first parameter is the .session file name (absolute paths allowed)
    def setabout(name, author):
        global isfirst
        global textauthor
        global textname
        with TelegramClient('BVTelegram', api_id, api_hash) as client:
            if isfirst:
                client.send_message('me', 'Было запущено приложение Nerif Project StatusBar Beta от B_Votson Team. Все права на скрипт принадлежат B_Votson Team. Сайт: http://bvotson.byethost7.com . Сайт проекта: nerifproject.22web.org. Удачного использования.')
                isfirst = False
            client(UpdateProfileRequest(
                about = textname + name + textauthor + author
            ))
    def setstandart():
        with TelegramClient('BVTelegram', api_id, api_hash) as client:
            
            client(UpdateProfileRequest(
                about = ""
            ))
    def loop1():
        while True:
            global ison
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            while ison == True:
                global timebefore
                
                time.sleep(int(timebefore))
                if current_track is not None:
                    name = current_track['item']['name']
                    author = current_track['item']['artists'][0]['name']
                    setabout(name, author)    
                    print("TRACKED")
                    
            setstandart()
    """            
    textname = "Сейчас играет - "
    textauthor = " .Автор: "
    timebefore = 3
    ison = False

    """
    def getcurrent():
        with TelegramClient('BVTelegram', api_id, api_hash) as client:
            me = client.get_me()
            return me.bio
    """

    def setabout(name, author):
        global isfirst
        global textauthor
        global first_status
        global textname
        with TelegramClient('BVTelegram', api_id, api_hash) as client:
            if isfirst:
                client.send_message('me', 'Было запущено приложение Nerif Project StatusBar Beta от B_Votson Team. Все права на скрипт принадлежат B_Votson Team. Сайт: http://bvotson.byethost7.com . Сайт проекта: nerifproject.22web.org. Удачного использования.')
                first_status = client.get_me().about
                isfirst = False
            client(UpdateProfileRequest(
                about = textname + name + textauthor + author
            ))
    def setstandart():
        global first_status
        with TelegramClient('BVTelegram', api_id, api_hash) as client:
            
            client(UpdateProfileRequest(
                about = first_status
            ))
    class Worker(QThread):
        signal = pyqtSignal(str)
        def run(self):
            print("HUE")
            while True:
                print("HUE")
                global ison
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                while ison == True:
                    global timebefore
                    
                    time.sleep(int(timebefore))
                    if current_track is not None:
                        name = current_track['item']['name']
                        author = current_track['item']['artists'][0]['name']
                        setabout(name, author)    
                        print("TRACKED")
                        
                setstandart()



    class FileSelectorApp(QMainWindow):
        global textname
        global textauthor
        global timebefore
        global ison
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            loadUi("design.ui", self)

            self.pushButton_2.clicked.connect(self.onIt)
            self.pushButton.clicked.connect(self.saveChanges)

            self.worker_thread = Worker()
            
            self.worker_thread.start()
        def onIt(self):
            global ison
            print("STARTED")
            ison = not ison
            
        def saveChanges(self):
            textname = str(self.lineEdit_2.text())
            textauthor = str(self.lineEdit.text())
            timebefore = self.spinBox.value()
            print(timebefore)
            


        

    if __name__ == '__main__':
        app = QApplication([])
        window = FileSelectorApp()
        window.show()
        app.exec_()
except Exception as ex:
    print(ex)
    
