# load data
text = sc.textFile("hdfs:///user/lsda/lsda.txt")

# apply transformations
words = text.flatMap(lambda line: line.split(" "))
words_hadoop = text.filter(lambda w: "hadoop" in w.lower())
words_love = text.filter(lambda w: "love" in w.lower())
words_both = words_hadoop.union(words_love)

# apply action
words_both.count()
