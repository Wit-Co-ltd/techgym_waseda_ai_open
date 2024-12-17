import openai

# OpenAI APIキーを設定します
api_key = "ここに発行したAPIキーを貼り付ける"
client = openai.OpenAI(api_key=api_key)


# ChatGPTモデルを使用してメッセージを送信し、応答を取得する関数を定義します
def chat_with_openai(location):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content":
                "あなたは地理に関する専門家です。"
                "ユーザーが入力した国や都市に関する面白いと思えるような詳細で興味深い情報、"
                "出力する内容は２，３行程度に短縮してください"
                "情報は正確で有益なものとし、具体的な例や数字を含めてください。"
                "情報の正確性は担保し、ユーモアを交えて解答してください"},
            {"role": "user", "content": location}
        ],
        model="gpt-4",
        temperature=0
    )
    return response.choices[0].message.content


print("地理探検ゲームへようこそ")
location = input("\n場所を入力してください: ")
response_content = chat_with_openai(location)
print(response_content)
