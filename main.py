'''fichier = main.py'''

#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """Retourne le contenu du fichier <filename> sous forme d'une liste de listes d'entiers.

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 liste par ligne)
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f:
        for line in f:
            # Supprimer les espaces vides en début et fin de ligne
            # Diviser la ligne sur le point-virgule pour obtenir une liste de chaînes
            # Convertir chaque élément en entier
            l.append([int(x) for x in line.strip().split(';')])
    return l


def get_list_k(data, k):
    '''retourne la liste d'indice k'''
    return data[k]

def get_first(l):
    '''retourne le premier élement'''
    return l[0]

def get_last(l):
    '''retourne le dernier élement'''
    return l[-1]

def get_max(l):
    '''retourne le plus grand élement'''
    return max(l)

def get_min(l):
    '''retourne le plus petit élement'''
    return min(l)

def get_sum(l):
    '''retourne la somme des élement'''
    return sum(l)


#### Fonction principale


def main():
    '''foncTion principale'''
    # data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    # k = 37
    # print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
