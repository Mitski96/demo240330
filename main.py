import streamlit as st
import openai
import os

# 環境変数からOpenAI APIキーの取得
openai.api_key = os.getenv('OPENAI_API_KEY')

def main():
    st.title('志望動機作成ヘルパー')

    # ユーザー入力の受け取り
    experience = st.text_area('あなたの経歴を教えてください。', height=150)
    company_name = st.text_input('会社の名前')
    industry = st.text_input('業種')
    positive_aspects = st.text_area('この会社について好きな点', height=150)
    company_homepage_content = st.text_area('会社のホームページや企業理念など、参考にしたい内容をここに貼り付けてください。', height=200)

    # 志望動機の生成
    if st.button('志望動機を生成'):
        prompt = f"経歴: {experience}\n希望する会社: {company_name}\n業種: {industry}\n良いと思う点: {positive_aspects}\n参考にした会社の情報: {company_homepage_content}\n\nこれらの情報に基づいて、詳細な志望動機を作成してください。"
        response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=150)
        st.write(response.choices[0].text.strip())

if __name__ == '__main__':
    main()
