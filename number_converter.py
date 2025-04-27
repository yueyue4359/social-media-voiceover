import re 


num_to_chinese_mapping = {
    '0': '零', '1': '一', '2': '二', '3': '三', '4': '四',
    '5': '五', '6': '六', '7': '七', '8': '八', '9': '九'
}

def number_to_chinese(num: int) -> str:

    if num == 0:
        return num_to_chinese_mapping['0']
    chinese_str = ''
    for digit in str(num):
        chinese_str += num_to_chinese_mapping[digit]
    return chinese_str

    
def format_number_to_chinese(num: int) -> str:
    """Convert a number to Chinese characters."""
    if num == 0:
        return "零"
    elif num < 10:
        return num_to_chinese_mapping[str(num)]
    elif num < 20:
        return "十" + (num_to_chinese_mapping[str(num % 10)] if num % 10 != 0 else "")
    else:
        tens = num // 10
        ones = num % 10
        if ones == 0:
            return num_to_chinese_mapping[str(tens)] + "十"
        else:
            return num_to_chinese_mapping[str(tens)] + "十" + num_to_chinese_mapping[str(ones)]


def convert_time_to_chinese(time_str: str) -> str:
    """Convert a time string (e.g., '10:12') to Chinese time format."""
    try:
        hour, minute = map(int, time_str.split(":"))
    except ValueError:
        return "Invalid time format"

    hour_chinese = format_number_to_chinese(hour)

    if minute == 0:
        time_in_chinese = f"{hour_chinese}点"
    elif minute == 30:
        time_in_chinese = f"{hour_chinese}点半"
    elif minute == 15:
        time_in_chinese = f"{hour_chinese}点一刻"
    elif minute == 45:
        time_in_chinese = f"{hour_chinese}点四十五"
    else:
        minute_chinese = format_number_to_chinese(minute)
        time_in_chinese = f"{hour_chinese}点{minute_chinese}"

    return time_in_chinese


def time_colon_replacer(match):
    hour, minute = match.group(1), match.group(2)
    return convert_time_to_chinese(f"{hour}:{minute}")


def time_dot_replacer(match):
        hour = match.group(1)
        return convert_time_to_chinese(f"{hour}:00")


def number_replacer(match):
        num = match.group(1)
        return number_to_chinese(int(num))


def convert_all(text):
    """
    Convert tricky numbers to colloquial Chinese
    
    for example: 
    time_str1 = "9:30"
    time_str2 = "6:45"
    time_str3 = "12:15"
    time_str4 = "10:12"
    
    should translate as: 
    九点半
    六点四十五
    十二点一刻
    十点十二
    """

    time_colon = re.sub(r'(\d{1,2}):(\d{2})', time_colon_replacer, text)
    time_dot = re.sub(r'(\d{1,2})点', time_dot_replacer, time_colon)
    converted_text = re.sub(r'(?<!\d)(\d+)(?!\d)', number_replacer, time_dot)
    return converted_text