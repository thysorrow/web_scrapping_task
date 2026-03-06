import pytest

from summary_formatter import format_check_summary


@pytest.mark.parametrize("checks, expected", [
    ([], "Проверки: 0"),
    ([{"name": "WSL", "ok": True}],
     'Проверки: 1\n✅ WSL — ок'),

])
def test_format_check_summary_ru(checks, expected):
    assert format_check_summary(checks) == expected


@pytest.mark.parametrize("checks, lang, expected", [
    ([
        {"name": "SSL", "ok": True, "message": "Done"},
        {"name": "WHOIS", "ok": True},
        {"name": "WHOIS"},
        {"name": "DNS", "ok": False, "message": "Timeout error"},
    ],
        "en",
        """Checks: 4
✅ SSL — Done
✅ WHOIS — ok
❌ WHOIS
❌ DNS — Timeout error"""),
])
def test_format_check_summary_en(checks, lang, expected):
    assert format_check_summary(checks, lang) == expected
