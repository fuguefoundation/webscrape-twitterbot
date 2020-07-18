with open("tweet_data_LIFE.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print i, repr(line)