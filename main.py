from googlesearch import search

def search_music(mood):
    query = f"{mood} instrumental music YouTube"
    try:
        for j in search(query, num_results=1):
            return j
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    print("What kind of music you want to listen?")
    print("1. Relaxing\n2. Study\n3. Focus\n4. Nature\n5. Joyful\n6. Energetic\n7. Ambient\n8. Uplifting\n9. Chill\n10. Serene\n"
          "11. Motivational\n12. Inspirational\n13. Mellow\n14. Peaceful\n15. Soothing\n16. Melodic\n17. Tranquil\n18. Laid-back\n"
          "19. Happy\n20. Calm")

    user_input = input("Enter the number corresponding to your mood: ")

    moods = [
        "Relaxing", "Study", "Focus", "Nature", "Joyful",
        "Energetic", "Ambient", "Uplifting", "Chill", "Serene",
        "Motivational", "Inspirational", "Mellow", "Peaceful", "Soothing",
        "Melodic", "Tranquil", "Laid-back", "Happy", "Calm"
    ]

    try:
        mood_index = int(user_input) - 1
        if 0 <= mood_index < len(moods):
            selected_mood = moods[mood_index]
            print(f"Searching for {selected_mood} music on YouTube...")
            video_link = search_music(selected_mood)
            if video_link:
                print(f"Click the link to open the video: {video_link}")
            else:
                print("No results found.")
        else:
            print("Invalid input. Please enter a number within the range.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
