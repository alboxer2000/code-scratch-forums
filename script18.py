# script 1
data = "spam"
with open("/path/to/eggs.file", w) as f:
    f.write(data) # the 4 spaces can be interchanged with tabs, but WHITESPACE MUST REMAIN CONSISTENT (so, no mixing spaces and tabs)

# script 2
with open("/path/to/eggs.file", r) as f: # make sure you keep the write path and the read path EXACTLY the same, to help with this, make a variable and store the path there.
    f.read() # ditto as on the code block above, make sure you don't mix indents and all that
