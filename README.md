## Setting up your Start Foundry VTT Alexa Skill in the Developer Console

1.  **Go to the [Alexa Developer Console](http://developer.amazon.com/alexa?&sc_category=Owned&sc_channel=RD&sc_campaign=Evangelism2018&sc_publisher=github&sc_content=Survey&sc_detail=quiz-game-python-V2_GUI-1&sc_funnel=Convert&sc_country=WW&sc_medium=Owned_RD_Evangelism2018_github_Survey_quiz-game-python-V2_GUI-1_Convert_WW_beginnersdevs&sc_segment=beginnersdevs).  In the top-right corner of the screen, click the "Sign In" button.**
(If you don't already have an account, you will be able to create a new one for free.)

1.  Once you have signed in, select the **Developer Console** link and then **Alexa Skills Kit**.

1.  From the **Alexa Developer Console** select the **Create Skill** button near the top-right of the list of your Alexa Skills.

1. Give your new skill a **Name**, for example, 'Start Foundry'. 

1. Select the Default Language.  This tutorial will presume you have selected 'English (US)'.

1. Select the **Custom** model under the *'Choose a model to add to your skill'* section. Choose Alexa Hosted Python. Click the **Create Skill** button at the top right.

1. Choose **Start from scratch** from the *Choose a template* section and click the **Choose** button on the top right.

1. **Build the Interaction Model for your skill**
	1. On the left hand navigation panel, select the **JSON Editor** tab under **Interaction Model**. In the textfield provided, replace any existing code with the code provided in the [Interaction Model](./models/en-US.json).  Click **Save Model**.
    2. If you want to change the skill invocation name, select the **Invocation** tab. Enter a **Skill Invocation Name**. This is the name that your users will need to say to start your skill.  In this case, it's preconfigured to be 'foundry'.
    3. Click "Build Model".

	**Note:** You should notice that **Intents** and **Slot Types** will auto populate based on the JSON Interaction Model that you have now applied to your skill. 

1. If your interaction model builds successfully, proceed to the next step. If not, you should see an error. 