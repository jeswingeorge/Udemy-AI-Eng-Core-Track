# Day 3 Notes

3 different breeds of LLMs that they have been trained to do, the tasks that they have set out to accomplish. 
- And the starting point is known as **Base Model**. Its an LLM model that takes a sequence of information as input and would predict what would come next. Eg: Chatting in message, etc.
- Model that could decide how much thinking to do is known as **hybrid model**: 
  - ChatGPT gives reply based on instruction
  - Reasong/Thinking Models (Eg: Adding Step-by-step in prompt)

And the amount of reasoning that a reasoning model does is sometimes called its **reasoning budget** or its **reasoning effort**. And there's a technique called **budget forcing**.  
When you make a model a reasoning model and make it think longer, you make it do more reasoning. And there are various tricks to achieving this.

Simply by adding the word weight periodically into the sequence as you're making it predict the next tokens, causes it to reflect on its reasoning and reason a bit deeper, and challenge itself and weigh up the arguments that it's made and consider whether they're still accurate.

Reasoning models with a high reasoning budget perform better in all of the different benchmarks really almost across the board.

