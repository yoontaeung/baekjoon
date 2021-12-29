if __name__ == '__main__':
    case = int(input())
    word = []
    for i in range(case):
        word.append(input())
    word.sort()
    dictionary = {}

    for j in range(case):
        dictionary[word[j]] = len(word[j])
    sorted_dict = sorted(dictionary.items(), key=lambda item: item[1])
    for k in range(len(sorted_dict)):
        print(sorted_dict[k][0])
