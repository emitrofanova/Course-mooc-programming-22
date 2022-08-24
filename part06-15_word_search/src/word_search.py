# Write your solution here
def find_words(search_term: str):
    with open("words.txt") as f:
        answ = []
        if "." in search_term:
            for line in f:
                line = line.replace("\n", "")
                cnt = -1
                cnt2 = 0
                cnt3 = 0
                if len(line) == len(search_term):
                    for ch in search_term:
                        cnt += 1
                        if ch != ".":
                            if ch == line[cnt]:
                                cnt3 += 1
                        else:
                            cnt2 += 1
                        if cnt3 == (len(search_term) - cnt2):
                                answ.append(line)
        elif search_term.startswith("*"):
            for line in f:
                line = line.replace("\n", "")
                if search_term[1:] == line[len(line) - len(search_term) + 1:]:
                    answ.append(line)
        elif search_term.endswith("*"):
            for line in f:
                line = line.replace("\n", "")
                if search_term[:len(search_term) - 1] == line[:len(search_term) - 1]:
                    answ.append(line)
        else:
            for line in f:
                line = line.replace("\n", "")
                if search_term == line:
                    answ.append(search_term)
    return answ

if __name__ == "__main__":
    print(find_words("*vokes"))
    print(find_words("voy*"))
    print(find_words("ca."))
    print(find_words("sale"))
