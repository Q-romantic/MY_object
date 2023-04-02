import os
from win32com import client as wc


def save_doc_to_docx(rawpath):  # doc转docx
    '''
    :param rawpath: 传入和传出文件夹的绝对路径
    :return: None
    '''
    word = wc.Dispatch("Word.Application")
    filenamelist = os.listdir(rawpath)  # 需要处理的文件所在文件夹目录
    for i in filenamelist:
        if i.endswith('.doc') and not i.startswith('~$'):  # 找出文件中以.doc结尾并且不以~$开头的文件（~$是为了排除临时文件的）
            print(i)
            # try 打开文件
            doc = word.Documents.Open(rawpath + i)
            # 将文件名与后缀分割
            rename = os.path.splitext(i)
            # 将文件另存为.docx
            doc.SaveAs(new_path + rename[0] + '.docx', 12)  # 12表示docx格式
            doc.Close()
    word.Quit()


if __name__ == '__main__':
    old_path = 'C:\\Z\\全国邮储分行\\邮储2021年模板-Q3-ISS&BCS\\'  # 不能用相对路径，老老实实用绝对路径,注意：目录的格式必须写成双反斜杠
    new_path = 'C:\\Z\\全国邮储分行\\邮储2021年模板-Q4-ISS&BCS\\'
    save_doc_to_docx(old_path)
