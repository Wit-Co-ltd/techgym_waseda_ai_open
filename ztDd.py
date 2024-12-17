import openai
import random

# OpenAI APIキーを設定します
api_key = "ここに発行したAPIキーを貼り付ける"
client = openai.OpenAI(api_key=api_key)


# ランダムな都市の名前を入力
def get_random_location():
    locations = ["日本", "ニューヨーク", "パリ", "ロンドン", "シドニー"]
    return random.choice(locations)


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


def main():
    print("地理探検ゲームへようこそ！終了するには '終了' と入力してください。")
    while True:
        location = input("\n場所を入力してください: ")
        if location.lower() == "終了":
            print("ゲームを終了します。ありがとうございました！")
            break
        elif location.lower() == "ランダム":
            location = get_random_location()

        response = chat_with_openai(location)
        print("\n" + response)


main()
