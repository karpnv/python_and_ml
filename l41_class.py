# def my_min(a,b):
#     if a>b:
#         r=b
#     else:
#         r=a
#     return r
#
# r1=my_min(2,3)
# print(r1)

class My_file():
    fname='C:\\'

    def __init__(self):
        fname='other_df.tsv'
        self.fname=fname
        self.count+=1

    def set_name(self,fname):
        self.fname=fname

    def show(self):
        print('File name is '+self.fname)

    def __del__(self):
        self.count+=-1
        del self.fname

    def set_prefix(fname='myfile.tsv'):
        prefix='c:\\Users\\'
        return prefix+fname

f=My_file()
f.show()
f.set_name('df.tsv')
print(My_file.count)
f.show()

f1=My_file.set_prefix('new_df.tsv')
print(My_file.fname)
