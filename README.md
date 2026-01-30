# 🎙️ VoxFlow -- Conversando por Voz com IA

VoxFlow é uma aplicação interativa desenvolvida em **Python** com
**Streamlit** que permite conversar com um modelo de IA utilizando
**voz**, integrando **Speech-to-Text**, **Large Language Models** e
**Text-to-Speech** em um fluxo contínuo.

> 📌 **Este projeto foi desenvolvido como parte do desafio da DIO:**\
> **"Conversando por Voz Com o ChatGPT Utilizando Whisper (OpenAI) e
> Python"**,\
> no **Bootcamp Bradesco -- GenAI & Dados**.

------------------------------------------------------------------------

## 🚀 Funcionalidades

-   🎤 Gravação de áudio pelo navegador\
-   🧠 Transcrição automática de voz para texto (Whisper)\
-   ✏️ Edição manual do texto transcrito\
-   🤖 Conversação com IA (Gemini)\
-   🔊 Resposta em texto e áudio (gTTS)\
-   💬 Histórico de conversa em formato de chat\
-   ⏳ Spinners durante processamento

------------------------------------------------------------------------

## 🧩 Arquitetura

    VoxFlow/
    │
    ├── main.py
    ├── services/
    │   ├── speech_to_text.py
    │   ├── llm.py
    │   ├── tts.py
    │   └── __init__.py
    │
    ├── .env
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## 🛠️ Tecnologias

-   Python\
-   Streamlit\
-   Whisper (OpenAI -- local)\
-   Google Generative AI (Gemini)\
-   gTTS\
-   FFmpeg

------------------------------------------------------------------------

## ⚙️ Pré-requisitos

-   Python 3.10+\
-   FFmpeg instalado\
-   API Key do Gemini

------------------------------------------------------------------------

## ▶️ Execução

``` bash
streamlit run main.py
```

------------------------------------------------------------------------

## 🎓 Contexto Educacional

Projeto desenvolvido para a **Digital Innovation One (DIO)**\
**Bootcamp:** Bradesco -- GenAI & Dados

------------------------------------------------------------------------

## 👨‍💻 Autor

Desenvolvido por **Kaio Pablo**