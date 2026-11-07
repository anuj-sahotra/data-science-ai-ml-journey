def inspect_data(*args, **kwargs):
    print("Postional : ", args)
    print("Keyword : " , kwargs)
    
inspect_data(10,30, name = "Champion", age = 23)    