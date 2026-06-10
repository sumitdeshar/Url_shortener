import random
import string
from .models import Link

from django.db.models import F
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
    while True:
        random_indices = random.sample(range(0, 62), k=shortcode_length)
        candidate = "".join([lookup_table[str(num)] for num in random_indices])

        if not Link.objects.filter(short_link=candidate).exists():
            return candidate

def build_short_url(shortcode, user_domain=None):
    base_domain = user_domain or "chotkari.com"

    if base_domain.startswith("http"):
        return f"{base_domain.rstrip('/')}/{shortcode}"

    return f"https://{base_domain.strip('/')}/{shortcode}"



def increment_click(link_id):
    Link.objects.filter(id=link_id).update(
        click_count=F("click_count") + 1
    )

def increment_click_from_cache(shortcode):
    link = Link.objects.filter(short_link=shortcode).first()
    if link:
        Link.objects.filter(id=link.id).update(
            click_count=F("click_count") + 1
        )