from apis import audio, twilio, gui
import customtkinter

def main_menu():
    gui.clear()
    gui.print("Select an action via a button!")
    gui.print("Currently selected genres: ")
    gui.print(user_selections["genres"])
    gui.print("Currently selected artists:")
    gui.print(user_selections["artists"])   

def quit_program():
    app.destroy()

def select_genres():
    gui.clear()
    gui.print("Select favorite genres here...")
    # 1. Allow user to select one or more genres using the
    #    audio.get_genres() function
    gui.print(audio.get_genres())
    genres = gui.input(prompt = "Select your favorite genres:\nType clear to clear your selections")
    # 2. Allow user to store / clear / modify / retrieve genres
    #    from user_selections to be used in the mixtape
    user_selections["genres"].append(genres)
    if genres == "clear":
        for genre in genres:
            user_selections["genres"].pop()
            main_menu()
    main_menu()
    
def select_artists():
    gui.clear()
    gui.print("Select favorite artists here...")
    # 1. Allow user to search for an artist using
    #    audio.search_for_artists() function
    particular_artist = gui.input(prompt = "Type your favorite artist")
    possible_matches = audio.search_for_artists(particular_artist)

    
    # 2. Allow user to store / clear / modify / retrieve artists
    #    from user_selections to be used in the mixtape
    nice_table = audio.generate_artists_table(possible_matches)
    gui.print(nice_table)
    if particular_artist == "clear":
        user_selections["artists"]={}
        main_menu()
        return
        
    artist_select = int(gui.input(prompt = "What number corresponds to your artist?"))
    an_artist = possible_matches[artist_select - 1]

    artist_name = an_artist["name"]
    artist_id = an_artist["id"]
    
    user_selections["artists"][artist_name]= artist_id
    


    main_menu()
          

def make_mixtape():
    gui.clear()
    gui.print("Show recommendations here...")
    # 1. Allow user to retrieve song recommendations using the
    #    audio.generate_mixtape() function
    list_of_ids = []
    for entry in user_selections["artists"]:
        artist_id = user_selections["artists"][entry]
        list_of_ids.append(artist_id)

    
    suggested_tracks = audio.generate_mixtape(artist_ids = list_of_ids, genres = user_selections["genres"], practice = False)
    # 2. Show them to the user
    gui.print(audio.generate_tracks_table(suggested_tracks))
    # 3. Ask if you want to email them!
    email_prompt = gui.input(prompt = "Would you like to email this mixtape to someone?")
    if email_prompt == "Yes":
        email_send = gui.input("What is the email you would like to send it to?")
        twilio.send_email(to_emails = email_send, subject = "A mixtape for you!", content = audio.generate_tracks_table(suggested_tracks, to_html = True), to_file = True)
        
                          


### GLOBAL VARIABLES
user_selections = {
    'genres': [],
    'artists': {}
}

actions = {
    "Main Menu": main_menu,
    "Quit": quit_program,
    "Select Genres": select_genres,
    "Select Artists": select_artists,
    "Make Mixtape!": make_mixtape,
}

app = customtkinter.CTk()
gui._setup_window(app, title="Mixtape Maker")
gui._setup_buttons(actions)
main_menu()
app.mainloop()
