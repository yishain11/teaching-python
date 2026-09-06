import deepl
import dotenv
import os
import questionary as q

dotenv.load_dotenv()


def get_translation_main(txt):
    target_lang = ask_for_traget_lang().split(" ")[0]
    translation = get_translation(txt, target_lang)
    show_translation_results(translation, target_lang)


def ask_for_traget_lang():
    answer = q.select(
        "What language do you want to translate into? ",
        choices=["HE - hebrew", "CA - catalan", "DE - german"],
    ).ask()
    return answer


def setup_translation_client():
    auth_key = os.getenv("DEEPL_KEY")
    if not auth_key:
        print("no auth key for translation!")
        return
    deepl_client = deepl.DeepLClient(auth_key)
    return deepl_client


def get_translation(text, target_lang):
    client = setup_translation_client()
    if not client:
        return
    result = client.translate_text(text, target_lang=target_lang)
    return result.text


def show_translation_results(translation, target_lang):
    if target_lang.upper() == "HE":
        translation = translation[::-1]
    print(translation)
