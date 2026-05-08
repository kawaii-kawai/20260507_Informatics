from lunar_python import Solar
from datetime import datetime, timedelta
import json
from tqdm import tqdm

# 二十四節気名
SOLAR_TERMS = [
    "小寒", "大寒", "立春", "雨水", "啓蟄", "春分",
    "清明", "穀雨", "立夏", "小満", "芒種", "夏至",
    "小暑", "大暑", "立秋", "処暑", "白露", "秋分",
    "寒露", "霜降", "立冬", "小雪", "大雪", "冬至"
]

# 黄経 (度)
LONGITUDES = {
    "春分": 0,
    "清明": 15,
    "穀雨": 30,
    "立夏": 45,
    "小満": 60,
    "芒種": 75,
    "夏至": 90,
    "小暑": 105,
    "大暑": 120,
    "立秋": 135,
    "処暑": 150,
    "白露": 165,
    "秋分": 180,
    "寒露": 195,
    "霜降": 210,
    "立冬": 225,
    "小雪": 240,
    "大雪": 255,
    "冬至": 270,
    "小寒": 285,
    "大寒": 300,
    "立春": 315,
    "雨水": 330,
    "啓蟄": 345,
}


def get_solar_terms_for_year(year):
    """
    指定年の二十四節気を取得
    """

    result = []

    # 年初から探索
    start = datetime(year, 1, 1)
    end = datetime(year + 1, 1, 1)

    current = start

    while current < end:
        solar = Solar.fromDate(current)

        # 節気名
        jq = solar.getLunar().getJieQi()

        if jq in SOLAR_TERMS:
            item = {
                "name_ja": jq,
                "solar_longitude": LONGITUDES[jq],
                "datetime": current.strftime("%Y-%m-%dT%H:%M:%S"),
            }

            # 重複防止
            if len(result) == 0 or result[-1]["name_ja"] != jq:
                result.append(item)

        current += timedelta(hours=1)

    return result


all_terms = []

for y in tqdm(range(2000, 2031), desc="Processing years"):
    all_terms.extend(get_solar_terms_for_year(y))


with open("solar_terms.json", "w", encoding="utf-8") as f:
    json.dump(all_terms, f, ensure_ascii=False, indent=2)


print("solar_terms.json を出力しました")