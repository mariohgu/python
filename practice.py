def search_str(string:str):
    lower_case=[x for x in string if x.islower()]
    upper_case = [y for y in string if y.isupper()]
    print(f'The lowercases are: {lower_case} and \nthey are: {len(lower_case)}')
    print(f'The uppercases are {upper_case} and \nthey are: {len(upper_case)}')

def hiy(hey:str):
    return "ya" if hey=="r" else "no"

def run():
    search_str("Welcome to the World of Possibilities!")
    print(hiy("uu"))



if __name__ == '__main__':run()