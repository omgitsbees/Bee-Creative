import pygame
import os

# Initialize Pygame mixer
pygame.mixer.init()

# Function to load and play a song
def play_song(song_path):
    try:
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        print(f'Playing: {os.path.basename(song_path)}')
    except pygame.error as e:
        print(f'Error playing {song_path}: {e}')
        
# Function to stop the song
def stop_song():
    pygame.mixer.music.stop()
    print('Music stopped')
    
# Function to pause the song
def pause_song():
    pygame.mixer.music.pause()
    print('Music paused')
    
# Function to unpause the song
def unpause_song():
    pygame.mixer.music.unpause()
    print('Music unpaused')
    
# Main program
if __name__ == "__main__":
    while True:
        print("\nMP3 Player")
        print("1. Play a song")
        print("2. Stop the song")
        print("3. Pause the song")
        print("4. Unpause the song")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            song_path = input("Enter the path of the song: ")
            play_song(song_path)
        elif choice == "2":
            stop_song()
        elif choice == "3":
            pause_song()
        elif choice == "4":
            unpause_song()
        elif choice == "5":
            print("exiting MP3 Player")
            break
        else:
            print("Invalid choice. Please try again.")