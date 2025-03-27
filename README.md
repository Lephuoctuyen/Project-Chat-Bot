# <p align="center"><strong>Build Project Chat Bot AI</strong></p>

## 1. Introduce Chat bot with LLM.
* Get familiar with a traditional [chatbot](https://github.com/PacktPublishing/Python-Natural-Language-Processing-Cookbook/tree/master/Chapter07): 
  * Chapter 7 of the Book Python-Natural-Language-Processing-Cookbook introduces the traditional chatbot Rasa. 
     * Building a basic chatbot with keyword-matching
     * Building a basic Rasa chatbot
     * Creating question-answer pairs with Rasa
     * Creating and visualizing conversation paths with Rasa
     * Creating actions for the Rasa chatbot
     * Detail basic rasa chatbot:
       * [Youtube](https://www.youtube.com/watch?v=YxQNVe0M7j8&list=PLp9h3aIPyUbZyCUP4ELTaS2ajxKNWaSnU): Build a chatbot using Rasa in Youtube
       * [Medium]( https://medium.com/analytics-vidhya/build-a-chatbot-using-rasa-78406306aa0c): Build a chatbot using Rasa in Medium

       * [Rasa](https://www.techtarget.com/searchenterpriseai/definition/natural-language-understanding-NLU) is an open-source machine learning framework for automating text—and voice-based conversations. Building contextual assistants and chatbots that help customers is hard. Rasa provides the infrastructure and tools necessary for high-performing, resilient, proprietary contextual assistants that work. With Rasa, all developers can create better text—and voice-based assistants.
         * Rasa open source includes:
           * NLU: determines what the user wants and captures key contextual information.
             * NLU is the core technology that processes human language input extracts its meaning, and provides meaningful insights.
             * NLU is the foundation for many advanced AI applications, such as chatbots, voice assistants, sentiment analysis, and machine translation.
             * The ultimate goal is to build systems that interact with humans as naturally and intelligently as possible.
             * Two fundamental concepts of NLU are intent and entity recognition:
               * Intent recognition is the process of identifying the user's sentiment in the input text and determining their objective. It's the first and most important part of NLU, as it establishes the meaning of the text.
               * Entity recognition is a specific type of NLU that focuses on identifying the entities in a message and then extracting the most important information about those entities. There are two types of entities: name entities (people's names, business names,...) and numeric entities (quantities, dates, currencies and percentages,...)
           * Core: selects the next best response or action based on conversation history.
           * Rasa gồm 2 phần chính : Rasa NLU và Rasa Core. Trong đó, với một message đầu vào, Rasa NLU sẽ tiến hành phân tích câu để đưa ra ý định (intent) của người dùng và đối tượng (entity) trong câu. Rasa Core sau đó sẽ tiếp nhận phần thông tin để quyết định công việc cần làm cũng như message trả ra
           * Rasa NLU (Natural Language Understanding): Rasa NLU is an open-source natural language processing tool for intent classification (decides what the user is asking), extraction of the entity from the bot in the form of structured data and helps the chatbot understand what user is saying. [Rasa NLU là một công cụ xử lý ngôn ngữ tự nhiên mã nguồn mở dùng để phân loại ý định (xác định người dùng đang yêu cầu gì), trích xuất thực thể từ chatbot dưới dạng dữ liệu có cấu trúc và giúp chatbot hiểu được nội dung mà người dùng đang nói.] 
           * Rasa Core: a chatbot framework with machine learning-based dialogue management which takes the structured input from the NLU and predicts the next best action using a probabilistic model like LSTM neural network rather than if/else statement. Underneath the hood,  it also uses reinforcement learning to improve the prediction of the next best action. [Rasa Core là một framework chatbot với quản lý hội thoại dựa trên học máy, sử dụng đầu vào có cấu trúc từ NLU và dự đoán hành động tiếp theo tối ưu bằng mô hình xác suất như mạng nơ-ron LSTM thay vì sử dụng các câu lệnh if/else. Bên dưới, nó cũng áp dụng học tăng cường (reinforcement learning) để cải thiện khả năng dự đoán hành động tiếp theo.] 
           * Channels and integrations: connect assistant to user and backend systems.
           * [Reference detail of vietnam](https://viblo.asia/p/tong-quan-ve-rasa-chatbot-E1XVOxrp4Mz#_cac-van-de-khi-xay-dung-chatbot-thong-minh-1): 
* Build a model chatbot with [LLM](https://github.com/PacktPublishing/Python-Natural-Language-Processing-Cookbook-Second-Edition/tree/main/Chapter10): 
  * .....

## 2. Build 
