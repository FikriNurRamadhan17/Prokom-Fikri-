# Exercise 8.12
def make_sandwich(*items):
    """Ringkas bahan sandwich yang dipesan."""
    print("\nSandwich dengan bahan:")
    for item in items:
        print(f"- {item}")


make_sandwich('keju')
make_sandwich('ayam', 'selada', 'tomat')
make_sandwich('tuna', 'mayones', 'timun', 'telur')
