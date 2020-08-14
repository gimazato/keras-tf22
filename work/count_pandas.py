import pandas as pd

# それぞれの属性の要素の出現回数をカウントしたpandas.seriesのリストを返す
def count_attibute_value(df):
    list_of_attribute_series=[]
    columns_list = df.columns.values
    #attribute_num = len(columns_list)

    for attribute in columns_list:
        list_of_attribute_series.append(df[attribute].value_counts())
    return list_of_attribute_series


if __name__ == '__main__':
    #example
    df = pd.DataFrame({"item":[c for _ in range(5) for c in ["apple", "banana","orange"]],"rank":[chr(i%7+65) for i in range(15)]})
    l = count_attibute_value(df)
    print(df)
    print(l[0])
    print(l[1])