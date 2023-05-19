import time
from datetime import datetime, timedelta


class DataTimeUtils:
    """时间工具类"""
    ACCURACY_TIME_PATTERN = "%Y-%m-%d %H:%M:%S"  # 年 - 月 - 日 时：分：秒
    YEAR_MONTH_DAYS_PATTERN = "%Y-%m-%d"  # 年 - 月 - 日
    HOUR_MINUTE_SECOND_PATTERN = "%H:%M:%S"  # 时：分：秒
    YEAR_PATTERN = "%Y"  # 年
    MONTH_PATTERN = "%m"  # 月
    WEEK_PATTEN = "%w"  # 周
    DAYS_PATTERN = "%d"  # 日
    HOUR_PATTERN = "%H"  # 时，24 小时
    MINUTE_PATTERN = "%M"  # 分
    SECOND_PATTERN = "%S"  # 秒
    MICROSECOND_PATTERN = "%f" # 微秒

    @classmethod
    def recordTime(cls) -> float:
        """
        记录当前时间

        Returns:
            时间浮点
        """
        return time.time()

    @classmethod
    def caculate(cls, start: float, end: float, round_index=3) -> float:
        """
        计算时间差

        Args:
            start: 开始时间
            end: 结束时间
            round_index: 结果位数，默认保留3位

        Returns:
            时间差

        Examples:
            >>> start = DataTimeUtils.recordTime()
            >>> print("test")
            >>> end = DataTimeUtils.recordTime()
            >>> result = DataTimeUtils.caculate()
        """
        return round(end - start, round_index)

    @classmethod
    def getTime(cls, days=0) -> str:
        """
        获取某准确日期，自选

        Args:
            days: 今天为0，昨天为-1，以此类推，默认为0

        Returns:
            日期，格式为年-月-日-时-分-秒
        """
        now = datetime.now()
        return (now + timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")

    @classmethod
    def getTimeByPattern(cls, pattern: str, days=0) -> str:
        """
        根据格式获取某准确日期

        Args:
            pattern: 生成日期的格式
            days: 今天为0，昨天为-1，以此类推，默认为0

        Returns:
            日期
        """
        now = datetime.now()
        return (now + timedelta(days=days)).strftime(pattern)

    @classmethod
    def caculateDays(cls, start: str, end: str) -> int:
        """
        计算天数差

        Args:
            start: 开始的准确日期，格式为年-月-日
            end: 结束的准确日期，格式为年-月-日

        Returns:
            天数差
        """
        d1 = datetime.strptime(start, "%Y-%m-%d")
        d2 = datetime.strptime(end, "%Y-%m-%d")
        d = d2 - d1
        return int(d.days)

    @classmethod
    def caculateTimes(cls, start: str, end: str) -> float:
        """
        计算时间差

        Args:
            start: 开始的准确时间，格式为时:分:秒
            end: 结束的准确时间，格式为时:分:秒

        Returns:
            时间差，单位为秒
        """
        d1 = datetime.strptime(start, "%H:%M:%S")
        d2 = datetime.strptime(end, "%H:%M:%S")
        d = d2 - d1
        return d.total_seconds()

    @classmethod
    def caculateTimes_ms(cls, start: str, end: str) -> float:
        """
        计算时间差(毫秒级别)

        Args:
            start: 开始的准确时间，格式为时:分:秒.毫秒
            end: 结束的准确时间，格式为时:分:秒.毫秒

        Returns:
            时间差，单位为秒
        """
        d1 = datetime.strptime(start, "%H:%M:%S.%f")
        d2 = datetime.strptime(end, "%H:%M:%S.%f")
        d = d2 - d1
        return d.total_seconds()

    @classmethod
    def getDayByCaculate(cls, time: str, days=-1) -> str:
        """
        计算参数时间为基准的时间

        Args:
            time: 基准时间,年-月-日
            days: 计算的时间，-1为昨天

        Returns:
            计算后时间，年-月-日

        Examples:
            >>> caculate = DataTimeUtils.getDayByCaculate("2023-05-11")
            2023-05-10
            >>> caculate = DataTimeUtils.getDayByCaculate("2023-04-12", days=1)
            2023-04-13
        """
        base_time = datetime.strptime(time, "%Y-%m-%d")
        caculate = base_time + timedelta(days=days)
        return caculate.strftime("%Y-%m-%d")

    @classmethod
    def getDay(cls, days=0):
        """
        获取某日期

        Args:
            days: 今天为0，昨天为-1，以此类推

        Returns:
            日期，格式为年-月-日

        Examples:
            >>> DataTimeUtils.getDay() # 假设今天是2023-05-11
            2023-05-11
            >>> DataTimeUtils.getDay(-1)
            2023-05-10

        """
        now = datetime.now()
        day = now + timedelta(days=days)
        return day.strftime("%Y-%m-%d")