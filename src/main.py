import pickle
from sklearn import svm
import json

TESTDATANUM = 5

def main():
    alphdata = pickle.load(open('alphdata.pkl', 'r'))
    alphtrain = []
    alphtest = dict() 
    alphgp = []
    for ii in alphdata:
        alphgp += [ii]*len(alphdata[ii])
        alphtrain += alphdata[ii][0:-TESTDATANUM]
        alphtest[ii] = alphdata[ii][-TESTDATANUM:]
    
    clf = svm.SVC()
    clf.fit(alphtrain, alphgp)
    print('learning complete!')
    
    input("Press Enter to continue...")
    
    count = 0,0
    for ii in alphtest:
        print(ii)
        ans = clf.predict(alphtest[ii])
        print(t)
        for jj in t:
            if ii == jj:
                count[0] += 1
            count[1] += 1
    
    print('Correct Rate: ' + count[0]/count[1]) 
