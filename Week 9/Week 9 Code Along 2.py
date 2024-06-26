import csv
import DB_Base as db

class CollegeScoreCard:
    def __init__(self, row):
        self.id = row[0]
        self.name = row[1]
        self.state = row[2]
        self.act_med = row[3]
        self.sat_avg = row[4]
        self.enrollment = row[5]
        self.tuition = row[6]
        self.postgrad_income_10yr = row[7]
        self.completion_rate = row[8]

class CsvLab(db.DBBase):

    def __init__(self, db_name):
        super().__init__(db_name)  # Assuming db.DBBase accepts a database name as an initialization parameter

    def reset_database(self):
        try:
            sql = """
                    DROP TABLE IF EXISTS CollegeScoreCard;
                    CREATE TABLE CollegeScoreCard (
                        id INTEGER NOT NULL PRIMARY KEY UNIQUE,
                        name TEXT,
                        state VARCHAR(2),
                        act_med INTEGER,
                        sat_avg INTEGER,
                        enrollment INTEGER,
                        tuition INTEGER,
                        postgrad_income_10yr INTEGER,
                        completion_rate REAL
                    );
                  """
            self.execute_script(sql)
        except Exception as e:
            print(e)

    def read_college_data(self, file_name):
        self.college_scores_list = []
        try:
            with open(file_name, 'r') as record:
                csv_reader = csv.reader(record)
                next(csv_reader)  # Skip header
                for row in csv_reader:
                    college = CollegeScoreCard(row)
                    self.college_scores_list.append(college)
        except Exception as e:
            print(e)

    def save_to_database(self):
        print("Number of records to save:", len(self.college_scores_list))
        save = input("Continue (y/n)? ").lower()

        if save == "y":
            for item in self.college_scores_list:
                try:
                    self.get_cursor().execute("""INSERT INTO CollegeScoreCard
                                (id, name, state, act_med, sat_avg, enrollment, tuition, postgrad_income_10yr, completion_rate)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                                    (item.id, item.name, item.state, item.act_med, item.sat_avg,
                                     item.enrollment, item.tuition, item.postgrad_income_10yr,
                                     item.completion_rate))
                    self.get_connection().commit()
                    print("Saved item", item.id, item.name, item.state)
                except Exception as e:
                    print(e)
        else:
            print("Save to database aborted.")

#usage
csv_lab = CsvLab("colleg_scores.sqlite")
csv_lab.reset_database()  # Uncomment this line if you want to reset the database
csv_lab.read_college_data("CollegeScoreCard_Exercise.csv")
csv_lab.save_to_database()
