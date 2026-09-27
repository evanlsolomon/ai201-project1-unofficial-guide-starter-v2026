import string


def judge(question, expects, answer, results) -> bool:

    STOPWORDS = {
        "a", "an", "the", "is", "are", "was", "of", "to", "in", "on", "for", "and",
        "or", "it", "be", "at", "by", "with", "you", "your", "can", "per", "that",
    }

    # Create a translation table to map punctuation to None
    clean_expects = expects.translate(
        str.maketrans("", "", string.punctuation))
    clean_answer = answer.translate(str.maketrans("", "", string.punctuation))

    ans_words = clean_answer.split()
    expects_words = clean_expects.split()
    ans_words_without_stops = [t for t in ans_words if t not in STOPWORDS]
    expects_words_without_stops = [
        t for t in expects_words if t not in STOPWORDS]

    hits = 0

    for word in ans_words_without_stops:
        if word in expects_words_without_stops:
            hits += 1
            return True

    # if at least 50% of expected keywords are present in the answer keywords, we consider it correct
    return hits/len(expects_words_without_stops) >= 0.5
