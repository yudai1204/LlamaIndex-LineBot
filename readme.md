# LlamaIndex-LINE Bot

このレポジトリはLINE Messaging API及びChatGPTを用いた自動返信Botの動作プログラムです。
LlamaIndexというライブラリを用い、事前に設定した知識情報をもとに返信することができ、ChatGPTの制限よりも多いデータ数を読み込ませることができるためオリジナルの返信をすることができます。
今回は依頼元クリニックのデータと医療データを大量に読み込み、医療に関する質問に答えることができるようにしました。
DBに会話履歴を保存しAPIに送信することで会話の流れを読んだ回答をすることができます。

### support
 - Python 3.9↑
 - Flask
 - openai
 - llama-index
