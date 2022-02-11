import pickle
# pickle 모둘 - 객체(리스트, 딕셔너리)의 형태를 그래로
# 유지하면서 파일에 저장하고 불러올수 있는 모듈임

with open('./output/data.txt', 'wb') as f:
    animal = ['강아지', '고양이', '호랑이']
    dic = {1:'강아지', 2:'고양이', 3:'호랑이'}
    pickle.dump(animal, f)
    pickle.dump(dic, f)

with open('./output/data.txt', 'rb') as f2:
    animal = pickle.load(f2)
    dic = pickle.load(f2)

    print(animal)
    print(dic)