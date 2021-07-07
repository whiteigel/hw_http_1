import requests

def search_name(superhero):
    name = superhero
    url = f'https://superheroapi.com/api/2619421814940190/search/{name}'
    response = requests.get(url=url)
    if response.status_code != 200:
        print("ERROR")
        return
    res = response.json()['results']
    for ind, elm in enumerate(res):
        name = elm['name']
        # id = elm['id']
        intelligence = elm['powerstats']['intelligence']
        stats = {}
        stats[name] = intelligence
        return stats

def compare_heros(heroes):
    dict_hero = {}
    for ind, hero in enumerate(heroes):
        # print(hero)
        for s_hero, stat in hero.items():
            dict_hero[s_hero] = int(stat)
    super_intel_hero = max(dict_hero, key=dict_hero.get)
    return f'Самый умный из супер-героев: {super_intel_hero}'

if __name__ == '__main__':
    heroes_list = [search_name('Hulk'), search_name('Thanos'), search_name('Captain America')]
    print(compare_heros(heroes_list))

