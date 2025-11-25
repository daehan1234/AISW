import os
from openai import OpenAI
import streamlit as st

# 키는 무조건 제거하고 환경 변수 or secrets로 처리해야 함.
os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


st.title("좋지 못한 습관을 개선해드립니다")

habit = st.text_input("어떤 습관을 가지고 계신가요?")

if st.button("개선안 듣기"):

    # 1) 텍스트 개선안 생성
    chat_response = client.chat.completions.create(
        messages=[
            {"role": "system", 
             "content": "입력받은 습관을 개선할 수 있는 방법을 파트별로 나누어 가독성 있게 작성해줘."},
            {"role": "user", "content": habit},
        ],
        model="gpt-4o",
    )

    result = chat_response.choices[0].message.content

    # 2) “개선된 모습” 프롬프트 자동 생성
    improved_prompt_msg = client.chat.completions.create(
        messages=[
            {"role": "system",
             "content": "사용자가 입력한 나쁜 습관이 완전히 개선된 후의 모습을 시각적으로 묘사한 이미지 프롬프트를 만들어줘. "
                        "사진 스타일로 자연스럽고 긍정적인 분위기를 강조해."},
            {"role": "user", "content": habit},
        ],
        model="gpt-4o",
    )

    improved_prompt = improved_prompt_msg.choices[0].message.content

    # 3) 개선된 모습 이미지 생성
    image = client.images.generate(
        model="dall-e-3",
        prompt= improved_prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = image.data[0].url

    st.write(result)
    st.image(image_url, caption="개선된 모습 이미지")
