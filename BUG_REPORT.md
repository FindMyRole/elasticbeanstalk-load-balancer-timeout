# Elasticbeanstalk Load Balancer Timeout
<!--- Provide a general summary of the issue in the Title above -->

## Expected Behavior
* the eb environment instance should not timeout at 60 seconds
<!--- Tell us what should happen -->

## Current Behavior
* I am getting a 504 error
<!--- Tell us what happens instead of the expected behavior -->

## Possible Solution
* I am splitting the api call into 5 seperate calls in order to get all my data within the 60 limit timeframe
* I could try to leverage threading for the tasks to complete asynchrounously


<!--- Not obligatory, but suggest a fix/reason for the bug, -->

## Steps to Reproduce

<!--- Provide a link to a live example, or an unambiguous set of steps to -->
<!--- reproduce this bug. Include code to reproduce, if relevant -->
1. Create a new eb instance
2. Deploy the flask app in this repo
3. Find the corresponding load balancer in the EC2 console
4. Go to attributes -> Edit
5. Set the idle timeout to 4000
6. make an api call to the /timeout endpoint if you get a value past 60 seconds sucess else error

## Environment
|property|value|data|
|:------|:------:|------|
||||
||||
||||
||||
||||
||||

## Files
<!-- paste snippets as well as upload files -->




<!--- How has this issue affected you? What are you trying to accomplish? -->
<!--- Providing context helps us come up with a solution that is most useful in the real world -->

<!--- Provide a general summary of the issue in the Title above -->

## Detailed Description
<!--- Provide a detailed description of the change or addition you are proposing -->

## Possible Implementation
<!--- Not obligatory, but suggest an idea for implementing addition or change -->
