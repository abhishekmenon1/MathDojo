from utils.database import DatabaseAddition, DatabaseSubtraction, theEnd, Improvement, DatabasePercentage, \
    DatabaseCombined

db = DatabaseAddition("assets/text/add_data.txt")
db_sub = DatabaseSubtraction("assets/text/sub_data.txt")
db_com = DatabaseCombined("assets/text/com_data.txt")
db_per = DatabasePercentage("assets/text/percent_data.txt")
db_imp = Improvement("assets/text/improv.txt")
db_end = theEnd("assets/text/end_score.txt")



