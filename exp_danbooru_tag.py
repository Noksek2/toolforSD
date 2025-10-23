# clean tag
def show_cleantag(tag,add_tag={'shiny skin','masterpiece','doujin'},exc_tag={'monochrome','grayscale','greyscale','simple background', 'white background'}):
  #split by '\n', make list, get odd number index (1,3,5) ... , tag2
  tag2=[line for line in tag.strip().split('\n')][1::2]
  
  # t in tag2 -> 
  # example : ['asdf wef 3f', 'xdmvkmv 232323 f3'] 
  # -> t : 'asdf wef 3f'
  # -> t.split(' ') : ['asdf', 'wef', '3f']
  # -> [:-1] : ['asdf','3f']
  # -> ''.join(~~) : 'asdf 3f'
  taglist=[' '.join(t.split(' ')[:-1]) for t in tag2]

  # if t not in exc_tag -> add t in list
  #ex) taglist : ['pork' 'pig' 'buta']
  #ex) exc_tag : {'pork', 'pig'}
  #ex) for t in taglist : 'pork' , 'pig', 'buta'
  #ex) tag_out=['buta']. exc_tag=['pork', 'pig']
  tag_out=[t for t in taglist if t not in exc_tag]

  #union(tag_out, add_tag)
  #ex) add_tag={'haha'}, tag_out=['pork']
  # -> {'pork'} U {'haha'} = {'pork', 'haha'}
  # list({'pork', 'haha'}) = ['pork', 'haha']
  tag_out=list(set(tag_out).union(add_tag))

  #sort tag_out 
  tag_out.sort()

  #join the tags with ,
  print(', '.join(tag_out))

#copy & paste tags line from danbooru 
show_cleantag("""?
1girl 3k
?
school uniform 15k""")
