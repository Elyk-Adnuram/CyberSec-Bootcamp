"""Iterate list and display each list item and its index position"""

fav_movies = ['Anchorman', 'Dune', 'Interstellar', 'Inception', 'The Other Guys']

# Iterate list and print each list item and index 
for index, movie in enumerate(fav_movies):
    # condition to ensure comma is not added to the end of last movie title
    if index != len(fav_movies) - 1:
        print(f'Movie {index + 1}: {movie}, ', end='')
    else:
        print(f'Movie {index + 1}: {movie}', end='')
