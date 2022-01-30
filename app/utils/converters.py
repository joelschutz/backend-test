def kebab_to_title(target: str):
    return ' '.join([s.capitalize() for s in target.split('-')])

def title_to_kebab(target: str):
    return target.strip().replace(" ", "-").lower()