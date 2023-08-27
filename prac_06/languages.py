"""
estimate time: 30 minutes
actual time: 20 minutes
"""
from prac_06.programming_language import ProgrammingLanguage


def main():
    """main function"""
    languages = []
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    print(ruby)
    print(visual_basic)
    languages.append(python)
    languages.append(ruby)
    languages.append(visual_basic)
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
