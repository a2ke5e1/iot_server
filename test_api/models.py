from django.db import models


# Create your models here.
class Plugs(models.Model):
    """
    Convert these fields into Django model
    "end_time";"person_id";"start_time";"type";"date";"duration";"is_high_level";"plausability";"provider" """
    end_time = models.DateTimeField()
    person_id = models.IntegerField()
    start_time = models.DateTimeField()
    type = models.CharField(max_length=255)
    date = models.DateField()
    duration = models.IntegerField()
    is_high_level = models.BooleanField()
    plausability = models.BooleanField()
    provider = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "plugs"

    def __str__(self):
        return f"Plugs(end_time={self.end_time},\
        person_id={self.person_id},\
        start_time={self.start_time},\
        type={self.type},\
        date={self.date},\
        duration={self.duration},\
        is_high_level={self.is_high_level},\
        plausability={self.plausability},\
        provider={self.provider})"

    @staticmethod
    def get_average_activity_by_date():
        from django.db import connection

        cursor = connection.cursor()
        results = cursor.execute(
            """
            SELECT date, type, AVG(duration) as "averge_duration" FROM test_api_plugs GROUP BY type, date ORDER BY date;
            """
        )
        columns = [col[0] for col in results.description]
        return [
            dict(zip(columns, row)) for row in results.fetchall()
        ]

    @staticmethod
    def get_average_activity():
        from django.db import connection

        cursor = connection.cursor()
        results = cursor.execute(
            """
            SELECT type, AVG(duration) as "averge_duration" FROM test_api_plugs GROUP BY type;
            """
        )
        columns = [col[0] for col in results.description]
        return [
            dict(zip(columns, row)) for row in results.fetchall()
        ]
