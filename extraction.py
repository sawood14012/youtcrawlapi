import json

def extractclean(output):
    with open(output) as json_file:
        data = json.load(json_file)
        prefinal = []
        childids =[]
        parentids =[]


        for p in data:
            if '.' in p['cid']:
                childids.append(p['cid'])

            elif '.' not in p['cid']:
                parentids.append(p['cid'])

            else:
                break

        for p in parentids:
            pwr = {}
            #print p
            pwr['comment'] = p.encode("utf-8")
            if [s for s in childids if p in s]:
                pwr['replies'] = [s.encode("utf-8") for s in childids if p in s]
        # print [s.encode("utf-8") for s in childids if p in s]
        #print pwr
                prefinal.append(pwr)


    

# print prefinal
        for p in prefinal:

            for d in data:
                if p['comment']==d['cid']:
                #print p['comment']
                    print d['text']
                    if 'replies' in p.keys():
                        print 'has replies'
                    
                        replies = p['replies']
                        for r in replies:
                            for i in data:
                                if r == i['cid']:
                                    print "reply:", i['text']   

    return data


if __name__ == "__main__":
    extractclean("outvccwHvCIuW8.json")
   # main(sys.argv[1:])
 #  main2("vccwHvCIuW8",100)

         
                    

            
    


