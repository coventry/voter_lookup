import json, xapian, csv
from .config import dbpath, fields

def index_voters(datapath):
    f = open(datapath)
    headers = csv.reader(f).next()
    voters = csv.DictReader(f, headers)
    db = xapian.WritableDatabase(dbpath, xapian.DB_CREATE_OR_OPEN)
    termgenerator = xapian.TermGenerator()
    for voternum, voter in enumerate(voters):
        if voternum % 1000 == 0:
            print voternum
        if voter['PARTY_AFFILIATION'] is None: # Must have reached end of file
            try:
                f.next()
            except StopIteration:
                break
            else:
                raise RuntimeError, 'Should never get here'
        doc = xapian.Document()
        termgenerator.set_document(doc)
        for field, prefix in fields.items():
            termgenerator.index_text(voter[field], 1, prefix)
            termgenerator.index_text(voter[field])
            termgenerator.increase_termpos()
        doc.set_data(json.dumps(voter))
        # Make sure this record is only in the DB once
        doc.add_boolean_term(voter['SOS_VOTERID'])
        db.replace_document(voter['SOS_VOTERID'], doc)

def main():
    from .config import datapaths
    for p in datapaths:
        index_voters(p)
    
if __name__ == '__main__':
    main()
