[ACE](https://docs.nvidia.com/ace/overview/latest/index.html)Workflows
  * [Animation Pipeline](https://docs.nvidia.com/ace/animation-pipeline/latest/index.html)
  * [Tokkio](https://docs.nvidia.com/ace/tokkio/latest/index.html)
  * [Gaming Avatar](https://docs.nvidia.com/ace/gaming-avatar/latest/index.html)

Microservices
  * [Animation Graph](https://docs.nvidia.com/ace/animation-graph-microservice/latest/index.html)
  * [Omniverse Renderer](https://docs.nvidia.com/ace/omniverse-renderer-microservice/latest/index.html)
  * [Audio2Face-3D](https://docs.nvidia.com/ace/audio2face-3d-microservice/latest/index.html)
  * [ACE Agent](https://docs.nvidia.com/ace/ace-agent/latest/index.html)
  * [Riva ASR](https://docs.nvidia.com/ace/riva-asr-microservice/latest/index.html)
  * [Riva TTS](https://docs.nvidia.com/ace/riva-tts-microservice/latest/index.html)
  * [Riva Translation](https://docs.nvidia.com/ace/riva-translation-microservice/latest/index.html)
  * [Audio2Face-2D](https://docs.nvidia.com/ace/audio2face-2d-microservice/latest/index.html)
  * [Voice Font](https://docs.nvidia.com/ace/voice-font-microservice/latest/index.html)

Microservices (Early Access)
  * [Audio2Face-3D Authoring](https://docs.nvidia.com/ace/audio2face-3d-authoring-microservice/latest/index.html)
  * [Unreal Renderer](https://docs.nvidia.com/ace/unreal-renderer-microservice/latest/index.html)

Interfaces
  * [Animation Data Format](https://docs.nvidia.com/ace/animation-data-format/latest/index.html)
  * [Colang](https://docs.nvidia.com/ace/colang-language/latest/index.html)
  * [UMIM](https://docs.nvidia.com/ace/umim/latest/index.html)

Containers
  * [Resource Downloader](https://docs.nvidia.com/ace/resource-downloader-container/latest/index.html)

Tools
  * [Avatar Customization](https://docs.nvidia.com/ace/avatar-customization/latest/index.html)
  * [Unified Cloud Services Tools (UCS Tools)](https://docs.nvidia.com/ucf/)
  * [Maya-ACE](https://docs.nvidia.com/ace/maya-ace/latest/index.html)
  * [ACE Unreal Plugin](https://docs.nvidia.com/ace/ace-unreal-plugin/latest/index.html)


[Skip to main content](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#main-content)
Back to top
`Ctrl`+`K`
[ ![ACE Agent - Home](https://docs.nvidia.com/ace/ace-agent/latest/_static/nvidia-logo-horiz-rgb-blk-for-screen.svg) ![ACE Agent - Home](https://docs.nvidia.com/ace/ace-agent/latest/_static/nvidia-logo-horiz-rgb-wht-for-screen.svg) ACE Agent ](https://docs.nvidia.com/ace/ace-agent/latest/index.html)
Search `Ctrl`+`K`
Search `Ctrl`+`K`
[ ![ACE Agent - Home](https://docs.nvidia.com/ace/ace-agent/latest/_static/nvidia-logo-horiz-rgb-blk-for-screen.svg) ![ACE Agent - Home](https://docs.nvidia.com/ace/ace-agent/latest/_static/nvidia-logo-horiz-rgb-wht-for-screen.svg) ACE Agent ](https://docs.nvidia.com/ace/ace-agent/latest/index.html)
Table of Contents
  * [Getting Started](https://docs.nvidia.com/ace/ace-agent/latest/getting-started.html)
    * [Overview](https://docs.nvidia.com/ace/ace-agent/latest/overview.html)
    * [Quick Start Guide](https://docs.nvidia.com/ace/ace-agent/latest/quick-start-guide.html)
    * [Release Notes](https://docs.nvidia.com/ace/ace-agent/latest/release-notes.html)
  * [Architecture](https://docs.nvidia.com/ace/ace-agent/latest/architecture/index.html)
    * [Architecture Introduction](https://docs.nvidia.com/ace/ace-agent/latest/architecture/arch-intro.html)
  * [Deployment](https://docs.nvidia.com/ace/ace-agent/latest/deployment/index.html)
    * [Interface Introduction](https://docs.nvidia.com/ace/ace-agent/latest/deployment/interface-intro.html)
    * [Docker Environment](https://docs.nvidia.com/ace/ace-agent/latest/deployment/docker-environment.html)
    * [Kubernetes Environment](https://docs.nvidia.com/ace/ace-agent/latest/deployment/kubernetes-environment.html)
    * [Python Environment](https://docs.nvidia.com/ace/ace-agent/latest/deployment/python-environment.html)
    * [Sample Clients](https://docs.nvidia.com/ace/ace-agent/latest/deployment/sample-clients.html)
  * [Tutorials](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/index.html)
    * [Building a Bot using Colang 2.0 and Event Interface](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html)
    * [Building LangChain-Based Bots](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-langchain-bot.html)
    * [Building a Low Latency Speech-To-Speech RAG Bot](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-rag.html)
    * [Customizing a Bot](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/customize-a-bot.html)
  * [Sample Bots](https://docs.nvidia.com/ace/ace-agent/latest/sample-bots/index.html)
    * [Sample Bots Introduction](https://docs.nvidia.com/ace/ace-agent/latest/sample-bots/sample-bots-intro.html)
    * [Chitchat Bot](https://docs.nvidia.com/ace/ace-agent/latest/sample-bots/chitchat-bot.html)
    * [LLM Bot](https://docs.nvidia.com/ace/ace-agent/latest/sample-bots/llm-bot.html)
    * [RAG Bot](https://docs.nvidia.com/ace/ace-agent/latest/sample-bots/rag-bot.html)
    * [Stock Market Bot](https://docs.nvidia.com/ace/ace-agent/latest/sample-bots/stock-market-bot.html)
    * [Gaming Non-Playing Character (NPC) Bot](https://docs.nvidia.com/ace/ace-agent/latest/sample-bots/gaming-npc-bot.html)
    * [DuckDuckGo LangChain Bot](https://docs.nvidia.com/ace/ace-agent/latest/sample-bots/duckduckgo-langchain-bot.html)
    * [Spanish Weather Bot](https://docs.nvidia.com/ace/ace-agent/latest/sample-bots/spanish-weather-bot.html)
    * [Food Ordering Bot](https://docs.nvidia.com/ace/ace-agent/latest/sample-bots/food-ordering-bot.html)
    * [Plan and Execute (LangGraph) Bot](https://docs.nvidia.com/ace/ace-agent/latest/sample-bots/plan-execute-langgraph-bot.html)
    * [Colang 1.0 Sample Bots](https://docs.nvidia.com/ace/ace-agent/latest/sample-bots/colang1-sample-bots.html)
  * [Configuration Guide](https://docs.nvidia.com/ace/ace-agent/latest/config/index.html)
    * [Bot Configurations Introduction](https://docs.nvidia.com/ace/ace-agent/latest/config/bot-configurations.html)
    * [General Configurations](https://docs.nvidia.com/ace/ace-agent/latest/config/general-configurations.html)
    * [Slots Configurations](https://docs.nvidia.com/ace/ace-agent/latest/config/slots-configurations.html)
    * [Plugin Configurations](https://docs.nvidia.com/ace/ace-agent/latest/config/plugin-configurations.html)
    * [Model Configurations](https://docs.nvidia.com/ace/ace-agent/latest/config/model-configurations.html)
    * [Chat Engine Configurations](https://docs.nvidia.com/ace/ace-agent/latest/config/chat-engine-configurations.html)
    * [Speech Configurations](https://docs.nvidia.com/ace/ace-agent/latest/config/speech-configurations.html)
  * [User Guide](https://docs.nvidia.com/ace/ace-agent/latest/user/index.html)
    * [Using Colang](https://docs.nvidia.com/ace/ace-agent/latest/user/colang.html)
    * [Integration with LangChain and LlamaIndex](https://docs.nvidia.com/ace/ace-agent/latest/user/integrate-langchan-llmaindex.html)
    * [NLP Server](https://docs.nvidia.com/ace/ace-agent/latest/user/nlp-server.html)
    * [Speech AI](https://docs.nvidia.com/ace/ace-agent/latest/user/speech-ai.html)
    * [Training Models](https://docs.nvidia.com/ace/ace-agent/latest/user/training-models.html)
    * [Plugin Server](https://docs.nvidia.com/ace/ace-agent/latest/user/plugin-server.html)
    * [Streaming in ACE Agent](https://docs.nvidia.com/ace/ace-agent/latest/user/streaming.html)
  * [API Guide](https://docs.nvidia.com/ace/ace-agent/latest/api/index.html)
    * [API Introduction](https://docs.nvidia.com/ace/ace-agent/latest/api/api-intro.html)
    * [HTTP Interface](https://docs.nvidia.com/ace/ace-agent/latest/api/http-interface.html)
    * [gRPC Interface](https://docs.nvidia.com/ace/ace-agent/latest/api/grpc-interface.html)
    * [Plugin Server](https://docs.nvidia.com/ace/ace-agent/latest/api/plugin-server-api.html)
    * [NLP Server](https://docs.nvidia.com/ace/ace-agent/latest/api/nlp-server-api.html)
  * [Best Practices](https://docs.nvidia.com/ace/ace-agent/latest/best-practices/index.html)
    * [Best Practices Introduction](https://docs.nvidia.com/ace/ace-agent/latest/best-practices/best-practices-intro.html)
    * [Planning your Bot](https://docs.nvidia.com/ace/ace-agent/latest/best-practices/planning-bot.html)
    * [Logging and Debugging Issues](https://docs.nvidia.com/ace/ace-agent/latest/best-practices/log-debug-issues.html)
    * [Security Considerations](https://docs.nvidia.com/ace/ace-agent/latest/best-practices/security.html)
  * [Reference](https://docs.nvidia.com/ace/ace-agent/latest/reference/index.html)
    * [Basic Concepts](https://docs.nvidia.com/ace/ace-agent/latest/reference/basic-concepts.html)
    * [Support Matrix](https://docs.nvidia.com/ace/ace-agent/latest/reference/support-matrix.html)
    * [Migrating from ACE Agent 4.0.0 to ACE Agent 4.1.0](https://docs.nvidia.com/ace/ace-agent/latest/reference/migrating.html)
    * [Troubleshooting](https://docs.nvidia.com/ace/ace-agent/latest/reference/troubleshooting.html)
    * [End User License Agreement](https://docs.nvidia.com/ace/ace-agent/latest/reference/eula.html)
    * [Notices](https://docs.nvidia.com/ace/ace-agent/latest/reference/notices.html)


4.1
[4.1](https://docs.nvidia.com/ace/ace-agent/4.1/tutorials/build-bot-colang.html)[4.0](https://docs.nvidia.com/ace/ace-agent/4.0/tutorials/build-bot-colang.html)
  * [ ](https://docs.nvidia.com/ace/ace-agent/latest/index.html)
  * [Tutorials](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/index.html)
  * Building a...


# Building a Bot using Colang 2.0 and Event Interface[#](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#building-a-bot-using-colang-2-0-and-event-interface "Link to this heading")
Before you build a bot using Colang 2.0 and the Event Interface, ensure you have followed the steps in the [Docker Environment](https://docs.nvidia.com/ace/ace-agent/latest/deployment/docker-environment.html#docker-environment) section.
NVIDIA ACE Agent is an SDK, which helps you to build your domain conversational AI agent using Large Language Models (LLM). In this tutorial, you will learn how to work with the ACE Agent and how to create a simple bot that makes use of Colang 2.0 and asynchronous event processing. The bot features:
  * **Different response types** - The bot will make use of gestures, utterances and showing information on a UI.
  * **LLM integration** - The bot will make different use of LLMs to provide contextual answers and to simplify user input handling.
  * **Proactivity** - The bot will be proactive and will try to engage the user if no reply is given.
  * **Interruptibility** - The user can interrupt the bot at any time.
  * **Back-channeling** - The bot can react in real time based on ongoing user input to make your interactions interesting.
  * **Business Logic** - The bot can utilize custom python functions or API calls to integrate business logic.


Before you get started, there are a two key terminologies that you need to know.
**Colang** - Colang is the dialog modeling language used by ACE Agent. Colang makes it easy to define and control the behavior of your conversational system, especially in situations where deterministic behavior is required. ACE Agent is built on top of [NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) which also uses the Colang language. The current ACE Agent release supports two different versions (Colang 1.0 and Colang 2.0-beta). In this tutorial, we are going to use Colang 2.0-beta syntax. Colang 1.0 will be deprecated in future releases. This tutorial requires no prior knowledge about Colang as we will walk you through all the changes step by step. For more information about Colang, refer to the [Getting Started](https://docs.nvidia.com/ace/colang-language/2.0/getting-started/index.html#getting-started "\(in Colang\)") documentation.
**Event interface** - The ACE Agent event interface provides an asynchronous, event-based interface to interact with bots written in Colang 2.0. The interface allows you greater flexibility in managing your interaction between the user and the bot due to its asynchronous design. Using the interface, you can easily build interactive systems that break turn-taking behavior (user speaks, bot speaks, user speaks…) and you can handle multiple actions going on at the same time (for example, bot speaks, makes a gesture to emphasize a point, user is looking around and interrupts bot after a short while).
The event interface is best suited with more complex interactive systems. An example for this would be an interactive avatar system where you not only want to control the bot responses but also gestures, postures, sounds, showing pictures, and so on. The NVIDIA Tokkio reference application (part of ACE) is a great starting point for how to build a real interactive avatar system using the event interface from ACE Agent. For more information, [NVIDIA Tokkio](https://developer.nvidia.com/ace/tokkio-showcase) demonstrates such interactions with a 3D avatar running accessible from web browsers.
## Prerequisites[#](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#prerequisites "Link to this heading")
  1. Setup the [Event Simulator](https://docs.nvidia.com/ace/ace-agent/latest/deployment/sample-clients.html#event-sample-client) packaged as part of the [Quick Start resource](https://github.com/NVIDIA/ACE/tree/main/microservices/ace_agent/4.1) at `clients/event_client/`. To run the Event Simulator script, you need to install a few Python packages. It is recommended that you create a new Python environment to do so.
> ```
cdclients/event_client/
python3-mvenvsim-env
sourcesim-env/bin/activate
pipinstall-rrequirements.txt

```

  2. Test the template.
>     1. Open two different terminals.
>     2. In one terminal, start the ACE Agent with the bot template packaged in the [Quick Start resource](https://github.com/NVIDIA/ACE/tree/main/microservices/ace_agent/4.1) at `samples/event_interface_tutorial_bot`.
>> Set the OpenAI API key environment variable.
>>> ```
exportOPENAI_API_KEY=...
exportBOT_PATH=samples/event_interface_tutorial_bot/step_0
sourcedeploy/docker/docker_init.sh
dockercompose-fdeploy/docker/docker-compose.ymlupevent-bot-d

```

>     3. In a separate terminal, start the Event Simulator CLI.
>> ```
# Make sure that you are in the correct folder and that you have activated the python environment
cdclients/event_client/
sourcesim-env/bin/activate
pythonevent_client.py

```

  3. To confirm the test was successful, you should see the message **Welcome to the tutorial** in the **Chat** section on the left. Refer to the [sample event client](https://docs.nvidia.com/ace/ace-agent/latest/deployment/sample-clients.html#event-sample-client) section for more information.


> Note
> You can find the source code for all the individual steps in the Quick Start Resources under `samples/event_interface_tutorial_bot/step_x`. You can either follow the tutorial step by step making the necessary changes or you can try out the different versions by running the bots in the folder corresponding to each step (as explained in the following topics).
## Step 1: Making the Greeting More Interesting[#](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#step-1-making-the-greeting-more-interesting "Link to this heading")
In this section, you will see how you can use different types of responses to make the greeting or any other response from the bot more interesting. If you connect your bot to a system such as ACE to drive a 2D or 3D avatar, the exact same bot code as outlined below can be used to trigger multimodal responses such as avatar gestures or speech.
If you want to follow along, start with the bot in `samples/event_interface_tutorial_bot/step_0` to apply the changes below. The final bot code with all the changes from Step 1 can be found in `samples/event_interface_tutorial_bot/step_1`.
  1. Change the existing flow `bot express greetings` at the top of the `main.co` file. The flow should look similar to:
> ```
@meta(bot_intent=True)
flowbotexpressgreeting
(botexpress"Hi there!"
orbotexpress"Welcome!"
orbotexpress"Hello!")
andbotgesture"Wave with one hand"

```

  2. Show the greeting in the UI by adding the statement `start scene show short information "Welcome to this tutorial interaction" as $intro_ui` in the main flow before the line `bot express greeting` as shown below.
> ```
# The bot greets the user and a welcome message is shown on the UI
startsceneshowshortinformation"Welcome to this tutorial interaction"as$intro_ui
botexpressgreeting

```

  3. Restart the updated bot and Event Simulator.
> ```
dockercompose-fdeploy/docker/docker-compose.ymldown
exportBOT_PATH=samples/event_interface_tutorial_bot/step_1
sourcedeploy/docker/docker_init.sh
dockercompose-fdeploy/docker/docker-compose.ymlupevent-bot-d
pythonevent_client.py

```



In addition to the greeting message, we have a bot gesture shown for two seconds in the **Motion** area on the left and a UI shown on the right. To make a 3D Interactive Avatar say “Welcome!”, wave into the camera, and display a proper UI in the view, you could use the exact same Colang code.
## Step 2: Leveraging LLMs to Answer User Questions[#](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#step-2-leveraging-llms-to-answer-user-questions "Link to this heading")
In this section, you will enable the bot to answer any user question based on a large language model (LLM).
If you want to follow along, start with the bot in `samples/event_interface_tutorial_bot/step_1` to apply the changes below. The final bot code with all the changes from Step 2 can be found in `samples/event_interface_tutorial_bot/step_2`.
  1. Provide general instructions. Open the file `samples/event_interface_tutorial_bot/step_2/bot_config.yml`. Under `instructions` is an example for general LLM instructions. Keep these instructions for now, however, you can experiment with different instructions and see how you can change the types of answers the bot provides.
> ```
instructions:
-type:"general"
content:|
BelowisaconversationbetweenEmma,ahelpfulinteractiveavatarassistant(bot),andauser.
Thebotisdesignedtogeneratehuman-likeactionsbasedontheuseractionsthatitreceives.
[...]

```

  2. Enable LLM fallback. Update your `main.co` file as shown below. You only need to update the `CHANGE` sections. Ensure you don’t duplicate flows when doing your changes. If you define the same flow twice, the later definition will overwrite the first one. Your `main.co` file should look like this:
> ```
importcore
importavatars
importllm
@meta(bot_intent=True)
flowbotexpressgreeting
(botexpress"Hi there!"
orbotexpress"Welcome!"
orbotexpress"Hello!")
andbotgesture"Wave with one hand"
# CHANGE 1
# Add two flows to handle ending the conversation: bot express goodbye, user expressed done
@meta(bot_intent=True)
flowbotexpressgoodbye
(botexpress"Goodbye"orbotexpress"Talk to you soon!")andbotgesture"bowing in goodbye"
@meta(user_intent=True)
flowuserexpresseddone
usersaid(regex("(?i).*done.*|.*end.*demo.*|.*exit.*"))
flowhandlinguserrequestsuntiluserexpresseddone
# CHANGE 2
# This activates LLM-based responses for all unhandled user intents
activatellmcontinuation
# CHANGE 3 (optional)
# This will generated a variation of the question (variations are generated by the LLM)
botsaysomethinglike"How can I help you today?"
# CHANGE 4
# When the user expressed we end the conversation
userexpresseddone
botexpressgoodbye
# The main flow is the entry point
@meta(exclude_from_llm=True)
flowmain
# Technical flows, see Colang 2.0 documentation for more details
activatenotificationofundefinedflowstart
activatenotificationofcolangerrors
activatetrackingbottalkingstate
# The bot greets the user and a welcome message is shown on the UI
startsceneshowshortinformation"Welcome to this tutorial interaction"as$intro_ui
botexpressgreeting
# CHANGE 5
# Start handling user requests
handlinguserrequestsuntiluserexpresseddone
# This will prevent the main flow finishing ever
waitindefinitely

```

  3. Restart the updated bot and Event Simulator.
> ```
dockercompose-fdeploy/docker/docker-compose.ymldown
exportBOT_PATH=samples/event_interface_tutorial_bot/step_2
sourcedeploy/docker/docker_init.sh
dockercompose-fdeploy/docker/docker-compose.ymlupevent-bot-d
pythonevent_client.py

```

  4. Ask any questions to the bot that will be answered by the LLM given the provided general instructions.


## Step 3: Making the Bot Proactive[#](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#step-3-making-the-bot-proactive "Link to this heading")
In this section, we will add a proactivity feature to make the conversation with your bot feel more natural. The bot will generate an appropriate utterance when the user has been silent for a specified amount of time. This helps drive the conversation forward and can be used to provide additional information or help to the user.
If you want to follow along, start with the bot in `samples/event_interface_tutorial_bot/step_2` to apply the changes below. The final bot code with all the changes from Step 3 can be found in `samples/event_interface_tutorial_bot/step_3`.
  1. Add a new flow to `main.co` and activate the flow inside the `handling user requests until user expressed done` flow.
> ```
[...]
[...]
# CHANGE 1: Add new flow that reacts to the user being silent
flow handling user silence
user was silent 15.0
llm continue interaction
flow handling user requests until user expressed done
activate llm continuation
# CHANGE 2:Activate the new flow
activate handling user silence
bot say something like "How can I help you today?"
user expressed done
bot express goodbye
[...]

```

> With this, we will leverage the LLM to generate a bot response whenever the user has been silent for at least 15 seconds.
  2. Restart the updated bot and Event Simulator.
> ```
dockercompose-fdeploy/docker/docker-compose.ymldown
exportBOT_PATH=samples/event_interface_tutorial_bot/step_3
sourcedeploy/docker/docker_init.sh
dockercompose-fdeploy/docker/docker-compose.ymlupevent-bot-d
pythonevent_client.py

```

  3. Look for a timer that is ticking down, in the **Utils** section. When the timer finishes, the bot will follow up with the user.


## Step 4: Interrupting the Bot[#](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#step-4-interrupting-the-bot "Link to this heading")
When humans talk to each other we often interrupt each other to clarify certain points or to tell someone that you already know what they are talking about. With the ACE Agent event interface and Colang 2.0 we can easily achieve this with a few small changes to the current bot.
If you want to follow along, start with the bot in `samples/event_interface_tutorial_bot/step_3` to apply the changes below. The final bot code with all the changes from Step 4 can be found in `samples/event_interface_tutorial_bot/step_4`.
  1. Activate the following flow inside the `handling user requests until user expressed done` flow.
> ```
flowhandlinguserrequestsuntiluserexpresseddone
[...]
# Allow the user to interrupt the bot at anytime
activateinterruptionhandlingbottalking$mode="interrupt"
botsaysomethinglike"How can I help you today?"
[...]

```

> This flow handles any interruptions by the user.
  2. Ask the bot to tell a story about something, make the bot respond with a long sentence.
  3. While the bot is responding, type something to interrupt it.
  4. Restart the updated bot and Event Simulator.


> ```
dockercompose-fdeploy/docker/docker-compose.ymldown
exportBOT_PATH=samples/event_interface_tutorial_bot/step_4
sourcedeploy/docker/docker_init.sh
dockercompose-fdeploy/docker/docker-compose.ymlupevent-bot-d
pythonevent_client.py

```

## Step 5: Back-Channeling[#](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#step-5-back-channeling "Link to this heading")
Back channeling means the bot might provide short reactions based on user input to make the interaction more engaging. For this tutorial we will use a very simple example: At the end of the interaction we will ask the user to provide an email address. While the user is entering the email address the bot will provide contextual feedback.
If you want to follow along, start with the bot in `samples/event_interface_tutorial_bot/step_4` to apply the changes below. The final bot code with all the changes from Step 5 can be found in `samples/event_interface_tutorial_bot/step_5`.
  1. Add the following flows to the top of the file `main.co`.


> ```
# CHANGE 1: Add two new user intent flows
@meta(user_intent=True)
flowuserconfirmed
userhasselectedchoice"yes"
orusersaid"yes"
orusersaid"ok"
orusersaid"that's ok"
orusersaid"yes why not"
orusersaid"sure"
@meta(user_intent=True)
flowuserdenied
userhasselectedchoice"no"
orusersaid"no"
orusersaid"don't do it"
orusersaid"I am not OK with this"
orusersaid"cancel"
# CHANGE 2: Add flow that asks user for email address using UI and voice
flowaskforuseremail
startVisualChoiceSceneAction(prompt="Would you share your e-mail?",support_prompts=["You can just type 'yes' or 'no'","Or just click on the buttons below"],choice_type="selection",allow_multiple_choices=False,options=[{"id":"yes","text":"Yes"},{"id":"no","text":"No"}])as$confirmation_ui
botsay"I would love to keep in touch. Would you be OK to give me your e-mail address?"
whenuserconfirmed
send$confirmation_ui.Stop()
botask"Nice! Please enter a valid email address to continue"
startVisualFormSceneAction(prompt="Enter valid email",inputs=[{"id":"email","description":"email address","value":""}])as$action
whileTrue
whenVisualFormSceneAction.InputUpdated(interim_inputs=[{"id":"email","value":regex("@$")}])
botsay"And now only the domain missing!"
orwhenVisualFormSceneAction.InputUpdated(interim_inputs=[{"id":"email","value":regex("^[-\w\.]+@([\w-]+\.)+[\w-]{2,4}$")}])
botsay"Looks like a valid email address to me, just click ok to confirm"andbotgesture"success"
orwhenVisualFormSceneAction.ConfirmationUpdated(confirmation_status="confirm")
botsay"Thank you"andbotgesture"bowing"
break
orwhenVisualFormSceneAction.ConfirmationUpdated(confirmation_status="cancel")
botsay"OK. Maybe another time."
break
orwhenuserdenied
botsay"That is OK"

```

  1. Add the flow `ask for user email` at the end of the `handling user requests until user expressed done` flow before the bot expresses `goodbye`.
> ```
flowhandlinguserrequestsuntiluserexpresseddone
[...]
userexpresseddone
# Run the flow that asks the user for email address and await it
askforuseremail
botexpressgoodbye

```

  2. Restart the updated bot and Event Simulator.
> ```
dockercompose-fdeploy/docker/docker-compose.ymldown
exportBOT_PATH=samples/event_interface_tutorial_bot/step_5
sourcedeploy/docker/docker_init.sh
dockercompose-fdeploy/docker/docker-compose.ymlupevent-bot-d
pythonevent_client.py

```

  3. Test this interaction by ending the conversation. For example, write `I am done` into the prompt. This will trigger the flow `ask for user email`. This flow first asks you if you are `Okay` to provide your email (you can write the confirmation in the prompt or click on an option in the UI on the right). If you confirm, the `email` entering prompt will appear on the right in the UI section.


> Note
> The bot will react if you type the `@` as part of your email address.
## Step 6: Running Python Code[#](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#step-6-running-python-code "Link to this heading")
Colang allows you to call Python code from within a flow. These are called Python Actions and can contain arbitrary Python code. Python Actions can be particularly useful if you need more complex data processing functionality that cannot be easily done in Colang.
If you want to follow along, start with the bot in `samples/event_interface_tutorial_bot/step_5` to apply the changes below. The final bot code with all the changes from Step 6 can be found in `samples/event_interface_tutorial_bot/step_6`.
> Note
> All Python Actions run in the Python context of the Colang interpreter (sharing libraries and dependencies). If you need to write more complex code with specific dependencies, refer to [Integrating a Plugin Service](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#integrate-plugin-service).
Using Python Actions, we can easily leverage Python functionality inside a flow. Let’s add a flow that counts the words from the user’s sentence.
  1. Create a file called `actions.py` inside the `bot` folder, with the following content.


> ```
fromnemoguardrails.actions.actionsimportaction
@action(name="CountWordsAction")
asyncdefcount_words_action(transcript:str)->int:
returnlen(transcript.split())

```

  1. Update the `main.co` as shown below (adding a new user intent flow and a flow to handle the word counting requests from the user).


> ```
# CHANGE 1: Add a new user intent at the top of main.co (after the imports)
@meta(user_intent=True)
flowuserrequestedtocountwordsinsentence
userhasselectedchoice"can you please count the words in my next sentence"
orusersaid"count how many words are in my next utterance"
orusersaid"how many words"
[...]
# CHANGE 2: Add new flow that defines how to handle word counting requests
flowhandlingwordcountingrequests
userrequestedtocountwordsinsentence
botsay"Sure, please say a sentence and I will count the words"
usersaidsomethingas$ref
$count=awaitCountWordsAction(transcript=$ref.transcript)
botsay"There were {$count} words in your sentence."
[...]
flowhandlinguserrequestsuntiluserexpresseddone
[...]
activatehandlingbottalkinginterruption$mode="interrupt"
# CHANGE 3: Activate the new flow
activatehandlingwordcountingrequests
botsaysomethinglike"How can I help you today?"
[...]

```

  1. Restart the updated bot and Event Simulator.


> ```
dockercompose-fdeploy/docker/docker-compose.ymldown
exportBOT_PATH=samples/event_interface_tutorial_bot/step_6
sourcedeploy/docker/docker_init.sh
dockercompose-fdeploy/docker/docker-compose.ymlupevent-bot-d
pythonevent_client.py

```

## Step 7: Integrating a Plugin Service[#](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#step-7-integrating-a-plugin-service "Link to this heading")
In this section, we will add support to integrate an external API call with our bot. If the bot that you design depends on external information or needs to invoke certain actions, you may use the plugin service to host more complex Python code, compared to the approach showcased in the previous section using Python Actions.
If you want to follow along, start with the bot in `samples/event_interface_tutorial_bot/step_6` to apply the changes below. The final bot code with all the changes from Step 7 can be found in `samples/event_interface_tutorial_bot/step_7`.
Using plugin services, you can interact with any external API or any custom code using ACE Agent’s Plugin server. For this example, let’s collect information about stocks using the Yahoo Finance API and feed that information into the bot using a custom plugin.
  1. Create a file called `plugin_config.yaml`. This will contain the details of plugins that need to be deployed by ACE Agent.
  2. Create a `plugin` directory in the bot config directory.
  3. Add a file named `yahoo_fin.py` inside the `plugin` directory.


> ```
samples
└── event_interface_tutorial_bot
  └── bot_config.yaml
  └── main.co
  └── plugin
    └── yahoo_fin.py
  └── plugin_config.yaml

```

  1. Update `yahoo_fin.py` to get information about stocks using the Yahoo Finance API. For custom plugins, it’s necessary to import the `APIRouter` object.


> ```
importyfinanceasyf
fromyahoo_finimportstock_infoassi
importrequests
fromtypingimportOptional
fromfastapiimportAPIRouter
# API to extract stock price
Y_TICKER="https://query2.finance.yahoo.com/v1/finance/search"
Y_FINANCE="https://query1.finance.yahoo.com/v7/finance/quote?symbols="
router=APIRouter()
# Prepare headers for requests
session=requests.Session()
user_agent=(
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
)
session.headers.update({"User-Agent":user_agent})

defget_ticker_symbol_alphavantage(stock_name:str)->Optional[str]:
# We do not need actual api key to get ticker info
# But it is required as placeholder
api_key="YOUR_ALPHA_VANTAGE_API_KEY"
url=f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={stock_name}&apikey={api_key}"
response=requests.get(url)
data=response.json()
if"bestMatches"indataandlen(data["bestMatches"])>0:
ticker_symbol=data["bestMatches"][0]["1. symbol"]
returnticker_symbol
returnNone

@router.get("/get_ticker")
defget_ticker(company_name:str)->Optional[str]:
"""
  Take company name returns ticker symbol used for trading
  param
    Args:
      company_name: company name like Microsoft
    Returns:
      Ticker Symbol used for trading like MSFT for microsoft
  """
try:
params={"q":company_name,"quotes_count":1,"country":"United States"}
returnsession.get(url=Y_TICKER,params=params).json()["quotes"][0]["symbol"]
exceptExceptionase:
returnget_ticker_symbol_alphavantage(company_name)

@router.get("/get_stock_price")
defget_stock_price(company_name:str)->Optional[float]:
"""
  get a stock price from yahoo finance api
  """
try:
# Find ticker symbol for stock name, eg. Microsoft : MSFT, Nvidia: NVDA
ticker=get_ticker(company_name)
live_price=si.get_live_price(ticker)
returnround(live_price,2)
exceptExceptionase:
print(f"Unable to find stock price of {company_name}")
returnNone

```

  1. Register the plugin into the Plugin server. Update `plugin_config.yaml` to include the name and path of the new plugin.


> ```
config:
workers:1
timeout:30
plugins:
-name:stock
path:"./plugin/yahoo_fin.py"

```

  1. Update `main.co` to add and activate the new flow `handling stock price questions` to utilize the endpoints exposed by this plugin for our bot as shown below. The flow will first use the LLM to extract the company name, and then send the name to the plugin that we’ve created.


> ```
defineflowprovidestockprice
userasksstockprice
# CHANGE 1: Add user intent at the top of main.co
@meta(user_intent=True)
flowuseraskedstockprice
usersaid"What is the stock price of Microsoft?"
orusersaid"How much does an Nvidia stock cost"
orusersaid"what is the value of amazon share price?"
orusersaid"What is it's stock price?"
[...]
# CHANGE 2: Add flow that handles stock price questions
flowhandlingstockpricequestions
global$last_user_transcript
useraskedstockprice
$company_name=..."Return the name of the company the user was referring to in quotes \"<company name here>\" or \"unknown\" if the user did not mention a company."
if$company_name=="unknown"
botsay"Sorry, I can't understand which company you are referring to here. Can you rephrase your query?"
return
else
$price=awaitInvokeFulfillmentAction(endpoint="/stock/get_stock_price",company_name=$company_name)
ifnot$price
botsay"Could not find the stock price!"
else
botsay"Stock price of {$company_name} is {$price}"
[...]
flowhandlinguserrequestsuntiluserexpresseddone
[...]
activatehandlingbottalkinginterruption$mode="interrupt"
# CHANGE 3: Activate the flow
activatehandlingstockpricequestions
[...]

```

  1. Restart the updated bot and Event Simulator.


> ```
dockercompose-fdeploy/docker/docker-compose.ymldown
exportBOT_PATH=samples/event_interface_tutorial_bot/step_7
sourcedeploy/docker/docker_init.sh
dockercompose-fdeploy/docker/docker-compose.ymlupevent-bot-d
pythonevent_client.py

```

[ previous Tutorials ](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/index.html "previous page") [ next Building LangChain-Based Bots ](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-langchain-bot.html "next page")
On this page 
  * [Prerequisites](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#prerequisites)
  * [Step 1: Making the Greeting More Interesting](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#step-1-making-the-greeting-more-interesting)
  * [Step 2: Leveraging LLMs to Answer User Questions](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#step-2-leveraging-llms-to-answer-user-questions)
  * [Step 3: Making the Bot Proactive](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#step-3-making-the-bot-proactive)
  * [Step 4: Interrupting the Bot](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#step-4-interrupting-the-bot)
  * [Step 5: Back-Channeling](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#step-5-back-channeling)
  * [Step 6: Running Python Code](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#step-6-running-python-code)
  * [Step 7: Integrating a Plugin Service](https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#step-7-integrating-a-plugin-service)


[ ![NVIDIA](https://docs.nvidia.com/ace/ace-agent/latest/_static/nvidia-logo-horiz-rgb-1c-blk-for-screen.svg) ![NVIDIA](https://docs.nvidia.com/ace/ace-agent/latest/_static/nvidia-logo-horiz-rgb-1c-wht-for-screen.svg) ](https://www.nvidia.com)
[Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/) | [Manage My Privacy](https://www.nvidia.com/en-us/about-nvidia/privacy-center/) | [Do Not Sell or Share My Data](https://www.nvidia.com/en-us/preferences/start/) | [Terms of Service](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/) | [Accessibility](https://www.nvidia.com/en-us/about-nvidia/accessibility/) | [Corporate Policies](https://www.nvidia.com/en-us/about-nvidia/company-policies/) | [Product Security](https://www.nvidia.com/en-us/product-security/) | [Contact](https://www.nvidia.com/en-us/contact/)
Copyright © 2023-2025, NVIDIA Corporation. 
Last updated on Feb 27, 2025. 
