from jokeapi_fns import get_joke_main
from translation_fns import get_translation_main


def main():
    joke_txt = get_joke_main()
    if joke_txt:
        get_translation_main(joke_txt)


main()
