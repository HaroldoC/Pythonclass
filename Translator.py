from translate import Translator

translator = Translator(to_lang="ja")
try:
    with open("Pythonclass\Read,Write, Append.txt", mode="r") as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open("Pythonclass\Read,Write, Append-ja.txt", mode="w") as my_file2:
            my_file2.write(translation)
            print(translation)
except FileNotFoundError as err:
    print("File does not exist")
    raise err
else:
    print("Success")
