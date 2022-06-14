def init_db():
    # CVS Column Names
    col_names = ['name','catprod','bio', 'ville', 'departement', 'longitude', 'latitude', 'contact']
    # Use Pandas to parse the CSV file
    csvData = pandas.read_csv(filePath,names=col_names, header=None)
    for i,row in csvData.iterrows():
        print(i,row['name'],row['catprod'],row['bio'],row['ville'],row['departement'],row['longitude'],row['latitude'],row['contact'])
        # db.session.add(i,row['name'],row['catprod'],row['bio'],row['ville'],row['departement'],row['longitude'],row['latitude'],row['contact'])
    db.session.commit()
    lg.warning('Database initialized!')

def query_db(list):
    db.session.query(list)
    # checker si ok
    db.session.commit()
