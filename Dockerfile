FROM deezer/spleeter:3.6-5stems

#CMD ["/bin/bash"]



# docker run -v C:\Users\Xhepi\Desktop\nda\audio_out:/output  -v C:\Users\Xhepi\Desktop\nda\audio_in:/input nda_spleeter separate -o /output /input/relax.wav
# youtube-dl --extract-audio --audio-format mp3 --output "/audio_in/%(uploader)s%(title)s1234.%(ext)s" http://www.youtube.com/watch?v=rtOvBOTyX00