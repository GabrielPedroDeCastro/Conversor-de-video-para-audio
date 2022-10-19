import moviepy.editor   # pip install moviepy

# Carregar arquivos do video
video = moviepy.editor.VideoFileClip("video.mp4")

# Extrair áudio
audio_data = video.audio

# Salvar Arquivo de de áudio extraído
audio_data.write_audiofile("audio_video.mp3")

