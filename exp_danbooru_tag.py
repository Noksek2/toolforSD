input_text='''<paste danbooru tag>'''
#example
'''? babo 13M
? merong 15M
...
'''
prompt=','.join([' '.join(tag.split(' ')[:-1]) for tag in input_text.split('\n')]
