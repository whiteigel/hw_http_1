import requests

class Superhero:
    def __init__(self, name):
        self.name = name

    def search_name(self):
        name = self.name
        url = f'https://superheroapi.com/api/2619421814940190/search/{name}'
        response = requests.get(url=url)
        if response.status_code != 200:
            print("ERROR")
        intel = response.json()['results'][0]['powerstats']['intelligence']
        name = response.json()['results'][0]['name']
        stats = {}
        stats[name] = int(intel)
        return stats

    def compare_heros(self, heroes):
        dict_hero = {}
        for ind, hero in enumerate(heroes):
            for s_hero, stat in hero.items():
                dict_hero[s_hero] = int(stat)
        super_intel_hero = max(dict_hero, key=dict_hero.get)
        return f'Самый умный из супер-героев: {super_intel_hero}'

if __name__ == '__main__':
    thanos = Superhero("Thanos")
    hulk = Superhero("Hulk")
    captain = Superhero("Captain America")
    heroes_list = [thanos.search_name(), hulk.search_name(), captain.search_name()]
    print(hulk.compare_heros(heroes_list))



