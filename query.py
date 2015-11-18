import json, xapian
from .config import dbpath, fields

def search(query, active_element, numresults=10):
    # Don't do the search unless  the query is reasonably informative;
    # could hose the machine.
    if sum(map(len, query.values())) < 7:
        return []
    # Put active_element at end of query
    qfields = sorted(query, key=lambda k: k == active_element)
    # XXX There  should be a way  to do this without  going through an
    # intermediate string, and without adding prefixes.
    qvalues = [(k, e) for k in qfields for e in query[k].split()]
    qstring = ['%s:%s' % (field, value) for field, value in qvalues]
    querystring = ' AND '.join(qstring)
    db = xapian.Database(dbpath)
    queryparser = xapian.QueryParser()
    queryparser.set_database(db)
    for field, abbrev in fields.items():
        queryparser.add_prefix(field, abbrev)
    query = queryparser.parse_query(querystring,
                                    queryparser.FLAG_BOOLEAN |
                                    queryparser.FLAG_PARTIAL |
                                    queryparser.FLAG_WILDCARD)
    enquire = xapian.Enquire(db)
    enquire.set_weighting_scheme(xapian.BoolWeight())
    enquire.set_query(query)
    return [json.loads(r.document.get_data())
            for r in enquire.get_mset(0, numresults)]

