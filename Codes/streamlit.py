from rmn import RMN
import streamlit as st
import numpy as np
import cv2
from PIL import Image
from collections import Counter
from play_song import play_random_song
import random
import pygame
import os
import threading
import streamlit as st



model = RMN()


emotion_folders = {
    "angry": "songs\calm",
    "happy": "songs\happy",
    "surprise": "songs\surprise",
    "sad": "songs\sad",
    "calm": "songs\calm",
}

# def play_random_song(emotion):
#     if emotion in emotion_folders:
#         folder_path = emotion_folders[emotion]
#         # Get a list of all song files in the folder
#         song_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3')]
#         if song_files:
#             # Choose a random song from the folder
#             song_name = random.choice(song_files)
#             # Play the randomly selected song
#             play_song(folder_path, song_name)
#         else:
#             print("No songs found for the specified emotion.")
#     else:
#         print("Emotion not supported.")


# def play_song(folder_path, song_name):
#     # Initialize pygame
#     pygame.init()
    
#     # Get the full path of the song
#     song_path = os.path.join(folder_path, song_name)
    
#     try:
#         # Initialize the mixer module
#         pygame.mixer.init()
        
#         # Load the song
#         sound = pygame.mixer.Sound(song_path)
        
#         # Play the song
#         sound.play()
        
#         # Wait until the song finishes playing
#         while pygame.mixer.get_busy():
#             pygame.time.Clock().tick(10)
        
#         # Quit pygame
#         pygame.quit()
        
#     except pygame.error:
#         print("Could not load or play the song.")


        
def process_image(image):
    image = np.array(image)
    emotion = model.detect_emotion_for_single_frame(image)
    return emotion

def capture_face():
    capture_duration = 1  # Capture images for 5 seconds
    cap = cv2.VideoCapture(0)  # Open the camera (0 for default camera)

    images = []
    start_time = cv2.getTickCount()

    while True:
        ret, frame = cap.read()  # Read a frame from the camera
        if not ret:
            break

        # Convert the frame to RGB format
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        images.append(Image.fromarray(rgb_frame))
        
        # Check if capture duration is reached
        elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
        if elapsed_time >= capture_duration:
            break

    cap.release()  # Release the camera
    
    emotions = []
    for image in images:
        emotions.append(process_image(image))
    emotion_counts = Counter(emotions)
    most_common_emotion = emotion_counts.most_common(1)[0][0]
    
    return most_common_emotion

# def play_and_monitor_emotion():
#     global is_playing, curr_emo, thread

#     curr_emo = capture_face()
#     play_random_song(curr_emo)

#     # Wait for the song to finish playing
#     is_playing = True
#     while is_playing:
#         # Check if the thread is alive (song is still playing)
#         if not thread.is_alive():
#             is_playing = False

def main():
    st.title("Face Capture and Model Output")
    
    curr_emo = None
    
    if st.button("Play"):
        curr_emo = capture_face()
        st.write("Your Current emotion is:", curr_emo)
        
        # Define path to your songs folder
        songs_folder = "songs"
        
        # Check if the chosen emotion folder exists in the songs directory
        if os.path.exists(os.path.join(songs_folder, curr_emo)):
            # List all songs in the chosen emotion folder
            songs = os.listdir(os.path.join(songs_folder, curr_emo))
            
            if songs:
                # Select a random song from the emotion folder
                random_song = random.choice(songs)
                song_path = os.path.join(songs_folder, curr_emo, random_song)
                
                # Display the selected song
                st.audio(song_path, format="audio/mpeg", loop=True)
            else:
                st.warning("No songs found for this emotion.")
        else:
            st.warning("Emotion folder not found.")





if __name__ == "__main__":
    main()