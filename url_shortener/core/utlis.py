import random
import string

from .models import UsedShortcode
    
def build_char_map():
    
    alphanumeric_characters = string.ascii_lowercase + string.digits + string.ascii_uppercase

    char_list = list(alphanumeric_characters)
    random.shuffle(char_list)

    randomized_characters = "".join(char_list)

    return {index: char for index, char in enumerate(randomized_characters)}


shortcode_length = random.randint(7,10)

# hash_dict = generate_lookup()

def generate_shortcode(shortcode_length, lookup_table):
    result={}
    while True:
        random_indices = random.sample(range(0, 62), k=shortcode_length)
        candidate = "".join([lookup_table[str(num)] for num in random_indices])

        if not UsedShortcode.objects.filter(short_code=candidate).exists():
            UsedShortcode.objects.create(short_code=candidate)
            result['shortcode'] = candidate
            result['utlis_result'] = "Shortcode created and added to database"
            return result


# res = createshortcode(shortcode_length)

def build_short_url(shortcode,user_domain):
    domain = "Chotkari"
    if user_domain:
        domain = user_domain
    
    short_url = f"https://{domain}.com/{shortcode}"
    return short_url
