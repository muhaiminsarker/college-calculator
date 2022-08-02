### Purpose
Honestly, I made this for my cousin who is about to apply for college. I'm currently in college so this isn't of much use to me. Either way, I hope it'll help my cousin or anyone in my cousin's situation. 

### SAT College Calculator
The main idea behind this is to use the SAT Score that you've gotten and match you to colleges based on your SAT score. This will take into account the 25 percentile and 75 percentile. It'll show you what percentile you are for a specific college and whether the college is safety, match, or reach. You can also filter it out by the state of the college or view only T20s. 

##### Steps
1. Use Selenium and/or Beautiful Soup to get the SAT data on all the colleges
	1. Alternatively, you can just get a Kaggle dataset or any dataset which showcases this
2. Have the user input their SAT Score into a textbox within the website you create 
3. Output Safeties, Matches, and Reaches to different columns or buttons 
	1. Make sure that if a student is extremely out of range (meaning they have a 1300 and they are trying to get into Columbia whose 25 percentile may be a  1450, do not output it at all)
	2. Additionally, make sure that you create a note saying that it doesn't reflect the entire story as your demographics, essays, ECs can make it more possible for you to get in. I am only checking based on the criteria for them to look at your application

##### How To Use
If you have python installed, make sure to install all dependencies needed. 
Run the following command to get all the dependencies you need within the project's directory:
''' 
pip install requirements.txt
'''

