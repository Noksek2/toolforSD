import glob
import os

# ==========================================
# [설정 구역] 여기에 원하는 태그를 넣고 빼세요
# ==========================================
TARGET_FOLDER = "E:/Lib/stable-diffusion-webui/outputs/X/mizu/res"  # 스크립트와 같은 폴더에 있는 파일들을 처리 (경로 지정 가능)

# 1. 무조건 추가할 태그 목록 (순서 유지를 위해 리스트로 선언 후 세트로 변환)
TAGS_TO_ADD = ["mizustyle", "simple background", "white background"]

# 2. 나중에 제외하고 싶은 태그가 생기면 여기에 적으세요 (예: "bad anatomy", "watermark")
TAGS_TO_REMOVE = []
# ==========================================

# 연산 효율 및 중복 체크를 위해 set으로 변환
add_set = set(TAGS_TO_ADD)
remove_set = set(TAGS_TO_REMOVE)

# 폴더 내 모든 .txt 파일 찾기
txt_files = glob.glob(os.path.join(TARGET_FOLDER, "*.txt"))

if not txt_files:
    print("❌ 처리할 .txt 파일을 찾지 못했습니다. 경로를 확인해주세요.")
    exit()

print(f"📦 총 {len(txt_files)}개의 파일을 처리를 시작합니다...")

for file_path in txt_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    # 1. 쉼표 기준으로 쪼개고 공백 제거 (콤마 양옆 공백 트림)
    existing_tags = [tag.strip() for tag in content.split(",") if tag.strip()]

    # 2. 제외할 태그 필터링 (remove_set에 있으면 탈락)
    filtered_tags = [tag for tag in existing_tags if tag not in remove_set]

    # 3. 추가할 태그 중 원본에 없는 녀석들만 발라내기 (중복 방지)
    # 셋(set)의 차집합 연산 사용
    existing_set = set(filtered_tags)
    needed_to_add = [tag for tag in TAGS_TO_ADD if tag not in existing_set]

    # 4. 최종 태그 조합
    # 화풍 고유 토큰(mizustyle 등)이 무조건 '맨 앞'에 와야 학습이 잘 되므로,
    # 새로 추가할 태그들을 앞에 배치하고 기존 필터링된 태그들을 뒤에 붙입니다.
    final_tags = needed_to_add + filtered_tags

    # 5. 콤마로 묶어서 다시 파일에 쓰기
    new_content = ", ".join(final_tags)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

print("✨ 모든 파일의 태그 수정이 완료되었습니다!")
