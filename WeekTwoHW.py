#Week Two - Assignments 1 & 2
bookShelf = ["All The Light We Cannot See", "The Time Traveler's Wife", "The Tea Girl of Hummingbird Lane", "The Invention of Wings", "Americanah", "Such A Fun Age", "Pride and Prejudice"]

favBook = {
	"title": "All The Light We Cannot See",
	"author": "Anthony Doerr",
	"published": 2014,
	"award": "Pulitzer Prize in Fiction",
	"genre": "historical fiction",
	"setting": ["Germany", "France"],
	"english": True
}

instantCameras = ["Instax Wide", "Instax Mini", "Instax SQ6"]

instantCameras[2] = {
    "camera": "Instax SQ6",
    "digital": False,
    "film": True,
    "maker": "Fujifilm",
    "filmSize": "Instax Square",
    "color": "white"	
}

# Week Two - Assignment 3
# intro
print ("Welcome to Choose Your Own VP Adventure!")
print ("Answer the prompts to join the debate.")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# madlib selection
day = raw_input("Choose a day of the week:")
vp1 = raw_input("Name a powerful woman:")
vp2 = raw_input("Name a villian:")
adj1 = raw_input("Adjective:")
num = raw_input("Number:")
noun1 = raw_input("Group of people:")
adj2 = raw_input("Another adjective:")
noun2 = raw_input("Animal (plural):")
adj3 = raw_input("Adjective meaning large:")
noun3 = raw_input("Pick a bug:")
verb = raw_input("Past tense action verb that can be done to another person:")
name = raw_input("Your name:")

# storytime!
story = "On " + day + " night, America watched as " + vp1 + " and " + vp2 + " took the debate stage on " + adj1 + " television. " \
"Both candidates got " + num + " minutes to answer each question. " + vp1 + " said that she wanted to help " + noun1 + ". " \
+ vp2 + " interrupted to say " + adj2 + " " + noun2 + " were more important. Then suddenly, a " + adj3 + " " + noun3 + " landed on " + vp2 + "'s head. " \
"The " + noun3 + " " + verb + " " + vp2 +"! " + name + " decided to vote for " + vp1 + "."


# hot off the presses...
print ("~~~~~~~~~~~~~~~~~ Story by " + name + " ~~~~~~~~~~~~~~~~~")
print (story)