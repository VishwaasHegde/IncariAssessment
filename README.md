# IncariAssessment
This is my solution to the Incari assignment



## Pre requisite:
Install Docker from [Here](https://docs.docker.com/engine/install/)

Make sure you have at least 8 GB of space to store the docker images

## Running:
1. Clone the repository using `git clone https://github.com/VishwaasHegde/IncariAssessment.git`
2. Navigate to `IncariAssessment` folder using `cd IncariAssessment`
3. Run the project with the command
   1. `docker compose -f docker-compose-gpu.yml up -d` if you have a GPU (Recommended)
   2. `docker compose -f docker-compose-cpu.yml up -d` if you have a CPU
4. If you are running for the first time, the above command will take at least 10 minutes (depending on your network connection), as it downloads the Llama3.1 model and creates an image
5. From the next time onwards, it hardly takes time to get the system running
6. **Important Note**: Make sure your system does not have ports (for localhost) 8051, 8026, 8025, 11434 allotted to some other program, if some other program is accessing these ports, make sure to stop them or change their ports  
7. Go to the URL http://localhost:8501/
8. Give an input in the chat window, example: "Navigate to a new page after a delay of 3 seconds when the user clicks a button." and then click `Send`

## Evaluation:
1. In the evaluation section of the UI, give the actual and predicted values
   1. Example: actual: `[OnClick] [Delay] [Navigate]`. predicted: `[OnClick] [Delay]`
2. Click on evaluate to get the Bleu, Rouge and Minimum Edit distance scores

## Test cases:
1. Run the test cases using the command `docker start -i incaritest`
2. This should print the test results and you should see 7 test cases passes
