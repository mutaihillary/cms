def Content():
    # MAIN : [TITLE, URL, BODY_TEXT (LIST), HINTS(LIST)]
    TOPIC_DICT = {"Basics": [["Python Introduction", "/introduction-to-python-programming/", [""]],
                             ["Print Function and Strings", "/python-tutorial-print-function-strings/",
                              ["The Print function outputs text to the console (black area). Let's try it out!",
                               "print() is a function, which does something with parameters, and parameters go inside the parenthesis.",
                               "See if you can use the print function to output 'Hello!' to the console!"]],
                             ["Math with Python", "/math-basics-python-3-beginner-tutorial/"],
                             ["Variables", "/python-3-variables-tutorial/"],
                             ["While Loop", "/python-3-loop-tutorial/"],
                             ["For Loop", "/loop-python-3-basics-tutorial/"],
                             ["If Statement", "/if-statement-python-3-basics-tutorial/"],
                             ["Threaded Port Scanner", "/python-threaded-port-scanner/"],
                             ["Binding and Listening with Sockets", "/python-binding-listening-sockets/"],
                             ["Client Server System with Sockets", "/client-server-python-sockets/"],
                             ["Python 2to3 for Converting Python 2 scripts to Python 3",
                              "/converting-python2-to-python3-2to3/"]],

                  # // suggest pyopengl next //

                  "MySQL": [["Intro to MySQL", "/mysql-intro/"],
                            ["Creating Tables and Inserting Data with MySQL", "/create-mysql-tables-insert/"],
                            ["Update, Select, and Delete with MySQL", "/mysql-update-select-delete/"],
                            ["Inserting Variable Data with MySQL", "/mysql-insert-variable/"],
                            ["Streaming Tweets from Twitter to Database",
                             "/mysql-live-database-example-streaming-data/"], ],

                  "SQLite": [
                      ["Inserting into a Database with SQLite", "/sql-database-python-part-1-inserting-database/"],
                      ["Dynamically Inserting into a Database with SQLite",
                       "/sqlite-part-2-dynamically-inserting-database-timestamps/"],
                      ["Read from Database with SQLite", "/sqlite-part-3-reading-database-python/"],
                      ["Graphing example from SQLite", "/graphing-from-sqlite-database/"], ],



                  }

    return TOPIC_DICT


if __name__ == "__main__":
    x = Content()

    print(x["Basics"])

    for each in x["Basics"]:
        print(each[1])

