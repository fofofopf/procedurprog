def find_common_participants(a, b, c=','):
    a = a.split(c)
    b = b.split(c)
    x = list(set(a) & set(b))
    return sorted(x)



participants_first_group = 'Иванов,Петров,Сидоров'
participants_second_group = "Петров,Сидоров,Смирнов"
print(find_common_participants(participants_first_group, participants_second_group))
