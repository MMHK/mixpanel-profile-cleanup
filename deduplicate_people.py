#!/usr/bin/python

from mixpanel_api import Mixpanel
import json, sys, getopt

projects = []

def parseOpt():
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hc:",["help","config="])
    except getopt.GetoptError:
        print 'deduplicate_people.py -c <config.json>'
        sys.exit(2)
    for opt_name,opt_value in opts:
        if opt_name in ('-h','--help'):
            print("deduplicate_people.py -c <config.json>")
            sys.exit()
        if opt_name in ('-c','--config'):
            return opt_value
    return 'config.json'

if __name__ == '__main__':
    config = parseOpt()
    with open(config, 'r') as f:
        projects = json.load(f)
        
    for project in projects:
        print("======== start =========\nbegin handle %s" % (project['name']))
        mixpanel = Mixpanel(project['secret'], token=project['token'], debug=True)
        r = mixpanel.deduplicate_people(prop_to_match=project['match'], merge_props=True, backup=True)
        # r = mixpanel.people_delete(query_params={ 'selector' : '(("11111111" in properties["$mobile"]))'})
        print(r) 
        print('======== end =========\n')
