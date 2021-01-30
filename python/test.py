with open("./data/tweet_data_ea.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print i, repr(line)