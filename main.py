import pandas as pd

def output(mainfile,checkfile,outfile):
    main = pd.read_excel(mainfile)
    main = main.astype('string')

    check = pd.read_excel(checkfile)
    check = check.astype('string')

    main_nore = main.drop_duplicates(subset=['number','supply'],keep='first')
    main_total = pd.merge(main_nore,main_nore,on='number')
    main_use = main_total.drop(main_total[main_total['supply_x']==main_total['supply_y']].index)

    main_use['supplym'] = main_use[['supply_x','supply_y']].apply(lambda x:x['supply_x']+x['supply_y'],axis=1)
    check['supplym2']=check[['supply1','supply2']].apply(lambda x:x['supply1']+x['supply2'],axis=1)

    main_use['checkindex'] = ''
    for i in range(0,len(check)):
        a = check.loc[i,'supplym2']
        main_use.loc[main_use['supplym']==a,'checkindex'] = i
        main_use.loc[main_use['supplym']==a,'checkname1'] = check.loc[i,'supply1']
        main_use.loc[main_use['supplym']==a,'checkname2'] = check.loc[i,'supply2']

    main_use[main_use['checkindex']!=''][['number','supply_x','supply_y','checkindex','checkname1','checkname2']].to_csv(outfile+'/result.csv')
