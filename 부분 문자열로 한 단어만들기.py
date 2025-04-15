def hidden_word (words, slices):
    answer = ""
    for word, range in zip(words,slices):
        answer += "".join([word[start:end+1] for start,end in range])
    return answer




words = ["apocalypse","meteorology","architect","cheetah"]
slices = [[(1, 2), (5, 6)],[(2, 3)],[(2, 2)],[(1, 1)]]

print(hidden_word(words, slices))