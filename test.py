str = 'As the country became embroiled in a domestic crisis, the first government was dislodged and succeeded by several different administrations. Bolikango served as Deputy Prime Minister in one of the new governments before a partial state of stability was reestablished in 1961. He mediated between warring factions in the Congo and briefly served once again as Deputy Prime Minister in 1962 before returning to the parliamentary opposition. After Joseph-Desire Mobutu took power in 1965, Bolikango became a minister in his government. Mobutu soon dismissed him but appointed him to the political bureau of the Mouvement Populaire de la Revolution. Bolikango left the bureau in 1970. He left Parliament in 1975 and died seven years later. His grandson created the Jean Bolikango Foundation in his memory to promote social progress. The President of the Congo posthumously awarded Bolikango a medal in 2005 for his long career in public service.'

word_list = str.replace(',', ' ').replace('.', ' ').split()
# print(word_list)

word_list_no_duplicate = list(set(word_list))
# print(word_list_no_duplicate)

# for i, word in enumerate(word_list_no_duplicate):
#     print(i, word)

word_count = []
for word in word_list_no_duplicate:
    word_count.append((word_list.count(word), word))

n = 0
for result in sorted(word_count, reverse=True):
    n += 1
    print(result[1], ':', result[0])
    if n == 10:
        break
