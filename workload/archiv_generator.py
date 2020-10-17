def create_archiv(size_in_MB, name):
    content = b''

    content += (b'b' * (1024*1024*size_in_MB))

    f = open(f'workload_{name}.txt','wb')
    f.write(content)
    f.close

def config_workload(size_in_MB, N_archivs):
    for i in range(N_archivs):
        create_archiv(size_in_MB, i)

config_workload(1, 2)
