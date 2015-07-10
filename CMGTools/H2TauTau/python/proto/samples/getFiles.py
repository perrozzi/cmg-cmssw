def getFiles(dataset, user, pattern, useCache=True, useAAA=False):
    from CMGTools.Production.datasetToSource import datasetToSource
    # print 'getting files for', dataset,user,pattern
    ds = datasetToSource( user, dataset, pattern, useCache )
    files = ds.fileNames
    if useAAA: 
      return ['root://cms-xrd-global.cern.ch/%s' % f for f in files]
    else:
      return ['root://eoscms//eos/cms%s' % f for f in files]
