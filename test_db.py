from databases.conectionBDMySql import DataBaseMySql

teste = DataBaseMySql()

# bytes = b"0x410x420x43x02123aaa"
# f = open("sample.txt", "wb")
# f.write(bytes)
# f.close()

teste.connect()
# teste.insert(bytes)
response = teste.select('dados','workload')
print(len(response[3][0]))
teste.disconnect()