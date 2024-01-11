def Lisamine(i:list,p:list,k:int): 
    """Andmete lisamine listidesse
    Tagastab listud

    :param list i: Inimesta nimekiri
    :param list p: Palkage loetelu
    :param int k: Inemeste kogus
    :rtype:list, list
    """
    for i in range(k):
        nimi=input("Mis on inimese nimi?")
        palk=int(input("Kui suur palk tal on? "))
        i.append(nimi)
        p.append(palk)
    return i,p


# 5 teema. funktsioonid (file in moodle)