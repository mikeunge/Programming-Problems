#!/bin/usr/python3 *
#-*- coding: utf-8 -*-

def destruct(sentence):
    try:
        sentence_arr = sentence.split(" ")
        return sentence_arr
    except Exception as ex:
        print(str(ex))
        exit(1)


def modify(arr):
    new_arr = []
    for elem in arr:
        elem_list = list(elem)
        if len(elem_list) != 0:
            elem_list.append(elem_list[0])
            elem_list.pop(0)
            elem = ''.join(elem_list) + 'ay'
            new_arr.append(elem)
    return new_arr


def construct(arr):
    return ' '.join(arr)


def main():
    sentence = input("Sentence to change: ")
    destructed_sentence = destruct(sentence)
    modified_sentence = modify(destructed_sentence)
    constructed_sentence = construct(modified_sentence)
    print(constructed_sentence)


if __name__ == '__main__':
    main()