import re
import os
import shutil

def write_words_to_file(words, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f_out:
            f_out.writelines(f"{word}\n" for word in words)
    except Exception as e:
        print(f"Fout bij het schrijven naar '{filename}': {e}")
        return False
    return True

def filter_gronings_wordlist(input_filename, output_filename, regex_pattern, description=""):
    if not os.path.exists(input_filename):
        print(f"Fout: Bestand '{input_filename}' niet gevonden.")
        return False, False

    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f]
    except Exception as e:
        print(f"Fout bij lezen van '{input_filename}': {e}")
        return False, False

    matched_words = [word for word in words if re.search(regex_pattern, word)]
    print(f"\n--- Filter: {description} ---")
    print(f"{len(matched_words)} {description} gevonden.")

    if matched_words:
        print("Gevonden woorden:", ', '.join(matched_words))
    else:
        print(f"Geen {description} gevonden.")
        return write_words_to_file(words, output_filename), False

    print("\nWat wil je doen met deze woorden?")
    print("1. Alles verwijderen")
    print("2. Alles behouden")
    print("3. Eén voor één controleren (typ 'f' om te stoppen)")

    choice = input("Maak een keuze (1, 2 of 3): ").strip()
    words_to_keep = []

    skip_remaining_filters = False

    if choice == '1':
        words_to_keep = [w for w in words if w not in matched_words]
    elif choice == '2':
        words_to_keep = words
    elif choice == '3':
        skip_checking = False
        for word in words:
            if word in matched_words and not skip_checking:
                answer = input(f"'{word}' verwijderen? (j/n, of 'f' om te stoppen): ").strip().lower()
                if answer == 'f':
                    print("Beoordeling voortijdig gestopt. De rest van de woorden worden behouden.")
                    skip_checking = True
                    skip_remaining_filters = True
                    words_to_keep.append(word)
                elif answer != 'j':
                    words_to_keep.append(word)
                # bij 'j' wordt het woord niet toegevoegd
            else:
                words_to_keep.append(word)
    else:
        print("Ongeldige keuze. Geen wijzigingen toegepast.")
        return write_words_to_file(words, output_filename), False

    success = write_words_to_file(words_to_keep, output_filename)
    return success, skip_remaining_filters

if __name__ == "__main__":
    initial_input_file = "gos_NL.dic"
    filtered_file = "gos_NL_filtered.dic"

    # Kopieer originele bestand als startpunt
    shutil.copy(initial_input_file, filtered_file)

    filters = [
        # (r'lijk$', "woorden die eindigen op 'lijk'"),
        # (r'ü', "woorden met 'ü'"),
        # (r'ao|erig$', "woorden met 'ao' of eindigend op 'erig'")
        # (r'erig$', "woorden met 'erig' op het einde"),
        # (r'x', "woorden met 'x'"),
        # (r'y', "woorden met 'y'"),
        # (r'tjie$', "woorden met 'tjie' op het einde"),
        # (r'ae', "woorden met 'ae'"),
        (r'_', "woorden met '_'"),
    ]


    for regex, description in filters:
        success, stop_here = filter_gronings_wordlist(
            input_filename=filtered_file,
            output_filename=filtered_file,
            regex_pattern=regex,
            description=description
        )

        if not success:
            print(f"Filter '{description}' faalde. Verwerken gestopt.")
            break
        if stop_here:
            print("Filtering vroegtijdig beëindigd door gebruiker.")
            break
