# You've built an inflight entertainment system with on-demand movie streaming.
# Users on longer flights like to start a second movie right when their first one ends, but they complain that the plane usually lands before they can see the ending. So you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.

# Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

# When building your function:

# Assume your users will watch exactly two movies
# Don't make your users watch the same movie twice
# Optimize for runtime over memory


def two_inflight_movies(fl_length, mov_lengths):
    # write the body of your function here
    # mov_lengths_seen = set()
    
    for i in mov_lengths:
        sec_mov_search = fl_length - i
        if sec_mov_search in mov_lengths:
            print sec_mov_search, i
            return True
    
                
    return False

# run your function through some test cases here
# remember: debugging is half the battle!
print two_inflight_movies(300, [90, 90, 120, 85, 60, 140, 160])
print two_inflight_movies(250, [150, 40, 60, 90])
print two_inflight_movies(360, [150, 210, 300, 60])