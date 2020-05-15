def repeatedString(s, n):
    pass

    # what happens when the repeated string's length > n

    # construct our n-length string
    # do we even actually need to construct the string?
    # we need to count the number of "a"s
    # loop through our n-length string and keep a counter for the number of "a"s

    # instead of wasting memory creating the n-length string, what we could
    # do instead is cycle through the initial string we're given
    # count the number of "a"s while we're doing that

    # could we do an n-length slice with Python's slice operator?
    # seems like no, the slice operator won't cycle through the string
    # by default
    # if we wanted to use the slice operator, we'd have to extend the
    # string, which would take up some additiional memory

    # (n // len(s)) * s.count() + s[n % len(s)].count
    # figure out how many times we can repeat the string s in its entirety
    # to fit in n
    # plus we have to figure out the "remainder", or how many more characters
    # in s we need to reach n if len(s) does not cleanly divide n
