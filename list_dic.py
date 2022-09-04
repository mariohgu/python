def run():
    super_list = [
        {"name":"mario", "lastname":"figueroa"},
        {"name":"doris", "lastname":"jimenez"},
        {"name":"juan", "lastname":"figueroa"},
        {"name":"leslie", "lastname":"figueroa"}
    ]
    
    super_dicc = {
        "natural":[1,2,3,4],
        "integer":[-4,-6,0,-3,4],
        "floating":[2.5,3.9,7.4,3,4]
    }
    
    for key,values in super_dicc.items():
        print(f'{key} and {values}')
        



if __name__== '__main__':
    run()

