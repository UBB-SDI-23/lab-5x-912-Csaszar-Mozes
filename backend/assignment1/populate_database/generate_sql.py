from generate_pc import generate as generate_pcs
from generate_people import generate as generate_ps
from generate_companies import generate as generate_cs
from generate_locations import generate as generate_ls
from generate_users import generate as generate_usups


def generate_all(nr_users=10000, nr_people=3000000, nr_companies=1000000):
    chances = [0.9, 0.097, 0.0027, 0.000297, 0.000003]
    chances_added = [0]
    for i in range(len(chances)):
        chances_added.append(chances_added[i] + chances[i])
    chances_added.append(1)
    nr_people_in_comp = [1, 15, 45, 180, 455, 1300]
    nr_locations_in_comp = [1, 2, 4, 10, 25, 100]
    net_values = [100, 1000, 15764, 547895, 7845962, 54687514]
    salaries = [100, 250, 2500, 25000, 180000, 600000]
    reputations = [20, 60, 70, 80, 90, 100]

    #generate_cs(nr_companies, chances_added, reputations, net_values, nr_users)
    #generate_ps(nr_people, nr_users)
    #generate_ls(chances_added, nr_locations_in_comp, [1, nr_companies])
    generate_pcs(chances_added, salaries, nr_people_in_comp, nr_users, [1, nr_people], [1, nr_companies])

    generate_usups(nr_users)


generate_all(10000, 1000000, 1000000)
