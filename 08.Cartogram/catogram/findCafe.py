import numpy as np

def find_cafe(str,data):
    cf = data[data['상호명'].str.find(str)>=0]
    cf.set_index('ID',inplace=True)
    return cf
    
def find_cafeE(str,data):
    cfE = data[data['상호명'].str.lower().str.find(str)>=0]
    cfE.set_index('ID',inplace=True)
    return cfE

def coffee(cafe):
    cafe['커피지수'] = (cafe['스타벅스 매장수'] + cafe['커피빈 매장수'])/(cafe['이디야 매장수'] + cafe['빽다방 매장수'])
    for i in cafe[cafe['커피지수'] == np.inf].index:
        cafe['커피지수'][i] = cafe['커피지수'].min()
    cafe.reset_index(inplace=True)
    cafe.rename(columns={'index':'ID'},inplace=True)
    return cafe