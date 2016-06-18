import pickle
from sklearn import svm


TESTDATANUM = 5
TRAINDATAPATH = 'output/alphdata.pkl'

def main():
    alphdata = pickle.load(open(TRAINDATAPATH, 'rb'))
    alphtrain = []
    alphtest = dict()
    alphgp = []
    for ii in alphdata:
        #if ii == 'z' or ii == 'y':
        #   continue
        alphgp += [ii]*(len(alphdata[ii])-TESTDATANUM)
        alphtrain += alphdata[ii][0:-TESTDATANUM]
        alphtest[ii] = alphdata[ii][-TESTDATANUM:]

    clf = svm.SVC()
    clf.fit(alphtrain, alphgp)
    print('learning complete!')

    input("Press Enter to continue...")

    count = [0,0]
    for ii in alphtest:
        #if ii == 'z' or ii == 'y':
        #    continue
        print(ii)
        ans = clf.predict(alphtest[ii])
        print(ans)
        for jj in ans:
            if ii == jj:
                count[0] += 1
            count[1] += 1

    print('Correct Rate: ' + str(count[0]/count[1])) 