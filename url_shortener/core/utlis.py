import random
import string

from .models import ShortCode
    
def generate_lookup():
    
    alphanumeric_characters = string.ascii_lowercase + string.digits + string.ascii_uppercase

    char_list = list(alphanumeric_characters)
    random.shuffle(char_list)

    randomized_characters = "".join(char_list)

    return {index: char for index, char in enumerate(randomized_characters)}


shortcode_length = random.randint(7,10)
shortcode_length = 5

# hash_dict = generate_lookup()

def createshortcode(shortcode_length, lookup_table):
    msg={}
    while True:
        sample_num_list = random.sample(range(0, 62), k=shortcode_length)
        shortcode = "".join([lookup_table[num] for num in sample_num_list])

        if not ShortCode.objects.filter(short_code=shortcode).exists():
            ShortCode.objects.create(short_code=shortcode)
            msg['shortcode'] = shortcode
            msg['utlis_msg'] = "Shortcode created and added to database"
            return msg


# res = createshortcode(shortcode_length)

def generate_url(shortcode):
    url = 'http://chotkarily/'
    new_url = url + shortcode
    return new_url
