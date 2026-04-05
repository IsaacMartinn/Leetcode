class Solution:
    def dayOfYear(self, date: str) -> int:
        curr_sum = 0
        calendar_dict = {
            "01": 31,
            "02": 28,
            "03": 31,
            "04": 30,
            "05":31,
            "06": 30,
            "07": 31,
            "08": 31,
            "09": 30,
            "10": 31,
            "11": 30,
            "12": 31
        }

        year, month, day = date.split("-")

        if int(month) == 1:
            return int(day)
        
        for key, value in calendar_dict.items():
            curr_sum += value
            if int(key) == int(month) - 1:
                curr_sum += int(day)
                break
        
        if (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0):
            if int(month) > 2:
                return curr_sum + 1
            else:
                return curr_sum
        else:
            return curr_sum

            