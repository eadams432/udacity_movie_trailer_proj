import media,fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A toy story",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

her = media.Movie("Her"
                  ,"Guy falls in love with operating system"
                  ,"https://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg"
                  ,"https://www.youtube.com/watch?v=ne6p6MfLBxc")


fantastic_mr_fox = media.Movie("Fantastic Mr. Fox"
                               ,"Animal friends plan to rob farmers.  Chaos ensues"
                               ,"https://upload.wikimedia.org/wikipedia/en/a/af/Fantastic_mr_fox.jpg"
                               ,"https://www.youtube.com/watch?v=n2igjYFojUo")

bridesmaids = media.Movie("Bridesmaids"
                          ,"A woman tries to cope with her friend getting married"
                          ,"https://upload.wikimedia.org/wikipedia/en/d/df/BridesmaidsPoster.jpg"
                          ,"https://www.youtube.com/watch?v=FNppLrmdyug")


movie_list = [toy_story,her,fantastic_mr_fox,bridesmaids]

fresh_tomatoes.open_movies_page(movie_list)
