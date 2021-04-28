format_title = '{:^0}\t{:^12}\t{:^8}\t{:^8}\t{:^10}'
format_data = '{:^0}\t{:^12}\t{:^8}\t{:^8}\t{:^10}'


def add(info):
    while True:
        flag = False
        Id = int(input('请输入学生编号:'))
        name = input('请输入学生姓名:')
        age = int(input('请输入学生年龄:'))
        sex = input('请输入学生性别(男/女):')
        score = int(input('请输入学生成绩:'))
        for i in info:
            if Id == i['id']:
                flag = True
                break
        if flag:
            input('该学生编号已存在，无法添加该学生')
            break
        info += [{'id': Id, 'name': name, 'age': age, 'sex': sex, 'score': score}]
        q = input('学生添加成功，按回车继续，输入q并按回车退出：')
        if q == 'q':
            break
    return info


def show(info):
    if len(info) == 0:
        input("暂时没有学生信息,按任意键返回")
        return

    print(format_title.format('编号', '姓名', '年龄', '性别', '成绩'))

    for i in info:
        print(format_data.format(i.get('id'), i.get('name'), i.get('age'), i.get('sex'), i.get('score')))
    input('按任意键返回主菜单')


def delete(info):
    flag = 0
    count = 0
    print("删除学生信息")
    Id = int(input('请输入要删除的学生编号(输入0返回)：'))
    if Id == 0:
        return
    for i in info:
        if i['id'] == Id:
            del info[count]
            flag = 1
            input('删除成功，按任意键返回')
        count += 1
    if flag == 0:
        print('没有找到id为', Id, '的学生，按任意键返回', end='')
        input()


def update(info):
    flag = 0
    print("修改学生信息")
    Id = int(input('请输入要修改的学生编号(输入0返回)：'))
    if Id == 0:
        return
    for i in info:
        if i['id'] == Id:
            flag = 1
            name = input('请输入学生姓名:')
            age = int(input('请输入学生年龄:'))
            sex = input('请输入性别(男/女):')
            score = input('请输入学生成绩:')
            i['name'] = name
            i['age'] = age
            i['sex'] = sex
            i['score'] = score
            input('学生信息修改成功，按任意键继续')
    if flag == 0:
        print('没有找到id为', Id, '的学生,按任意键返回', end='')
        input()


def sort(info):
    x = sorted(info, key=lambda info: info['score'])
    print('按成绩倒序')
    print(format_title.format('编号', '姓名', '年龄', '性别', '成绩'))
    for i in x:
        print(format_data.format(i.get('id'), i.get('name'), i.get('age'), i.get('sex'), i.get('score')))
    input('按任意键返回主菜单')

