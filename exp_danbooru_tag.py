# clean tag
def show_cleantag(
    raw_tag_string: str, 
    add_tags: set = {'shiny skin', 'masterpiece', 'doujin'}, 
    exclude_tags: set = {'monochrome', 'grayscale', 'greyscale', 'simple background', 'white background'}
):
    """
    Danbooru에서 복사한 태그 문자열('?'와 카운트가 포함된)을 입력받아,
    불필요한 태그를 제외하고 필수 태그를 추가한 뒤,
    정렬된 콤마(,) 구분 문자열로 출력합니다.
    """

    # 1. 입력 문자열을 줄 단위로 분리하고, 빈 줄은 제거합니다.
    all_lines = raw_tag_string.strip().split('\n')
    
    # 2. Danbooru 태그 형식('?' 라인과 '태그 3k' 라인이 반복됨)을 파싱합니다.
    #    홀수 번째(1, 3, 5...) 라인에 실제 태그가 있습니다.
    tag_lines_with_count = all_lines[1::2]
    
    # 3. 각 태그 라인에서 '15k' 같은 포스트 카운트 부분을 제거합니다.
    #    (예: "school uniform 15k" -> "school uniform")
    tags_without_count = []
    for line in tag_lines_with_count:
        parts = line.split(' ')   # 공백으로 분리 (예: ['school', 'uniform', '15k'])
        tag_only = ' '.join(parts[:-1]) # 마지막 요소(카운트)만 제외하고 다시 합침
        tags_without_count.append(tag_only)

    # 4. 제외 목록(exclude_tags)에 포함되지 않는 태그만 필터링합니다.
    filtered_tags = [tag for tag in tags_without_count if tag not in exclude_tags]

    # 5. 필수 태그(add_tags)를 추가합니다.
    #    set을 사용해 중복을 자동으로 방지하고, 합집합(union)을 구합니다.
    final_tag_set = set(filtered_tags).union(add_tags)

    # 6. 최종 태그 목록을 알파벳순으로 정렬합니다.
    #    set을 다시 list로 변환해야 sort()가 가능합니다.
    final_tag_list = list(final_tag_set)
    final_tag_list.sort()

    # 7. 콤마(,)와 공백으로 구분된 최종 문자열을 출력합니다.
    print(', '.join(final_tag_list))

# --- 실행 예시 ---
# copy & paste tags line from danbooru 
danbooru_input = """?
1girl 3k
?
school uniform 15k
?
monochrome 5k 
"""

show_cleantag(danbooru_input)
# 출력 결과: 1girl, doujin, masterpiece, school uniform, shiny skin
