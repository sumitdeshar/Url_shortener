import random
import string
    
def generate_lookup():
    
    alphanumeric_characters = string.ascii_lowercase + string.digits + string.ascii_uppercase

    char_list = list(alphanumeric_characters)
    random.shuffle(char_list)

    randomized_characters = "".join(char_list)

    return {index: char for index, char in enumerate(randomized_characters)}


shortcode_length = random.randint(7,10)
shortcode_length = 5


def createshortcode(shortcode_length):
    sample_num_list = random.sample(range(0,62),k=shortcode_length)
    shortcode = "".join([hash_dict[num] for num in sample_num_list])
    print(shortcode )

# hash_dict = generate_lookup()

# res = createshortcode(shortcode_length)

def generate_url(shortcode):
    url = 'http://chotkarily/'
    
    new_url = url.join(shortcode)
