customers_age = 10
movie_time = 1400
movie_ticket_price = 1000

if customers_age <= 12:
    discounted_price = movie_ticket_price - (movie_ticket_price*50/100)
    print(f"Price of the movie is {discounted_price}")

elif customers_age >= 60:
    discounted_price = movie_ticket_price - (movie_ticket_price * 30 / 100)
    print(f"Price of the movie is {discounted_price}")

elif movie_time < 1700:
    discounted_price = movie_ticket_price - (movie_ticket_price * 20 / 100)
    print(f"Price of the movie is {discounted_price}")

else:
    print(f"Price of the movie ticket is {movie_ticket_price}")

