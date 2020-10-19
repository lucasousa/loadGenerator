def create_archiv(size_in_MB, name, text):
    content = b'' + bytes(text, 'utf-8')

    content += (content * (1024*1024*size_in_MB))

    f = open(f'{name}.txt','wb')
    f.write(content)
    f.close

def config_workload(config_tests):
    for test in config_tests:
        create_archiv(test['text'], test['name'], test['char_content'])

config_workload([{'text': 4, 'name': 'workload_4MB', 'char_content': 'c'}, {'text': 10, 'name': 'workload_10MB', 'char_content': 'd'}])
