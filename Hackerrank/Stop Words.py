def stopWords(text, k):
    import collections
    sentence = text
    words = sentence.split()
    result = []
    first_occurrence = []
    word_counts = collections.Counter(words)
    for word, count in sorted(word_counts.items()):
        if count >= k:
            result.append(word)
            # print('"%s" is repeated %d time%s.' % (word, count, "s" if count > 1 else ""))
    for word in words:
        if word in result and not word in first_occurrence:
            first_occurrence.append(word)
    return first_occurrence


if __name__ == '__main__':
    text = "the quick brown fox jumps over the lazy brown dog and runs away to a brown house"

    k = 2

    result = stopWords(text, k)
    print(result)

