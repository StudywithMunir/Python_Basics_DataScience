# Branching with if, elif, and else

# Real-world example problem: Determine the category of a movie based on its rating.
# If the rating is greater than or equal to 8, it's an "Excellent" movie.
# If the rating is between 6 and 8 (inclusive), it's a "Good" movie.
# Otherwise, it's a "Average" movie.

def categorize_movie(rating):
    if rating >= 8:
        return "Excellent"
    elif rating >= 6:
        return "Good"
    else:
        return "Average"

movie_rating = 7.5
movie_category = categorize_movie(movie_rating)
print(f"The movie with a rating of {movie_rating} is categorized as '{movie_category}'.")


"""
age=13
if age>=18:
print("you are an adult")
print("you can vote")
elif age < 3:
print("you are achild")
else:
print("you are in school")
print("thank you")

"""



"""
#OurCalculator
first=input("Enterfirstnumber:")
second=input("Entersecondnumber:")
first=int(first)

second=int(second)
print("----press  keys foroperator(+,-,*,/,%)----------")
operator=input("Enter operator:")
if operator=="+":
print(first+second)
elif operator=="-":
print(first-second)
elif operator=="*":
print(first*second)
elif operator=="/":
print(first/second)
elif operator=="%":
print(first%second)
else:
print("InvalidOperation")

"""