#2/24/25
#marvel movie recs
#milan hill
import time
import random
from PIL import Image
import requests
from io import BytesIO


marvel_movies = ["https://tinyurl.com/4nvttw2f", #Captian America: Brave New World
"https://tinyurl.com/vk7pr6w7", #Black Widow
"https://tinyurl.com/3azy6bhc", #Black Panther
"https://tinyurl.com/5x85dmdu", #End Game
"https://tinyurl.com/4sba3ud2"  #Captain Marvel
]

#Define a function called open_image with a url parameter for the image address
def open_image(url): #function that is assigned with am image from its image address
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

while True:
    print("Welcome to Milan's Marvel Movie Recommendations") #introduces user
    answer = input("Would you like a recommendation? Y for Yes and N for No. Enter:") #asks for input if they want to play
    if answer == "Y":
        print("checking recently watched list...")
        time.sleep(3) #uses a time fn for aesthetics
        compare = (random.choice(marvel_movies)) #assigns the random movie to a function
        if compare == "https://tinyurl.com/4nvttw2f": #if the fn is chosen, it is printed with a description
            print("My Rating: 5/5 stars. Movie: Captain America: Brave New World. Description/Review: Captian America will not only have you gripping your popcorn bucket, but it will have you trying to figure out the unpredictable plot in the first few scenes. If you are looking for an intense, action film movie with amazing CGI along and a diverse group of marvel actors, this is the movie to watch next.")
            open_image(compare)
        elif compare == "https://tinyurl.com/vk7pr6w7":
            print("My Rating: 5/5 stars. Movie: Black Widow. Description/Review: THIS MOVIE IS AMAZING. I don't know if I was just emotional because it was my birthday watching this or if I was really impacted by this movie. I love spy thrillers espeically with women. Scarlett Johanson is an amazing actor and her bravery to defeat the red room was incredible. I also loved the CGI and the story of how she had a fake family but was still very close with her sister")
            open_image(compare)
        elif compare == "https://tinyurl.com/3azy6bhc":
            print("My Rating: 5/5 stars. Movie: Black Panther. Description/Review: Applause. Applause. Sobs. and more Applause. This movie touched my heart. Seeing black people on the screen being so powerful and intelligent was so impactful for me. The culture of Wakanda so beautiful to watch and I couldn't get my eyes of the screen. the plot was intense and thrilling and had me looking around after the film like wow! just wow! Also, watch the new black panther as well if you enjoy this one which I know you will.")
            open_image(compare)
        elif compare == "https://tinyurl.com/5x85dmdu":
            print( "My Rating: 5/5 stars. Movie: End game. Description/Review: Seeing so many marvel superheros in one movie made me feel full and just content. I love them all and seeing them working together fro one cause just made it all feel more real (i know its fiction). Thanos is awful but I loved seeing all the superheros and mix of dry humors throughout the film. although it does have a sad ending( sorry for the spoiler) give is watch!")
            open_image(compare)

    if answer == "N": #if they don't want to have a recommendation, they are can leave!
        print("Okay! thanks for joining!")
        quit()





#DO NOT FORGET TO CITE YOUR SOURCE
# Captian America: Brave New World movie starring Anthony Mackie. This is a critical review. Image source: Screen Rant. 2025. Feline Rangel. Accessed via https://tinyurl.com/3e7uvuyv.
# Black Widow is a spy thriller starring Scarlett Johanson. Image source: Review articel from the source The Knockturnal. 2021. Ethan Singh. Accessed via https://theknockturnal.com/film-review-black-widow/.
# Black Panther is a action filled and culture marvel movie starring Chadwick Boseman. This is film review. Image source: Roger Ebert. 2018. Odie Henderson. Accessed via https://tinyurl.com/yhd5vjfm.
# End game is a intense marvel movie featuring all of the marvel characters. This is a review on the movie. Image source: Forbes. 2019. Scott Mendelson. Accessed via: https://tinyurl.com/5x85dmdu.
# Captain Marvel is a female superhero starring Brie Larson. This is review of te film. Image source: Penn Moviegoer. Phoebe Weintraub. Accesssed via: https://www.thepennmoviegoer.com/about-us.



