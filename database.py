import sqlite3


class Database:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def get_scores(self, level):
        scores = self.cursor.execute("select score from Records where level=%d" % level).fetchall()

        return [i[0] for i in scores]

    def add_record(self, level, value):
        self.cursor.execute("INSERT INTO Records (level, score) VALUES (%d, %d)" % (level, value))

        self.connection.commit()

    def get_plot_value(self):
        plot_value = self.cursor.execute("select display from Plot").fetchone()

        return plot_value[0]

    def set_plot_value(self):
        self.cursor.execute("update Plot set display = 1")

        self.connection.commit()
