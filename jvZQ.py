import openai
import random

# OpenAI APIキーを設定します
api_key = "ここに発行したAPIキーを貼り付ける"
client = openai.OpenAI(api_key=api_key)


# ChatGPTモデルを使用してメッセージを送信し、応答を取得する関数を定義します
def chat_with_openai():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "こんにちはと入力されたら動作確認完了と返してください"},
            {"role": "user", "content": "こんにちは"},
        ],
        temperature=0
    )
    return response.choices[0].message.content


response_content = chat_with_openai()
print(response_content)
