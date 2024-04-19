letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z',]
def chipher(text, fase):
    text_list = list(text.lower())

    for i in range(len(text_list)):
        index = letters.index(text_list[i])
        index_fase = index + fase
        if index_fase <= len(letters):
            text_list[i] = letters[index_fase]
        if index_fase > len(letters):
            text_list[i] = letters[index_fase - len(letters)]
    str1 = ''.join(text_list)
    print(str1)


if __name__ == '__main__':
    print("helloworld")
    chipher("helloworld", 3)
