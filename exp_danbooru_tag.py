def show_cleantag(tag,add_tag={'shiny skin','masterpiece','doujin'},exc_tag={'monochrome','grayscale','greyscale','simple background', 'white background'}):
  tag2=[line for line in tag.strip().split('\n')][1::2]
  taglist=[' '.join(t.split(' ')[:-1]) for t in tag2]
  tag_out=[t for t in taglist if t not in exc_tag]
  tag_out=(set(tag_out).union(add_tag))
  print(', '.join(tag_out))
#
show_cleantag("""?
1girl 3k
?
school uniform 15k""")
