def check_answer(characters):
    for character, phrase in characters:
        print(f'У вашего персонажа есть фраза: "{phrase}"(y/n)?')
        answer = input()
        if answer == 'y':
            print(f"Ваш персонаж {character[2:]}")
            break
    else:
        print("Другие реплики я не знаю, возможно вы ошиблись мультиком")


def main():
    file = open('Akinator.txt', 'r', encoding='utf-8')
    characters = {}
    cartoon = ""
    while True:
        line = file.readline()
        if not line:
            break
        if line == "---\n":
            line = file.readline()
            characters[line] = []
            cartoon = line
        else:
            characters[cartoon].append(tuple(line.split(":")))
    i = 1
    unit_to_multiplier = {}
    for question in characters:
        print(f'{i}) {question[:-2]}')
        unit_to_multiplier[i] = question
        i += 1
    choice = int(input("Введите номер мультика\n"))
    if choice in unit_to_multiplier.keys():
        check_answer(characters[unit_to_multiplier[choice]])
    else:
        print("Введите номер мультика из списка")


if __name__ == '__main__':
    main()
