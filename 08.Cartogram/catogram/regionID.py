
def get_ID(df):
    si_name = [None] * len(df)
    for n in df.index:
        if df['시도명'][n][-3:] not in ['광역시','특별시','자치시']:
            if df['시군구명'][n][:-1]=='고성' and df['시도명'][n]=='강원도':
                si_name[n] = '고성(강원)'
            elif df['시군구명'][n][:-1]=='고성' and df['시도명'][n]=='경상남도':
                si_name[n] = '고성(경남)'
            elif len(df['시군구명'][n].split()) == 1:
                si_name[n] = df['시군구명'][n][:-1]
            elif df['시군구명'][n].split()[1] in ['마산합포구','마산회원구']:
                si_name[n] = df['시군구명'][n].split()[0][:-1] + ' ' + df['시군구명'][n].split()[1][2:-1]
            else:
                if len(df['시군구명'][n].split()[1]) == 2:
                    si_name[n] = df['시군구명'][n].split()[0][:-1] + ' ' + df['시군구명'][n].split()[1]
                else: 
                    si_name[n] = df['시군구명'][n].split()[0][:-1] + ' ' + df['시군구명'][n].split()[1][:-1]
        elif df['시도명'][n] == '세종특별자치시':
            si_name[n] = '세종'
        else:
            if len(df['시군구명'][n]) == 2:
                si_name[n] = df['시도명'][n][:2] + ' ' + df['시군구명'][n]
            else:
                si_name[n] = df['시도명'][n][:2] + ' ' + df['시군구명'][n][:-1]

    return si_name