def format_check_summary(checks: list[dict], lang: str = "ru") -> str:
    if len(checks) == 0:
        result = "Проверки: 0" if lang == "ru" else "Checks: 0"
        return result
    header = f"Проверки: {len(checks)}" if lang == "ru" else f"Checks: {len(checks)}"

    list_of_results = [header]
    for e in checks:
        icon = "✅" if e.get('ok') == True else "❌"
        ok = f'— {e["message"]}' if e.get('message') else "— ок" if lang == "ru" and e['ok'] == True else "— ok" if lang == "en" and e.get('ok') else ""
        name = e['name'] if e['name'] else "?"
        # print(name, ok)
        result_string = icon + " " + name + " " + ok
        list_of_results.append(result_string.strip())
        
    print("\n".join(list_of_results))
    return "\n".join(list_of_results)


def main():
    pass


if __name__ == "__main__":
    main()
