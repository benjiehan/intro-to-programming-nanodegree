import media
import fresh_tomatoes

# Mullholland Dr. movie: movie title, storyline, poster image and movie trailer
mullholland_dr = media.Movie(
    "Mullholland Dr.",
    "After a car wreck on the winding Mulholland Drive renders a woman "
    "amnesiac, she and a perky Hollywood-hopeful search for "
    "clues and answers across "
    "Los Angeles in a twisting venture beyond dreams and reality.",
    "https://upload.wikimedia.org/wikipedia/en/0/0f/Mulholland.png",  # NOQA
    "https://youtu.be/7KgH9n1c4mM"
    )

# The Fountain movie: movie title, storyline, poster image and movie trailer
the_fountain = media.Movie(
    "The Fountain",
    "As a modern-day scientist, Tommy is struggling with mortality, "
    "desperately searching for the medical breakthrough that will "
    "save the life of his cancer-stricken wife, Izzi.",
    "https://upload.wikimedia.org/wikipedia/en/e/ee/Fountain_poster_1.jpg",  # NOQA
    "https://youtu.be/F0yxCLznEqs"
    )

# Paprika movie: movie title, storyline, poster image and movie trailer
paprika = media.Movie(
    "Paprika",
    "When a machine that allows therapists to enter their patients' "
    "dreams is stolen, all Hell breaks loose. Only a young "
    "female therapist, Paprika, can stop it.",
    "https://upload.wikimedia.org/wikipedia/en/1/16/Paprikaposter.jpg",  # NOQA
    "https://youtu.be/yn7U1KIGeuQ"
    )

# The Prestige movie: movie title, storyline, poster image and movie trailer
the_prestige = media.Movie(
    "The Prestige",
    "After a tragic accident two stage magicians engage in a battle "
    "to create the ultimate illusion whilst sacrificing everything "
    "they have to outwit the other.",
    "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",  # NOQA
    "https://youtu.be/9n2B5WW4SKk"
    )

# Unbrekable movie: movie title, storyline, poster image and movie trailer
unbreakable = media.Movie(
    "Unbreakable",
    "A man learns something extraordinary about himself after a "
    "devastating accident.",
    "https://upload.wikimedia.org/wikipedia/en/9/9e/Unbreakableposterwillis.jpg",  # NOQA
    "https://youtu.be/R_f1uCWKZQs"
    )

# Fight Club movie: movie title, storyline, poster image and movie trailer
fight_club = media.Movie(
    "Fight Club",
    "An insomniac office worker, looking for a way to change his life, "
    "crosses paths with a devil-may-care soap maker, forming an "
    "underground fight club that evolves into something much, much more.",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",  # NOQA
    "https://youtu.be/BdJKm16Co6M"
    )

# Donnie Darko movie: movie title, storyline, poster image and movie trailer
donnie_darko = media.Movie(
    "Donnie Darko",
    "A troubled teenager is plagued by visions of a man in a "
    "large rabbit suit who manipulates him to commit a series "
    "of crimes, after he narrowly escapes a bizarre accident.",
    "https://upload.wikimedia.org/wikipedia/en/d/db/Donnie_Darko_poster.jpg",  # NOQA
    "https://youtu.be/rPeGaos7DB4"
    )

# Oldboy movie: movie title, storyline, poster image and movie trailer
oldboy = media.Movie(
    "Oldboy",
    "After being kidnapped and imprisoned for fifteen years, Oh Dae-Su "
    "is released, only to find that he must find his captor in five days.",
    "https://upload.wikimedia.org/wikipedia/en/6/67/Oldboykoreanposter.jpg",  # NOQA
    "https://youtu.be/2HkjrJ6IK5E"
    )

# Primer movie: movie title, storyline, poster image and movie trailer
primer = media.Movie(
    "Primer",
    "Four friends/fledgling entrepreneurs, knowing that there's something "
    "bigger and more innovative than the different error-checking devices "
    "they've built, wrestle over their new invention.",
    "https://upload.wikimedia.org/wikipedia/en/f/f7/Primer_%282004_film_poster%29.jpg",  # NOQA
    "https://youtu.be/dfOCp6cW7rQ"
    )

# Memento movie: movie title, storyline, poster image and movie trailer
memento = media.Movie(
    "Memento",
    "A man juggles searching for his wife's murderer and keeping his "
    "short-term memory loss from being an obstacle.",
    "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",  # NOQA
    "https://youtu.be/0vS0E9bBSL0"
    )

# Black Swan movie: movie title, storyline, poster image and movie trailer
black_swan = media.Movie(
    "Black Swan",
    "A committed dancer wins the lead role in a production of Tchaikovsky's "
    "\"Swan Lake\" only to find herself struggling to maintain her sanity.",
    "https://upload.wikimedia.org/wikipedia/en/6/68/Black_Swan_poster.jpg",  # NOQA
    "https://youtu.be/5jaI1XOB-bs"
    )

# The Machinist movie: movie title, storyline, poster image and movie trailer
the_machinist = media.Movie(
    "The Machinist",
    "An industrial worker who hasn't slept in a year begins to "
    "doubt his own sanity.",
    "https://upload.wikimedia.org/wikipedia/en/b/b9/The_Machinist_poster.JPG",  # NOQA
    "https://youtu.be/bAhBZXw1Kak"
    )

# Set the movies that will be passed to the media file
movies = [
    mullholland_dr,
    the_fountain,
    paprika,
    the_prestige,
    unbreakable,
    fight_club,
    donnie_darko,
    oldboy,
    primer,
    memento,
    black_swan,
    the_machinist
    ]

# Open the HTML file in a web browser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
