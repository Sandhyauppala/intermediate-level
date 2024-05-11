def take_command():
    print("Listening...")
    query = input("You: ")
    return query

if __name__ == '__main__':
    print("Amigo assistance activated ")
    print("How can I help you?")

    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            print("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            try:
                results = "Dummy Wikipedia summary for " + query
                print("According to Wikipedia:")
                print(results)
            except:
                print("Error: Unable to fetch Wikipedia information.")

        elif 'are you' in query:
            print("I am Amigo, developed by Jaspreet Singh.")

        elif 'open youtube' in query:
            print("Opening YouTube...")
            # Code to open YouTube in a web browser

        elif 'open google' in query:
            print("Opening Google...")
            # Code to open Google in a web browser

        elif 'open github' in query:
            print("Opening GitHub...")
            # Code to open GitHub in a web browser

        elif 'open stackoverflow' in query:
            print("Opening Stack Overflow...")
            # Code to open Stack Overflow in a web browser

        elif 'open spotify' in query:
            print("Opening Spotify...")
            # Code to open Spotify in a web browser

        elif 'open whatsapp' in query:
            print("Opening WhatsApp...")
            # Code to open WhatsApp application

        elif 'play music' in query:
            print("Playing music...")
            # Code to play music

        elif 'local disk d' in query:
            print("Opening Local Disk D...")
            # Code to open Local Disk D

        elif 'local disk c' in query:
            print("Opening Local Disk C...")
            # Code to open Local Disk C

        elif 'local disk e' in query:
            print("Opening Local Disk E...")
            # Code to open Local Disk E

        elif 'sleep' in query:
            print("Exiting Amigo.")
            break