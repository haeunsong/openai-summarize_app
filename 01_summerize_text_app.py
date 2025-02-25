##### 기본 정보 불러오기 ####
# Streamlit 패키지 추가
import streamlit as st
# OpenAI 패키지 추가
from openai import OpenAI

##### 기능 구현 함수 #####
# 요약하는 기능


def askGpt(prompt, api_key):
    try:
        client = OpenAI(api_key=api_key)  # API 키를 입력받은 후 클라이언트 생성
        messages_prompt = [{"role": "system", "content": prompt}]
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages_prompt
        )
        return response.choices[0].message.content  # 응답 메시지 반환
    except Exception as e:
        return f"오류 발생: {e}"  # 예외 처리

##### 메인 함수 #####


def main():
    st.set_page_config(page_title="📃 요약 프로그램")

    # 사이드바 - API 키 입력받기
    with st.sidebar:
        open_apikey = st.text_input(
            label="🔑 OPENAI API 키 입력",
            placeholder="API Key를 입력하세요",
            type="password"
        )
        st.markdown("---")

    # 메인 UI
    st.header("📃 텍스트 요약 프로그램")
    st.markdown("---")

    text = st.text_area("✍️ 요약할 텍스트를 입력하세요")

    # 요약 버튼 동작
    if st.button("📝 요약 실행"):
        if not open_apikey:
            st.warning("⚠️ API 키를 입력하세요.")
        elif not text.strip():
            st.warning("⚠️ 요약할 텍스트를 입력하세요.")
        else:
            prompt = f"""
            **Instructions**:
            - You are an expert assistant that summarizes text into **Korean language**.
            - Your task is to summarize the **text** sentences in **Korean language**.
            - Your summaries should include the following:
                - Omit duplicate content, but increase the summary weight of duplicate content.
                - Summarize by emphasizing concepts and arguments rather than case evidence.
                - Summarize in 3 lines.
                - Use the format of a bullet point.
            -text: {text}
            """
            summary = askGpt(prompt, open_apikey)
            st.info(summary)


if __name__ == "__main__":
    main()
