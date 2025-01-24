data Hello = Hello
instance Show Hello where
    show _ = "Hello, World!"
main = pure Hello >>= print
