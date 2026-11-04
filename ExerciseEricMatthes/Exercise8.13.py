# Exercise 8.13
def build_profile(first, last, **user_info):
    """Bangun dictionary berisi semua info tentang user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


my_profile = build_profile('fikri', 'ramadhan',
                           university='UNS',
                           major='Teknik Industri',
                           hometown='Banyumas')
print(my_profile)
