import webbrowser

comando = "/mnt/c/Program\ Files/Mozilla\ Firefox/firefox.exe %s"
#nav3 = webbrowser.get(comando)
#webbrowser.register("firefox", None, nav3)
webbrowser.get(comando).open("https://www.abc.com.py")