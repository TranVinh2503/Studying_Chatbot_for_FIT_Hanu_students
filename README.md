# Studying_Chatbot_for_FIT_Hanu_students
The academic advising chatbot for Hanoi University's Faculty of Information Technology (FIT) has made significant progress in providing personalized support and detailed information to students and lecturers. Using advanced techniques in machine learning and natural language processing, chatbots are capable of classifying intent, extracting information, and providing diverse and effective learning support. This study presents the development of chatbots capable of understanding natural English and Vietnamese languages. The system is capable of generating responses, taking user actions, and retaining the context of the conversation. My chatbot is developed by Bert, PhoBert, DIETClassifier, EntitySynonymMapper, WhitespaceTokenizer models and has been integrated into Rasa framework. Evaluation results based on the Bert and PhoBert models compared with Rasa Core show that the chatbot has brought significant efficiency with higher accuracy. Chatbot is deployed on Hanoi University's official admission fanpage on Facebook platform, one of the most famous social networks in Vietnam. 

In the project, 2 chatbots were established. Firstly, for the Vietnamese language uses the PhoBERT model. Sencondly, for the English language uses the model BERT.

Here is some command line interface (CLI) which gives you easy-to-remember commands for common tasks: 

**rasa init**	Creates a new project with example training data, actions, and config files.

**rasa train**	Trains a model using your NLU data and stories, saves trained model in ./models.

**rasa interactive**	Starts an interactive learning session to create new training data by chatting to your assistant.

**rasa shell**	Loads your trained model and lets you talk to your assistant on the command line.

**rasa run**	Starts a server with your trained model.

**rasa run actions**	Starts an action server using the Rasa SDK.

**rasa visualize**Generates a visual representation of your stories.

**rasa test**	Tests a trained Rasa model on any files starting with test_.

**rasa test e2e**	Runs end-to-end testing fully integrated with the action server that serves as acceptance testing.

**rasa data split nlu**	Performs a 80/20 split of your NLU training data.

**rasa data split stories**	Do the same as rasa data split nlu, but for your stories data.

**rasa data convert** Converts training data between different formats.

**rasa data migrate**	Migrates 2.0 domain to 3.0 format.
**rasa data validate**	Checks the domain, NLU and conversation data for inconsistencies.
**rasa export**	Exports conversations from a tracker store to an event broker.
**rasa evaluate markers**	Extracts markers from an existing tracker store.
**rasa marker upload**	Upload marker configurations to Analytics Data Pipeline
**rasa license**	Display licensing information.
**rasa -h**	Shows all available commands.
